from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, logout, login
from datetime import date
from django.db.models import Q
from .utils import send_enquiry_email, generate_random_password, send_member_credentials
from django.http import HttpResponse, JsonResponse
import random
from django.contrib import messages
from .models import Member
from django.core.paginator import Paginator
import openai
# Create your views here.
openai.api_key = ""

def index(request):
    return render(request, "index.html")

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST["uname"]
        p = request.POST["pwd"]
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
            return render(request, "failure.html")
    return render(request, "login_admin.html", locals())

def failure(request):
    return render(request, "failure.html")


def admin_home(request):
    if not request.user.is_staff:
        return redirect("admin_login")
    en = Enquiry.objects.all().count()
    eq = Equipment.objects.all().count()
    p = Plan.objects.all().count()
    m = Member.objects.all().count()

    d = {"en": en, "eq": eq, "p": p, "m": m}
    return render(request, "admin_home.html", d)


def member_home(request):
    return render(request, "member_home.html")


def contact(request):
    error = ""
    if request.method == "POST":
        n = request.POST["name"]
        e = request.POST["emailid"]
        c = request.POST["contact"]
        s = request.POST["subject"]
        m = request.POST["message"]
        try:
            Contact.objects.create(
                name=n,
                emailid=e,
                contact=c,
                subject=s,
                message=m,
                msgdate=date.today(),
                isread="no",
            )
            error = "no"
        except:
            error = "yes"
    return render(request, "contact.html", locals())


def member_enquiry(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        emailid = request.POST.get("emailid")
        branch = request.POST.get("branch")
        issue = request.POST.get("issue")
        message = request.POST.get("message")

        enquiry = MemberEnquiry(
            name=name,
            contact=contact,
            emailid=emailid,
            branch=branch,
            issue=issue,
            message=message,
        )
        enquiry.save()

        recipient_list = [
            "gymsync.official@gmail.com",
        ]
        if branch == "Branch 1":
            recipient_list.append("raghuu715@gmail.com")
        elif branch == "Branch 2":
            recipient_list.append("dirghayu1777@gmail.com")
        else:
            recipient_list.append("suryastiwari2222@gmail.com")
        # Send the email
        try:
            send_enquiry_email(issue, message, emailid, recipient_list)
            error = "no"
        except:
            error = "yes"

        recipient_list = [
            "gymsync.official@gmail.com",
        ]
        return render(request, "member_enquiry.html", {"error": error})

    return render(request, "member_enquiry.html")


def addEnquiry(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')  # Replace with your actual login view name
    
    error = ""
    if request.method == "POST":
        # Get form data
        n = request.POST.get("name")
        m = request.POST.get("mobile")
        e = request.POST.get("email")
        a = request.POST.get("age")
        g = request.POST.get("gender")
        
        try:
            # Create new enquiry entry
            Enquiry.objects.create(name=n, mobile=m, email=e, age=a, gender=g)
            error = "no"  # Successfully saved
        except Exception as e:
            print(f"Error: {e}")  # Log the error to the console for debugging
            error = "yes"  # Something went wrong

    # Render the template and pass the error variable
    return render(request, "add_enquiry.html", {'error': error})

def viewEnquiry(request):
    # Fetch all enquiry entries from the database
    enquiries = Enquiry.objects.all()  # You can add filters if needed
    return render(request, "viewEnquiry.html", locals())


def edit_Enquiry(request, pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect(admin_login)
    user = request.user
    enquiry = Enquiry.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST["name"]
        m1 = request.POST["mobile"]
        e1 = request.POST["email"]
        a1 = request.POST["age"]
        g1 = request.POST["gender"]

        enquiry.name = n1
        enquiry.mobile = m1
        enquiry.email = e1
        enquiry.age = a1
        enquiry.gender = g1
        try:
            enquiry.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "edit_Enquiry.html", locals())


def delete_Enquiry(request, pid):
    enquiry = Enquiry.objects.get(id=pid)
    enquiry.delete()
    return redirect("viewEnquiry")


from django.shortcuts import render, redirect
from .models import Plan

def addPlan(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')  # Ensure 'admin_login' is a valid URL pattern

    error = ""
    if request.method == "POST":
        p = request.POST["name"]
        a = request.POST["amount"]
        d = request.POST["duration"]
        try:
            Plan.objects.create(name=p, amount=a, duration=d)
            return redirect('viewPlan')  # Redirect to the viewPlan page after successful addition
        except Exception as e:
            error = "yes"
            print(f"Error: {e}")  # Log the error for debugging purposes

    return render(request, "addPlan.html", {"error": error})


def viewPlan(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')  # Make sure 'admin_login' is a valid URL pattern
    plans = Plan.objects.all()  # Fetch all plan records from the database
    return render(request, "viewPlan.html", {'plans': plans}) 


def edit_Plan(request, pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect(admin_login)
    user = request.user
    plan = Plan.objects.get(id=pid)
    if request.method == "POST":
        p1 = request.POST["name"]
        a1 = request.POST["amount"]
        d1 = request.POST["duration"]

        plan.name = p1
        plan.amount = a1
        plan.duration = d1
        try:
            plan.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "edit_Plan.html", locals())


def delete_Plan(request, pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect("viewPlan")


def addEquipment(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    if request.method == "POST":
        n = request.POST["name"]
        p = request.POST["price"]
        u = request.POST["unit"]
        pd = request.POST["purchasedate"]
        d = request.POST["description"]

        try:
            Equipment.objects.create(
                name=n, price=p, unit=u, purchasedate=pd, description=d
            )
            error = "no"
        except:
            error = "yes"
    return render(request, "addEquipment.html", locals())


def viewEquipment(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    equipment_list = Equipment.objects.all()  # Retrieve all equipment records
    return render(request, "viewEquipment.html", {"equipment_list": equipment_list})



def edit_Equipment(request, pid):
    error = ""
    if not request.user.is_authenticated:
        return redirect(admin_login)
    user = request.user
    equipment = Equipment.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST["name"]
        p1 = request.POST["price"]
        u1 = request.POST["unit"]
        d1 = request.POST["description"]

        equipment.name = n1
        equipment.price = p1
        equipment.unit = u1
        equipment.description = d1
        try:
            equipment.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "edit_Equipment.html", locals())


def delete_Equipment(request, pid):
    equipment = Equipment.objects.get(id=pid)
    equipment.delete()
    return redirect("viewEquipment")


import random


def addMember(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    plan1 = Plan.objects.all()

    # Define room groups based on plans
    room_groups = {
        "Golden Plan": ["GymSync GP 1", "GymSync GP 2", "GymSync GP 3"],
        "Silver Plan": ["GymSync SP 1", "GymSync SP 2", "GymSync SP 3"],
        "Silver Plan Double": ["GymSync SPD 1", "GymSync SPD 2", "GymSync SPD 3"],
    }

    if request.method == "POST":
        n = request.POST["name"]
        c = request.POST["contact"]
        e = request.POST["email"]
        g = request.POST["gender"]
        p = request.POST["plan"]
        j = request.POST["joindate"]
        i = request.POST["initamount"]

        # Retrieve the plan object
        plan = Plan.objects.get(name=p)

        # Generate a unique random password
        password = generate_random_password()

        room_names = room_groups.get(plan.name)
        chatroom_name = random.choice(room_names) if room_names else None

        try:
            member = Member.objects.create(
                name=n,
                contact=c,
                email=e,
                password=password,
                gender=g,
                plan=plan,
                joindate=j,
                initamount=i,
                chatroom_id=chatroom_name,  # Assign chatroom name directly
            )

            # Send an email with the credentials
            send_member_credentials(e, n, chatroom_name, plan.name, password)

            error = "no"
        except Exception as ex:
            print("Error adding member:", ex)
            error = "yes"
            return render(request, "failure.html")

    d = {"error": error, "plan": plan1}
    return render(request, "addMember.html", d)


# Member login view
def member_login(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")

        try:
            member = Member.objects.get(name=username, password=password)
            request.session["member_id"] = (
                member.id
            )  # Store member id in session for logged-in user
            error = "no"  # Login successful
        except Member.DoesNotExist:
            error = "yes"  # Login failed, incorrect credentials
            return render(request, "failure.html")

    return render(request, "member_login.html", {"error": error})


def viewMember(request):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    member = Member.objects.all()
    return render(request, "viewMember.html", locals())


def edit_Member(request, pid):
    if not request.user.is_authenticated:
        return redirect(admin_login)
    error = ""
    user = request.user
    member = Member.objects.get(id=pid)
    if request.method == "POST":
        n1 = request.POST["name"]
        c1 = request.POST["contact"]
        e1 = request.POST["email"]
        g1 = request.POST["gender"]
        i1 = request.POST["initamount"]

        member.name = n1
        member.contact = c1
        member.email = e1
        member.gender = g1
        member.initamount = i1
        try:
            member.save()
            error = "no"
        except:
            error = "yes"
    return render(request, "edit_Member.html", locals())


def delete_Member(request, pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect("viewMember")


def unread_queries(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    contact = Contact.objects.filter(isread="no")
    return render(request, "unread_queries.html", locals())


def read_queries(request):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    contact = Contact.objects.filter(isread="yes")
    return render(request, "read_queries.html", locals())


def view_queries(request, pid):
    if not request.user.is_authenticated:
        return redirect("admin_login")
    contact = Contact.objects.get(id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request, "view_queries.html", locals())


def delete_contact(request, pid):
    contact = Contact.objects.get(id=pid)
    contact.delete()
    return redirect("read_queries")


def member_plans(request):
    return render(request, "member_plan.html")


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect("index")
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST["oldpassword"]
        n = request.POST["newpassword"]
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = "not"
        except:
            error = "yes"
    return render(request, "changePassword.html", locals())


def member_queries(request):
    # Fetch all member queries from the database
    queries = MemberEnquiry.objects.all()

    # Render the queries to a template
    return render(request, "member_queries.html", {"queries": queries})


def Logout(request):
    logout(request)
    return redirect("index")


# Chat Room Views:
def home(request):
    return render(request, "home.html")


def room(request, room):
    username = request.GET.get("username")
    room_details = get_object_or_404(
        Room, name=room
    )  # This will return a 404 page if the room doesn't exist
    return render(
        request,
        "room.html",
        {"username": username, "room": room, "room_details": room_details},
    )


def checkview(request):
    room_name = request.POST["room_name"]
    username = request.POST["username"]
    password = request.POST["password"]

    # Fetch the member based on username, password, and room
    try:
        member = Member.objects.get(
            name=username, password=password, chatroom_id=room_name
        )
        # Redirect to the room if the details match
        return redirect(f"/{room_name}/?username={username}")
    except Member.DoesNotExist:
        # If details don't match, show an error message on the home page
        messages.error(
            request, "Invalid room name, username, or password. Please try again."
        )
        return redirect("failure")


def send(request):
    message = request.POST["message"]
    username = request.POST["username"]
    room_id = request.POST["room_id"]

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse("Message sent successfully")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    # Get the latest 5 messages in descending order and convert to a list of dictionaries
    messages = list(Message.objects.filter(room=room_details.id).order_by('-date').values()[:5])
    # Reverse the list to show the oldest message at the top
    messages.reverse()
    return JsonResponse({"messages": messages})


def generate_diet_plan(height, weight, sex, age, activity_level):
    # AI-based logic for generating personalized diet plan
    # Construct the prompt for GPT-3/ChatGPT
    prompt = f"Generate a personalized diet plan for a {age}-year-old {sex} who is {height} cm tall, weighs {weight} kg, and has a {activity_level} activity level."

    try:
        # Use OpenAI's new ChatCompletion API to generate the diet plan
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can change to another model if needed
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )

        # Extract the diet plan from the response
        diet_plan = response['choices'][0]['message']['content'].strip()
        return diet_plan
    except Exception as e:
        return f"Error generating diet plan: {e}"
    
def personalized_diet_plan(request):
    diet_plan = None
    if request.method == "POST":
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        activity_level = request.POST.get('activity_level')

        # Validate input (add more validations as necessary)
        if height and weight and sex:   
            # Call the AI function to generate the diet plan
            diet_plan = generate_diet_plan(height, weight, sex, age, activity_level)

    return render(request, 'personalized_diet_plan.html', locals())
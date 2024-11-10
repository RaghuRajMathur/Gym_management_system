# utils.py
from django.core.mail import EmailMessage
import random
import string


def send_enquiry_email(issue, message, sender_email, recipient_list):
    subject = issue
    body = message
    email = EmailMessage(
        subject,
        body,
        "gymsync.official@gmail.com",  # This will be the "From" address
        recipient_list,  # List of recipient email addresses
        reply_to=[sender_email],  # Reply-to email is the sender's email
    )
    email.send(fail_silently=False)


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for i in range(length))


def send_member_credentials(email, name, chatroom, plan, password):
    subject = "Welcome to the GymSync!"
    body = f"""
    Hello {name},

    Welcome to our Gym! Here are your login details:
    - Username: {name}
    - Password: {password}
    - Chatroom: {chatroom}
    - Plan: {plan}

    Enjoy your time with us!

    Best regards,
    Team GymSync
    """
    email = EmailMessage(
        subject, body, "gymsync.official@gmail.com", [email], reply_to=[email]
    )
    email.send(fail_silently=False)

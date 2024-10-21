# utils.py
from django.core.mail import EmailMessage


def send_enquiry_email(issue, message, sender_email, recipient_list):
    subject = issue
    body = message
    email = EmailMessage(
        subject,
        body,
        "dirghayu1777@gmail.com",  # This will be the "From" address
        recipient_list,  # List of recipient email addresses
        reply_to=[sender_email],  # Reply-to email is the sender's email
    )
    email.send(fail_silently=False)

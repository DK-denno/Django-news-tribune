from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def welcome_email(name,receiver):
    #creating the message sender and subject
    subject='Welcome to Moring Tribune'
    sender='dennisveer27@gmail.com'

    #creaing the content to send with the email
    text_content = render_to_string('email/email.txt',{"name":name})
    html_content = render_to_string('email/email.html',{"name":name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()

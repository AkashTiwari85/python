from email.message import EmailMessage
from email_sender import email_password
import ssl
import smtplib
email_sender='akhileshtiwar40@gmail.com'
email_password = 6306061542
email_receiver='aktiwari8543@gmail.com'
subject="Hi i am aktiwari"
body=""" If you want to learn any programming language
like java, python, c ,c++, then you can do."""
em=EmailMessage()
em['From']=email_sender
em['to']=email_receiver
em['subject']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
 smtp.login(email_password,email_password)
 smtp.sendmail(email_sender,email_receiver,em.as_string())
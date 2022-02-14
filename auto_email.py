import smtplib
from email.message import EmailMessage

def sender():
  email = EmailMessage()
  email['from'] = '<sender's mail adress>'
  email['to'] = '<reciever's mail adress >'
  email['subject'] = '<subject>'

  email.set_content(mes)
  
#This is to send email from gmail client.You can also use other clients
  with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('<put your email adress here>', '<put your password here>')
    smtp.send_message(email)
    
sender()
''' Author: Andhika Malik
    Reference:  1. https://youtu.be/q0yAR04avXk
                2. https://bit.ly/fransHalasonIndonesiaAI
'''

from email.utils import formataddr
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import *

# membaca file receiver_list
email_txt = open('receiver_list.txt', 'r')
email_list = (email_txt.read().splitlines())

# membuat list kosong, serta memasukan data dari email_list ke dalam email (berbentuk list)
email_name = []
for email in email_list:
    name = email.split('@')
    email_name.append(name[0])

# membaca file html
email_html = open('email.html')
template = email_html.read()

# memberikan gambar
pngname = 'gambar.png'

receiver = email_list
name = email_name
i = 1

# perulangan for untuk mengirim email sebanyak email yang terdaftar pada file receiver_list
for receiver_email, receiver_name in zip(receiver, name):
    print('mengirim email...')
    
    # konfigurasi email
    msg = MIMEMultipart()
    msg['Subject'] = 'Final Project - Email Automation'
    msg['From'] = 'Andhika Malik'
    msg['To'] = formataddr((receiver_name, receiver_email))

    # memberikan template
    msg.attach(MIMEText(template, 'html'))

    # membaca file gambar
    with open(pngname, 'rb') as attachment:
        png = MIMEBase("application", "octet-stream")
        png.set_payload(attachment.read())
        
        encoders.encode_base64(png)
            
        # menambahkan header file
        png.add_header(
            "Content-Disposition",
            "attachment",
            filename = pngname
        )
        msg.attach(png)
        
    # mengirimkan email
    context = ssl.create_default_context()
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls(context=context)
        server.login(username_email, pass_email)
        server.sendmail(username_email, receiver_email, msg.as_string())
        server.quit()
        
        print('email {} terkirim\n'.format(i))
        i += 1
        
print('semua email terkirim\n--------------------')
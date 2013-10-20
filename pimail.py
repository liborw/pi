import smtplib
from email.mime.text import MIMEText

import conf

msg = MIMEText("It works!")
msg['Subject'] = 'RPi: Startup Message'
msg['From'] = conf.GMAIL_MAIL
msg['To'] = conf.GMAIL_MAIL

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(conf.GMAIL_USER,conf.GMAIL_PASS)
server.sendmail(conf.GMAIL_MAIL, conf.GMAIL_MAIL, msg.as_string())

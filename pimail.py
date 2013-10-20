import smtplib
from email.mime.text import MIMEText
import subprocess

import conf

co = subprocess.Popen(['ifconfig'], stdout = subprocess.PIPE)
ifconfig = co.stdout.read()

text  = "\n$ ifconfig\n"
text += ifconfig

msg = MIMEText(text)
msg['Subject'] = 'RPi: Startup Message'
msg['From'] = conf.GMAIL_MAIL
msg['To'] = conf.GMAIL_MAIL

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(conf.GMAIL_USER,conf.GMAIL_PASS)
server.sendmail(conf.GMAIL_MAIL, conf.GMAIL_MAIL, msg.as_string())

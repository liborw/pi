import smtplib
from email.mime.text import MIMEText
import subprocess
import urllib2

import conf

co = subprocess.Popen(['ifconfig'], stdout = subprocess.PIPE)
ifconfig = co.stdout.read()
my_ip = urllib2.urlopen('http://ident.me/').read()

text  = "\n$ ifconfig\n"
text += ifconfig
text += "\nPublic IP: " + my_ip + "\n"

msg = MIMEText(text)
msg['Subject'] = 'RPi: Startup Message'
msg['From'] = conf.GMAIL_MAIL
msg['To'] = conf.GMAIL_MAIL

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(conf.GMAIL_USER,conf.GMAIL_PASS)
server.sendmail(conf.GMAIL_MAIL, conf.GMAIL_MAIL, msg.as_string())

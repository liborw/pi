import smtplib
import conf

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(conf.GMAIL_USER,conf.GMAIL_PASS)
server.sendmail(conf.GMAIL_MAIL, conf.GMAIL_MAIL, "It works!")

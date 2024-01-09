import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

password = "oknh jqss icgm kxje"
username = "marcfeitosa1@gmail.com"

receiver = "marcfeitosa1@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Greetings from the app
Hi, how are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)


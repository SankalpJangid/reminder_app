import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_list.settings')
django.setup()

from reminder.models import Details
from django.contrib.auth.models import User
import datetime
import smtplib
import time

def send():
    now = datetime.datetime.now()
    now_s = now.strftime("%Y-%m-%d"+'T'+"%H:%M")
    time_of_user = Details.objects.values_list('datetime',flat=True)
    if now_s in time_of_user:
        mail_time = Details.objects.get(datetime=now_s)
        name = str(mail_time.user)
        message_detail = str(mail_time.detail)
        print(message_detail)
        mail_send = User.objects.get(username=name)
        mail = str(mail_send.email)
        print(mail)
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login("sender mail", "password")
            message = f"""
To: {mail}
Subject: Reminder for your work

Reminder

Your Work: {message_detail}

This mail is computer generated and therefore does not reply to it.
"""
            server.sendmail("sender mail",mail , message)
            server.quit()
            time.sleep(59)
            print("Email successfully sent")
        except:
            print("Mail not sent")

if __name__ == "__main__":

    while True:
        send()

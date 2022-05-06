import os
import smtplib
from email.mime.text import MIMEText


def get_payload(message):
    msg = MIMEText(message)

    msg['From'] = 'kkona@umd.edu'
    return msg.as_string()

class Mailer:

    def __init__(self):
        self.port = 465
        self.sender = os.environ['EMAIL_USERNAME']
        self.password = os.environ['EMAIL_PASSWORD']
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.sender, self.password)
        self.mailer = s

    def send(self, message):

        payload = get_payload(message)

        self.mailer.sendmail(self.sender, "3023452467@vtext.com", payload)

    def quit(self):
        self.mailer.quit()


if __name__ == "__main__":
    mailer = Mailer()
    mailer.send('a' * 142 +'bcdef')

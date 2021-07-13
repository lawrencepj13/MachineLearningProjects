import tkinter
MyRoot = tkinter.Tk()
MyRoot.title("PHQ7 Survey")

def EntryBoxFunc():
    Label1.config(text = "Hello, Please fill out this PHQ7 Survey")
Label1 = tkinter.Label(MyRoot, text = "Please enter you full name")
Label1.pack(padx=30,pady=10)


def question_one():
    Label2 = tkinter.Label(MyRoot, text="What is your gender?")
    v0 = tkinter.IntVar()
    v0.set(1)
    r1 = tkinter.Radiobutton(MyRoot, text="Male", variable=v0, value=1)
    r2 = tkinter.Radiobutton(MyRoot, text="Female", variable=v0, value=2)
    r1.place(x=100, y=50)
    r2.place(x=180, y=50)
    Label2.pack(anchor='w')
    r1.pack(anchor='w')
    r2.pack(anchor='w')


def question_two():
    Label3 = tkinter.Label(MyRoot, text="How old are you?")
    v0 = tkinter.IntVar()
    v0.set(1)
    r3 = tkinter.Radiobutton(MyRoot, text="18-30", variable=v0, value=3)
    r4 = tkinter.Radiobutton(MyRoot, text="31-50", variable=v0, value=4)
    r5 = tkinter.Radiobutton(MyRoot, text="51-70", variable=v0, value=5)
    r6 = tkinter.Radiobutton(MyRoot, text="70+", variable=v0, value=6)
    Label3.pack(anchor='w')
    r3.pack(anchor='w')
    r4.pack(anchor='w')
    r5.pack(anchor='w')
    r6.pack(anchor='w')

def question_three():
    Label4 = tkinter.Label(MyRoot, text="How often do you have little interest in doing things?")
    v0 = tkinter.IntVar()
    v0.set(1)
    r3 = tkinter.Radiobutton(MyRoot, text="Not at all", variable=v0, value=3)
    r4 = tkinter.Radiobutton(MyRoot, text="Several days", variable=v0, value=4)
    r5 = tkinter.Radiobutton(MyRoot, text="More than half days", variable=v0, value=5)
    r6 = tkinter.Radiobutton(MyRoot, text="Nearly every day", variable=v0, value=6)
    Label4.pack(anchor='w')
    r3.pack(anchor='w')
    r4.pack(anchor='w')
    r5.pack(anchor='w')
    r6.pack(anchor='w')

def question_four():
    Label5 = tkinter.Label(MyRoot, text="How often are you feeling down, depressed or hopeless?")
    v0 = tkinter.IntVar()
    v0.set(1)
    r3 = tkinter.Radiobutton(MyRoot, text="Not at all", variable=v0, value=3)
    r4 = tkinter.Radiobutton(MyRoot, text="Several days", variable=v0, value=4)
    r5 = tkinter.Radiobutton(MyRoot, text="More than half days", variable=v0, value=5)
    r6 = tkinter.Radiobutton(MyRoot, text="Nearly every day", variable=v0, value=6)
    Label5.pack(anchor='w')
    r3.pack(anchor='w')
    r4.pack(anchor='w')
    r5.pack(anchor='w')
    r6.pack(anchor='w')

def question_five():
    Label6 = tkinter.Label(MyRoot, text="How often do you have trouble falling asleep, staying asleep or sleeping too much?")
    v0 = tkinter.IntVar()
    v0.set(1)
    r3 = tkinter.Radiobutton(MyRoot, text="Not at all", variable=v0, value=3)
    r4 = tkinter.Radiobutton(MyRoot, text="Several days", variable=v0, value=4)
    r5 = tkinter.Radiobutton(MyRoot, text="More than half days", variable=v0, value=5)
    r6 = tkinter.Radiobutton(MyRoot, text="Nearly every day", variable=v0, value=6)
    Label6.pack(anchor='w')
    r3.pack(anchor='w')
    r4.pack(anchor='w')
    r5.pack(anchor='w')
    r6.pack(anchor='w')

def question_six():
    Label7 = tkinter.Label(MyRoot, text="How often are you feeling tired or have little energy?")
    v0 = tkinter.IntVar()
    v0.set(1)
    r3 = tkinter.Radiobutton(MyRoot, text="Not at all", variable=v0, value=3)
    r4 = tkinter.Radiobutton(MyRoot, text="Several days", variable=v0, value=4)
    r5 = tkinter.Radiobutton(MyRoot, text="More than half days", variable=v0, value=5)
    r6 = tkinter.Radiobutton(MyRoot, text="Nearly every day", variable=v0, value=6)
    Label7.pack(anchor='w')
    r3.pack(anchor='w')
    r4.pack(anchor='w')
    r5.pack(anchor='w')
    r6.pack(anchor='w')

def quit_button():
    quit_button = tkinter.Button(MyRoot, text="Quit", command=MyRoot.destroy, width=5, bg="blue", fg="white", font=("ariel", 16, " bold"))
    quit_button.pack(side =tkinter.LEFT)


def submit_button():
    submit_button = tkinter.Button(MyRoot, text="Submit", command=MyRoot.destroy, width=5, bg="blue", fg="white",
                                 font=("ariel", 16, " bold"))
    submit_button.pack(side=tkinter.RIGHT)




def run():
    EntryBoxFunc()
    question_one()
    question_two()
    question_three()
    question_four()
    question_five()
    question_six()
    quit_button()
    submit_button()

run()

MyRoot.mainloop()
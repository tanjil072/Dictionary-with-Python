import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import json
import pyttsx3

# initialisation
engine = pyttsx3.init('sapi5')
# voiceDecision = (input('do you want voice support? \nyes : y\nno : n\n')).lower()

placeholder = "Please Type the word"
voiceDecision = 'y'
meaning = ''
EntryString=''
decision=''
l=''


def unmute():
    global voiceDecision
    voiceDecision = 'y'


def mute():
    global voiceDecision
    voiceDecision = 'n'


def read(line):
    if voiceDecision == 'y':
        engine.say(line)
        engine.runAndWait()

    else:
        pass


root = tk.Tk()

canvas1 = tk.Canvas(root, width=500, height=400)
canvas1.pack()

def update_meaning(word):
    read('Will you provide the meaning to our database')
    ProvideMeaning()

    if decision.lower() == 'y':
        read('Please type the meaning')
        USER_INP = simpledialog.askstring(title="Meaning",
                                          prompt="Please type the meaning")
        tk.messagebox.showinfo('Return', 'Thanks for your feedback')
        read('Thanks for your feedback')
        x[word] = [USER_INP]
        global l

       # print('The meaning of {} is {}'.format(EntryString, x[word]))
        global meaning
        meaning=''
        meaning='The meaning of {} is {}'.format(EntryString, x[word])
        l = tk.Label(canvas1, text=meaning, wraplength=220)
        l.place(x=80, y=100)
        read('The meaning of {} is {}'.format(EntryString, x[word]))
        with open('my_dictionary_database.json', 'w') as f:
            json.dump(x, f, indent=2, sort_keys=True)

    else:
        tk.messagebox.showinfo('Return', 'Maybe next time!!Thanks for using!')
        read('Maybe next time!!Thanks for using!')

with open('my_dictionary_database.json') as f:
    x = json.load(f)  # open the database


def search():
    global EntryString
    EntryString=E1.get()
    word = EntryString.lower()
    if word not in x:
        read('Sorry we dont have the word in our database.')
        messagebox.showinfo('Warning', 'Sorry we dont have the word in our database')
        update_meaning(word)
    else:
        global meaning
        meaning = 'The meaning of {} is {}\n'.format(EntryString, x[word])
        global l
        l = tk.Label(canvas1, text=meaning,wraplength=220)
        l.place(x=80, y=100)
        read('The meaning of {} is {}\n'.format(EntryString, x[word]))


b1 = tk.Button(canvas1, text="Search", width=10, command=search)
b1.place(relx=1, x=-120, y=20)
# Entry widget
E1 = tk.Entry(bd=3)
E1.insert(0, placeholder)
read('please type the word')
E1.place(relx=1, x=-420, y=22, height=30, width=190)


# label widget





def ProvideMeaning():
    MsgBox = tk.messagebox.askquestion('Provide Meaning', 'Will you provide the meaning to our database?',
                                       icon='warning')
    if MsgBox == 'yes':
        global decision
        decision='y'
    else:
        tk.messagebox.showinfo('Return', 'You will now return to the application screen')


photo = tk.PhotoImage(file=r"C:\Users\Tanjil\PycharmProjects\Dictionary\mute.png")
photoimage = photo.subsample(30, 30)

photo2 = tk.PhotoImage(file=r"C:\Users\Tanjil\PycharmProjects\Dictionary\speaker.png")
photoimage2 = photo2.subsample(30, 30)

mute = tk.Button(root, text='', image=photoimage, command=mute, bg='brown', fg='white')
canvas1.create_window(480, 380, window=mute)

unmute = tk.Button(root, text='', image=photoimage2, command=unmute, bg='brown', fg='white')
canvas1.create_window(450, 380, window=unmute)

root.mainloop()

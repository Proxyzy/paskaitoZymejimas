from tkinter import *

from tkinter import ttk

from addStudent import createStudent
from recognizer import rec
import os





window = Tk()

window.title("Lankomumo sistema")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(master=tab_control, width=300, height=300)
tab2 = ttk.Frame(master=tab_control, width=300, height=300)
tab3 = ttk.Frame(master=tab_control, width=300, height=300)

tab_control.add(tab1, text='Žymėjimas')
tab_control.add(tab2, text='Registracija')
tab_control.add(tab3, text='Mokymas')

lbl1 = Label(tab1, text= 'Studento žymejimas paskaitoje')
lbl1.config(font=('helvetica', 14))

def recognizeStudents():
    rec()

button1 = Button(tab1, text='Pradėti žymėjimą', command=recognizeStudents, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))



lbl1.pack(pady=25, side=TOP)
button1.pack(pady=25, side=TOP)

lbl2 = Label(tab2, text= 'Registruoti naują studentą')
lbl2.config(font=('helvetica', 14))

tlbl = Label(tab2, text= 'Pilnas studento vardas:')
tlbl.config(font=('helvetica', 10))

entry1 = Entry(tab2)
def addStudent():
    x1 = entry1.get()
    createStudent(x1)

button2 = Button(tab2, text='Registruoti studentą', command=addStudent, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

lbl2.pack(pady=25, side=TOP)
tlbl.pack(pady=0, side=TOP)
entry1.pack(pady=0, side=TOP)
button2.pack(pady=25, side=TOP)

lbl3 = Label(tab3, text= 'Studentų atpažinimo mokymas')
lbl3.config(font=('helvetica', 14))

def detectFaces():
    os.system("DetectAllFaces.py")

button3 = Button(tab3, text='Aptikti veidus turimose nuotraukose', command=detectFaces, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

def createEmbeddings():
    os.system("CreateEnbeddings.py")

button4 = Button(tab3, text='Sugeneruoti veidų bruožų vektorius', command=createEmbeddings, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

def recTraining():
    os.system("FaceClassification.py")

button5 = Button(tab3, text='Mokinti atpažinimo algoritmą', command=recTraining, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))

lbl3.pack(pady=25, side=TOP)
button3.pack(pady=5, side=TOP)
button4.pack(pady=5, side=TOP)
button5.pack(pady=5, side=TOP)




tab_control.pack(expand=1, fill='both')

window.mainloop()



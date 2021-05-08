import tkinter as tk
from addStudent import createStudent
from recognizer import rec

panel = tk.Tk()

canvas1 = tk.Canvas(panel, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(panel, text='Administratoriaus langas')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(panel, text='Enter Students Name:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(panel)
canvas1.create_window(200, 140, window=entry1)


def addStudent():
    x1 = entry1.get()
    createStudent(x1)

def recognizeStudents():
    rec()


button1 = tk.Button(text='Add new Student', command=addStudent, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

button2 = tk.Button(text='Recognize Students', command=recognizeStudents, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 200, window=button2)

panel.mainloop()
from tkinter import *
import backend

def get_selected_row(event):
    try:
        global selected_row
        index = list.curselection()
        selected_row = list.get(index[0])
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
        e5.delete(0,END)
        e5.insert(END,selected_row[5])
        e6.delete(0,END)
        e6.insert(END,selected_row[6])
    except IndexError:
        pass
  

def delete_command():
    try:
        backend.delete(selected_row[0])
    except:
        pass    

def view_command():
    list.delete(0,END)
    for row in backend.view():
        list.insert(END,row)

def search_command():
    list.delete(0,END)
    for row in backend.search(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()):
        list.insert(END,row)

def add_command():
    backend.insert(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get())

    list.delete(0,END)
    list.insert(END,(date_text.get(),earning_text.get(),exercise_text.get(),study_text.get(),diet_text.get(),python_text.get()))

def clear_command():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')

win = Tk()
win.configure(bg='blue')
win.wm_title('MY ROUTINE DATABASE')

l1 = Label(win, text='Date', bg = 'blue')
l1.grid(row=0,column=0)
l2 = Label(win, text='Earnings', bg='blue')
l2.grid(row=0,column=2)
l3 = Label(win, text='Exercise', bg = 'blue')
l3.grid(row=1,column=0)
l4 = Label(win, text='Study', bg='blue')
l4.grid(row=1,column=2)
l5 = Label(win, text='Diet', bg='blue')
l5.grid(row=2,column=0)
l6 = Label(win, text='Python', bg='blue')
l6.grid(row=2,column=2)

date_text = StringVar()
e1 = Entry(win, textvariable=date_text)
e1.grid(row=0,column=1)

earning_text = StringVar()
e2 = Entry(win, textvariable=earning_text)
e2.grid(row=0,column=3)

exercise_text = StringVar()
e3 = Entry(win, textvariable=exercise_text)
e3.grid(row=1,column=1)

study_text = StringVar()
e4 = Entry(win, textvariable=study_text)
e4.grid(row=1,column=3)

diet_text = StringVar()
e5 = Entry(win, textvariable=diet_text)
e5.grid(row=2,column=1)

python_text = StringVar()
e6 = Entry(win, textvariable=python_text)
e6.grid(row=2,column=3)

list = Listbox(win,height=13,width=45,bg='sky blue')
list.grid(row=3,column=0,rowspan=13,columnspan=3)

#Scroll bar
# sb = Scrollbar(win)
# sb.grid(row=3,column=2,rowspan=9)

list.bind('<<ListboxSelect>>',get_selected_row)

b1 = Button(win,bg='red',text='ADD',width=17,pady=5,command=add_command)
b1.grid(row=3,column=3)

b2 = Button(win,bg='blue',text='Search',width=17,pady=5,command=search_command)
b2.grid(row=4,column=3)

b3 = Button(win, bg='red', text='Delete date',
            width=17, pady=5, command=delete_command)
b3.grid(row=5,column=3)

b4 = Button(win, bg='blue', text='View all',
            width=17, pady=5, command=view_command)
b4.grid(row=6,column=3)

b5 = Button(win, bg='sky blue',text='Close',
            width=17,pady=5,command = win.destroy)
b5.grid(row=8,column=3)

clear = Button(win, text="Clear", width=17, pady=5,
               bg='red', command=clear_command)
clear.grid(row=7, column=3)

win.mainloop()

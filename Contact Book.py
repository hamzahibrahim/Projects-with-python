from tkinter import *
import sqlite3
#===========================
def connect():
    conn = sqlite3.connect('Contact_Book.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Contact_Book (Id INTEGER PRIMARY KEY ,name text, phone_number text , address text , email_address text)")
    conn.commit()
    conn.close()
#===========================
def insert(name , phone_number , address , email_address ):
    conn = sqlite3.connect('Contact_Book.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO Contact_Book VALUES (NULL , ?,?,?,?)" , (name , phone_number , address , email_address))
    conn.commit()
    conn.close()
#===========================
def view():
    conn = sqlite3.connect('Contact_Book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Contact_Book")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows
#===========================
def delete(id):
    conn = sqlite3.connect('Contact_Book.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM Contact_Book WHERE id=? ", (id,))
    conn.commit()
    conn.close()
#===========================
def search(name='' , phone_number='' , address='' , email_address=''):
    conn = sqlite3.connect('Contact_Book.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Contact_Book WHERE name=?  OR phone_number=? OR address=? OR email_address=? " , (name , phone_number , address , email_address))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

connect()
#===========================
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
    except IndexError:
        pass

#===========================
def delete_command():
    try:
        delete(selected_row[0])
    except:
        pass    
#===========================
def view_all_command():
    list.delete(0,END)
    for row in view():
        list.insert(END,row)
#===========================
def search_command():
    list.delete(0, END)
    for row in search(Name_text.get(), Phone_Number_text.get(), Address_text.get(), Email_Address_text.get()):
        list.insert(END, row)
#===========================
def add_command():
    insert(Name_text.get(), Phone_Number_text.get(),
           Address_text.get(), Email_Address_text.get())
    #to delete after adding (delete from the entry box)
    list.delete(0,END)
    list.insert(END,(Name_text.get(), Phone_Number_text.get(), Address_text.get(), Email_Address_text.get()))
#===========================
def clear_command():
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
#===========================
win = Tk()
win.configure(bg='blue')
#===========================
win.wm_title('MY Contact Book')
#===========================
l1 = Label(win, width=14 ,text='Name: ', bg = 'blue')
l1.grid(row=0,column=0)
l2 = Label(win, width=14,text='Phone Number: ', bg = 'blue')
l2.grid(row=1,column=0)
l3 = Label(win, width=14 ,text='Address: ', bg = 'blue')
l3.grid(row=2,column=0)
l4 = Label(win, width=14, text='Email Address: ', bg = 'blue')
l4.grid(row=3,column=0)

#===========================
Name_text = StringVar()
e1 = Entry(win, width=37 ,textvariable=Name_text)
e1.grid(row=0, column=1)

Phone_Number_text = StringVar()
e2 = Entry(win, width=37  ,textvariable=Phone_Number_text)
e2.grid(row=1, column=1)

Address_text = StringVar()
e3 = Entry(win, width=37 ,textvariable=Address_text)
e3.grid(row=2, column=1)

Email_Address_text = StringVar()
e4 = Entry(win, width=37 ,textvariable=Email_Address_text)
e4.grid(row=3, column=1)
#===========================
t1 = Label(win, text='', bg='sky blue',width=14)
t1.grid(column=3, row=0)
t1 = Label(win, text='Enjoy', bg='sky blue', width=14)
t1.grid(column=3, row=1)
t1 = Label(win, text='-_-', bg='sky blue',width=14)
t1.grid(column=3, row=2)
t1 = Label(win, text='', bg='sky blue',width=14)
t1.grid(column=3, row=3)
#===========================
list = Listbox(win, height=13, width=55)
list.grid(row=4, column=0, rowspan=13, columnspan=3)

#sb = Scrollbar(win)
#sb.grid(row=4, column=3, rowspan=12)

list.bind('<<ListboxSelect>>',get_selected_row)
#===========================
b1 = Button(win, text='ADD', width=14, pady=5, bg = 'red',command=add_command)
b1.grid(row=5, column=3)

b2 = Button(win, text='Search', width=14, pady=5, bg = 'blue', command=search_command)
b2.grid(row=6, column=3)

b3 = Button(win, text='Delete Contact', width=14, bg = 'red', pady=5, command=delete_command)
b3.grid(row=7, column=3)

b4 = Button(win, text='View all', width=14, pady=5, bg = 'blue', command=view_all_command)
b4.grid(row=8, column=3)

b5 = Button(win, text='Close or Exit', width=14,
            pady=7, bg='sky blue', command=win.destroy)
b5.grid(row=10, column=3)

clear = Button(win, text="Clear", width=14, pady=5, bg = 'red', command=clear_command)
clear.grid(row=9, column=3)
#===========================
win.mainloop()

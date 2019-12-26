from tkinter import *
from sqlite3 import *
#from tkinter import messagebox
from tkinter.messagebox import *
conn = connect('aditya')
cur = conn.cursor()

def insert(roll,name,mail):
    rolln = roll.get()
    namen = name.get()
    emailn = mail.get()
    if(rolln!='' and namen!='' and emailn!=''):
        t1.delete(0,END)
        t2.delete(0,END)
        t3.delete(0,END)
        create = 'create table if not exists aec (rollno varchar(20) , name varchar(100) , email varchar(20))'
        cur.execute(create)
        conn.commit()
        sel = "select * from aec where rollno=?"
        values =[rolln,]
        cur.execute(sel,values)
        data1 = cur.fetchall()
        if(len(data1)==0):
            insert='insert into aec (rollno,name,email)values(?,?,?)'
            values = [rolln,namen,emailn]
            d = cur.execute(insert,values)
            conn.commit()
            if d:
                #messagebox.showinfo('Notice' , 'inserted' )
                showinfo('Notice','inserted')
            else:
                #messagebox.showinfo('Warning' , 'not inserted' )
                showinfo('Warning','not inserted')
        else:
            showinfo('Warning','not inserted because already exists')
            confirm =askokcancel("confirmation","do you want to update it?")
            if confirm:
                update="update aec set name=? , email=? where rollno =?"
                values = [namen, emailn , rolln]
                cur.execute(update,values)
                conn.commit()
                showinfo('info',"data is updated")
                
    else:
        showinfo('Warning','some fields are empty')

def view():
    print("the registrations in DataBase are :")
    select = " select * from aec "
    cur.execute(select)
    data = cur.fetchall()
    for i in data:
        for j in i:
            print(j,end=" " )
        print()

def delete():
    confirm = askokcancel('confirmation' , 'confirm delete?')
    if confirm:
        select = " delete from aec "
        d = cur.execute(select)
        conn.commit()
        if d:
            showinfo('Notice','deleted')
        else:
            showinfo('Warning','not deleted')
root = Tk()
root.title("karthik's project")
root.geometry('600x600')

l1 = Label(root,text = 'enter roll no :')
l1.grid(row = 0 , column = 0)
roll_txt = StringVar()
t1 = Entry(root,textvariable = roll_txt)
t1.grid(row = 1,column = 0)

l2 = Label(root,text = 'enter name:')
l2.grid(row = 2 , column = 0)
name_txt = StringVar()
t2 = Entry(root,textvariable = name_txt)
t2.grid(row = 3,column = 0)

l3 = Label(root,text = 'enter email:')
l3.grid(row = 4  , column = 0)
email_txt = StringVar()
t3 = Entry(root,textvariable = email_txt)
t3.grid(row = 5,column = 0)

b1=Button(root,text = "register" , command = lambda:insert(roll_txt,name_txt,email_txt))
b1.grid(row=6,column = 0,columnspan = 2)

b2=Button(root,text = "view data" , command = view)
b2.grid(row=7,column = 0,columnspan = 2)


b3=Button(root,text = "delete data" , command = delete)
b3.grid(row=8,column = 0,columnspan = 2)


root.mainloop()

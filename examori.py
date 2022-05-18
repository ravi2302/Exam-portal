from ast import Return
import datetime
from typing_extensions import Self
from matplotlib.pyplot import flag
import mysql.connector
from tkinter import *
from tkinter import messagebox
from pandas import Timestamp

from pyparsing import common_html_entity
from setuptools import Command
window = Tk()
window.geometry('1200x1000')
window.title("EXAMINATION PORTAL")
dateti = str(datetime.datetime.now())
thing = []
print(thing)
def pop():
    messagebox.showinfo("LOGIN ID & PASSWORD","YOUR LOGIN ID OR PASSWORD IS WRONG")
def tab1():
    def tab3():
        label1.pack_forget()
        label2.pack_forget()        
        bt.pack_forget()
        bt2.pack_forget()
        label6 = Label(window, text = "WELCOME TO EXAMINATION", font=("arial bold",50))
        label6.pack()

        
    def tab2():
        def tab4():
            def tab5():
                e3=entry3.get()
                
                e5=entry5.get()
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="exam_portal")
                mycursor = mydb.cursor()
                val = [e3,thing[0],e5,dateti]
                print(val)
                mycursor.execute("insert into test_table(test_name,login_no,dept_name,date) values(%s,%s,%s,%s)", val)
                mydb.commit()

                e4=int(entry4.get())
                label5.pack_forget()
                label6.pack_forget()
                entry3.pack_forget()
                label8.pack_forget()
                entry5.pack_forget()
                label7.pack_forget()
                entry4.pack_forget()    
                bt4.pack_forget()
                que_entries= []
                
                def setting():
                    entrylist=[]
                    ent=[]                    
                    for u in que_entries:
                        my_result = u.get("1.0",'end-1c')
                        ent.append(my_result)
                        ent.append(thing[0])
                        tup = tuple(ent)
                        entrylist.append(tup)
                        ent.pop(0)
                        ent.pop(0)
                    print(ent)
                    print(entrylist)
                    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="exam_portal")
                    mycursor = mydb.cursor()
                    mycursor.executemany("insert into que_table (question,login_no) values(%s,%s)",entrylist)
                    mydb.commit()
                    label8 = Label(window, text = "QUESTIONS ARE SET SUCCESSFULLY", font=("arial bold",14))
                    label8.pack()

                for j in range(e4):
                    textbox = Text(window, width=70, height=3, font= ("arial bold",12), borderwidth=5)
                    textbox.pack()
                    que_entries.append(textbox)
                               
                button =Button(window, text= "SET", font= ("arial bold",10), command= setting)
                button.pack()                                      
            label3.pack_forget()
            label4.pack_forget()
            entry1.pack_forget()
            entry2.pack_forget()
            bt3.pack_forget()
            label5 = Label(window, text = "WELCOME TO FRAME QUESTIONS", font=("arial bold",50))
            label5.pack()
            label6 = Label(window, text = "GIVE TEST NAME, FOR EXAMPLE 'TEST1'", font=("arial bold",15))
            label6.pack()
            entry3 = Entry(window,width=25,borderwidth=5)
            entry3.pack()
            label8 = Label(window, text="GIVE THE DEPARTMENT NAME FOR THE EXAMINATION")
            label8.pack()
            entry5= Entry(window,width=25,borderwidth=5)
            entry5.pack()
            label7 = Label(window, text= "HOW MANY QUESTIONS DO YOU WANT TO HAVE?")
            label7.pack()
            entry4=Entry(window,width=25,borderwidth=5)
            entry4.pack()
            entry4.insert(0,"NO OF QUESTIONS: ")
            bt4 =Button(window, text = "SELECT", font= ("arial bold",25), command= tab5)
            bt4.pack()            
        label1.pack_forget()
        label2.pack_forget()
        bt.pack_forget()
        bt2.pack_forget()
        label3 = Label(window, text = "WELCOME TO CONDUCT EXAM", font=("arial bold",50))
        label3.pack()
        label4 = Label(window, text = "LOGIN HERE", font=("arial bold",25))
        label4.pack()
        entry1 = Entry(window, width=25,borderwidth=5)
        entry1.pack()
        entry1.insert(0,"LOGIN ID: ")
        entry2 = Entry(window, width=25,borderwidth=5)
        entry2.pack()
        entry2.insert(0,"PASSWORD: ")
        def search():
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="exam_portal")
            mycursor = mydb.cursor()
            mycursor.execute("select * from login_table")
            result = mycursor.fetchall()
            print(result)
            flag = 0
            
            for i in result:
                if i[1] == entry1.get() and i[2] == entry2.get():
                    thing.append(i[0])
                    tab4()                    
                else:
                    flag = flag + 1
            if flag == len(result):
                pop()
        bt3 = Button(window, text = "LOGIN", font= ("arial bold",25), command= search)
        bt3.pack()

    label1 = Label(window, text = "WELCOME TO THE EXAM PORTAL", font = ("arial bold",50))
    label1.pack()
    label2 =Label(window, text = "TO CONDUCT EXAM SELECT 'FRAME EXAM' OR IF CAME TO TAKE EXAM SELECT 'TAKE EXAM'", font= ("arial bold",25))
    label2.pack()
    bt= Button(window, text = "FRAME EXAM", font= ("arial bold",25), command= tab2)
    bt.pack()
    bt2= Button(window,text = "TAKE EXAM", font= ("arial bold",25), command = tab3)
    bt2.pack()


tab1()

window.mainloop()

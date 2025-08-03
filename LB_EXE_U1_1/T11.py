import tkinter as tk
import mysql.connector

root = tk.Tk()

root.title("Show Form")
root.geometry("450x300")

l_1 = tk.Label(root,text="Registration Form")
l_1.grid(row=0,column=2)

l_2 = tk.Label(root,text="Full Name")
l_2.grid(row=1,column=0)

ent_1 = tk.Entry(root)
ent_1.grid(row=1,column=1)

l_3 = tk.Label(root,text="Email")
l_3.grid(row=2,column=0)

ent_2 = tk.Entry(root)
ent_2.grid(row=2,column=1)

l_4 = tk.Label(root,text="Gender")
l_4.grid(row=3,column=0)

gen = ["Male","Female"]

gen = tk.StringVar()
tk.Radiobutton(root,text="Male",value="Male",variable=gen).grid(row=3,column=1)
tk.Radiobutton(root,text="Female",value="Female",variable=gen).grid(row=3,column=2)

l_5 = tk.Label(root,text="Age")
l_5.grid(row=4,column=0)

ent_3 = tk.Entry(root)
ent_3.grid(row=4,column=1)

def ins():
	print("Hi")
	name = ent_1.get()
	email = ent_2.get()
	gender = gen.get()
	a = ent_3.get()
	age = int(a)

	# print("---------Details---------")
	# print("Name: ",name)
	# print("Email: ",email)
	# print("Gender: ",gender)
	# print("Age: ",age)

	conn = mysql.connector.connect(host="localhost",user="php",password="php",database="php_db")

	cursor = conn.cursor()

	cursor.execute("INSERT INTO users VALUES (%s,%s,%s,%s)",(name,email,gender,age))
	conn.commit()
	print("Data Inserted in users table.")

btn_ins = tk.Button(root,text="Submit",fg="white",bg="red",command=ins).grid(row=5,column=1)

root.mainloop()
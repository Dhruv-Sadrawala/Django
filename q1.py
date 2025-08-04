import tkinter as tk

root = tk.Tk()

root.title("List Entry")
root.geometry("450x300")

#create list

list1 = []

e1 = tk.Entry(root)
e1.grid(rows=1,column=0)

listb = tk.Listbox(root)
listb.grid(rows=2,column=0)
 
def create():
	name = e1.get()

	if name:
		list1.append(name)

	listb.insert(tk.END,name)

	e1.delete(0,tk.END)

btn = tk.Button(root,text="Submit",command=create)
btn.grid(rows=3,column=0)

print(list1)
root.mainloop()
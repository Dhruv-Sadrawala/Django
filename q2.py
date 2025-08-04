import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.title("List Update")
root.geometry("450x300")

#update list 

list1 = ["ABC","GHJ","JKL","TYY","LOP"]

e1 = tk.Entry(root)
e1.grid(rows=1,column=0)

listb = tk.Listbox(root)
listb.grid(rows=2,column=0)
 
def update():
	selected = listb.curselection()
	new_name = e1.get().strip()

	if selected and new_name:
		index = selected[0]
		list1[index] = new_name
		listb.delete(index)
		listb.insert(index,new_name)
		e1.delete(0,tk.END)
	else:
		messagebox.showwarning("Update","Select a name and enter a new value.")

for name in list1:
	listb.insert(tk.END,name)

btn = tk.Button(root,text="Update",command=update)
btn.grid(rows=3,column=0)

print(list1)
root.mainloop()
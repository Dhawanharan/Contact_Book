#importing modules
from tkinter import *
from tkinter import messagebox

#initializing the window
root = Tk()
root.geometry('700x550')
root.config(bg ='#f9fbfc')
root.title('Contact Book')
root.resizable(0,0)

# sample contact list
contactlist = [
    ['Kumar','9477446582'],
    ['Ram','9478459827'],
    ['Shyam','9478459827']
]
Name = StringVar()
Number = StringVar()

# Right side contact list frame 
frame = Frame(root, bg="#f9fbfc")
frame.pack(side = RIGHT, padx=20, pady=20, fill=Y)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(
    frame,
    yscrollcommand=scroll.set,
    font=('Segoe UI', 14),
    bg = '#ffffff',
    width=22,
    height=18,
    borderwidth=2,
    relief="groove",
    selectbackground="#8ecae6",
    selectforeground="black"
)
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

# Functions
def selected():
    if len(select.curselection())==0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])

def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill the information")

def EntryReset():
    Name.set('')
    Number.set('')

def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Successfully Updated Contact")
        EntryReset()
        Select_set()
    elif not(Name.get()) and not (Number.get()) and not(len(select.curselection())==0):
        messagebox.showerror("Error", "Please fill the information")
    else:
        if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and press Load button")
        else:
            message1 = "To load the selected contact, press VIEW first."
            messagebox.showerror("Error", message1)

def Delete_Entry():
    if len(select.curselection())!=0:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result==True:
            del contactlist[selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select a Contact')

def VIEW():
    NAME, PHONE = contactlist[selected()]
    Name.set(NAME)
    Number.set(PHONE)
    
def EXIT():
    root.destroy()
    
def Select_set():
    contactlist.sort()
    select.delete(0,END)
    for name, phone in contactlist:
        select.insert(END,name)
Select_set()

# Left side form & controls 
Label(root, text = 'Name', font=("Segoe UI", 16, "bold"), bg = '#f9fbfc').place(x= 40, y=40)
Entry(root, textvariable = Name, font=("Segoe UI", 13), width=25, bd=2, relief="solid").place(x= 180, y=42)

Label(root, text = 'Contact No.', font=("Segoe UI", 16, "bold"), bg = '#f9fbfc').place(x= 40, y=90)
Entry(root, textvariable = Number, font=("Segoe UI", 13), width=25, bd=2, relief="solid").place(x= 180, y=92)

# Button style
btn_style = {"font": ("Segoe UI", 13, "bold"), "width":12, "height":1, "bd":0, "relief":"ridge"}

Button(root, text="ADD", bg='#90e0ef', fg="black", command=AddContact, **btn_style).place(x= 60, y=160)
Button(root, text="EDIT", bg='#ffd166', fg="black", command=UpdateDetail, **btn_style).place(x= 220, y=160)
Button(root, text="DELETE", bg='#ef476f', fg="white", command=Delete_Entry, **btn_style).place(x= 60, y=220)
Button(root, text="VIEW", bg='#06d6a0', fg="black", command=VIEW, **btn_style).place(x= 220, y=220)
Button(root, text="RESET", bg='#adb5bd', fg="black", command=EntryReset, **btn_style).place(x= 60, y=280)
Button(root, text="EXIT", bg='#e63946', fg="white", command=EXIT, **btn_style).place(x= 220, y=280)

root.mainloop()

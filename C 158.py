from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
root=Tk()
root.title("My Credit Card")
root.geometry("4000x4000")
root.configure(background="Black")
img=ImageTk.PhotoImage(Image.open("card2.png"))
input_1=Entry(root)
input_1.place(relx=0.5,rely=0.2,anchor=CENTER)
label_1=Label(root,image=img)
label_1.place(relx=0.5,rely=0.7,anchor=CENTER)
def enterpassword():
    try:
        input_value=int(input_1.get())
        messagebox.showinfo("Alert","Credit Card Accepted")
    except:
        messagebox.showinfo("Alert","Wrong Password ")
button_1=Button(root,text="Check Credit Card",command=enterpassword)
button_1.place(relx=0.5,rely=0.3,anchor=CENTER)
root.mainloop()
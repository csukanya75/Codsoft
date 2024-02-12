from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string, random

root = Tk()
root.geometry("500x500")
root.title("Password Generator")
root.config(bg="brown1")
root.resizable(False, False)

def password_generation():
    try:
        length_password = solidboss.get()
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        generated_password = "".join(all_list[0:length_password])
        password.set(generated_password)
        
        # Example of how to use username (you can modify this part as needed)
        username = username_entry.get()
        print("Username:", username)
        
    except:
        messagebox.askretrycancel("A problem has occurred! Please Try Again...")

Title = Label(root, text="Password Generator",bg="brown1", fg="white", font=("futura", 15, "bold"))
Title.pack(anchor="center", pady="20px")

length = Label(root, text="Select the Length of Your Password :- ", fg="white", bg="brown1", font=("ubuntu", 12))
length.place(x="20px", y="70px")

def onent(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def onlev(e):
    generate_btn['bg'] = "orange"
    generate_btn['fg'] = "black"   

solidboss = IntVar()
Selector = Combobox(root, textvariable=solidboss, state="readonly")
Selector['values'] = tuple(range(1, 31))  # Specify values directly
Selector.current(0)
Selector.place(x="240px", y="72px")

username_label = Label(root, text="Enter your username:", bg="brown1", fg="white", font=("ubuntu", 12))
username_label.place(x="20px", y="110px")

username_entry = Entry(root)
username_entry.place(x="200px", y="112px")

generate_btn = Button(root, text="Generate Your Password", bg="darkorange1", fg="black", font=("ubuntu", 12), cursor="hand2", command=password_generation)
generate_btn.bind("<Enter>", onent)
generate_btn.bind("<Leave>", onlev)
generate_btn.pack(anchor="center", pady="70px")

result_lable = Label(root, text="Your Generated Password is :- ", bg="brown1", fg="white", font=("ubuntu", 12))
result_lable.place(x="20px", y="160px")

password = StringVar()
pass_final = Entry(root, textvariable= password, state="readonly", fg="black", font=("ubuntu", 15))
pass_final.place(x="200px", y="160px")

root.mainloop()


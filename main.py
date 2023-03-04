import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 9
    password_max = 13
    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


textcolour ="#92C3BF"
colour = "#000000"
textfont = "MonumentExtended-Regular"

window = Tk()
window.title("Password Generator")
window.geometry("1080x720")
window.minsize(480, 360)
window.config(background=colour)

frame = Frame(window, bg=colour)

right_frame = Frame(frame, bg=colour)

label_title = Label(right_frame, text="PASSWORD:", font=(textfont, 25), bg=colour, fg="white")
label_title.pack()

password_entry = Entry(right_frame, font=(textfont, 25), bg=colour, fg="#92C3BF", relief= FLAT)
password_entry.pack()

generate_password_button = Button(right_frame, text="GENERATE PASSWORD", font=(textfont, 25), bg="#92C3BF", fg=colour, command=generate_password, activebackground="#92C3BF", relief=FLAT, cursor="tcross", borderwidth=0, highlightthickness=20)
generate_password_button.pack(fill=X)

leave_button = Button(right_frame, text="LEAVE", font=(textfont, 25), bg=colour, fg="#343434", command=window.quit, activebackground=colour, relief=FLAT, cursor="tcross", borderwidth=0, activeforeground="#92C3BF")
leave_button.pack()


right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)


window.mainloop()

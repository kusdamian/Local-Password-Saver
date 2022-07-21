from tkinter import *


# ----------------------------------- UI --------------------------------------- #
BLUE = '#DFF4FA'
FONT_NAME = "Courier"

# Main Window
root = Tk()
root.title('Password Saver')
root.config(padx=50, pady=50, bg=BLUE)

# logo
canvas = Canvas(width=200, height=190, bg=BLUE, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 95, image=logo)
canvas.grid(column=1, row=1, columnspan=2)

# login fields
name_text = Label(text='Username:', bg=BLUE, font=(FONT_NAME, 12))
name_text.grid(column=1, row=2)

name_entry = Entry()
name_entry.grid(column=2, row=2)

password_text = Label(text='Password:', bg=BLUE, font=(FONT_NAME, 12))
password_text.grid(column=1, row=3)

password_entry = Entry()
password_entry.grid(column=2, row=3)

log_button = Button(text='Login', highlightthickness=0)
log_button.grid(column=2, row=4)

blankspace1 = Label(text='', bg=BLUE, font=(FONT_NAME, 12))
blankspace1.grid(column=1, row=5)

# create account
create_acc_text = Label(text='Dont have an account?', bg=BLUE, font=(FONT_NAME, 8))
create_acc_text.grid(column=1, row=6)

create_acc_button = Button(text='Click Here', highlightthickness=0, font=(FONT_NAME, 8))
create_acc_button.grid(column=2, row=6)

if __name__ == '__main__':
    root.mainloop()

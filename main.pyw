"""
The main file of a local password saver app in which all the GUI elements are found.
"""

from tkinter import *
from buttons_aux import Butts


def create_acc_button():
    login_screen.pack_forget()
    create_screen.pack()


def return_button():
    create_screen.pack_forget()
    login_screen.pack()


# ----------------------------------- GUI --------------------------------------- #
BLUE = '#DFF4FA'
FONT_NAME = "Courier"


# Main Window
root = Tk()
root.title('Password Saver')
root.resizable(False, False)

# Frames setup
login_screen = Frame(root, padx=50, pady=50, bg=BLUE)
create_screen = Frame(root, padx=50, pady=50, bg=BLUE)
main_screen = Frame(root, padx=50, pady=50, bg=BLUE)


# =============== login Screen =================== #
# logo
canvas_ls = Canvas(login_screen, width=200, height=190, bg=BLUE, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas_ls.create_image(100, 95, image=logo)
canvas_ls.grid(column=1, row=1, columnspan=2)

# login fields
title_ls = Label(login_screen, text='Login', bg=BLUE, font=(FONT_NAME, 15, 'bold'))
title_ls.grid(column=1, row=2, columnspan=2)

name_text_ls = Label(login_screen, text='Username:', bg=BLUE, font=(FONT_NAME, 12))
name_text_ls.grid(column=1, row=3)

name_entry_ls = Entry(login_screen)
name_entry_ls.grid(column=2, row=3)

password_text_ls = Label(login_screen, text='Password:', bg=BLUE, font=(FONT_NAME, 12))
password_text_ls.grid(column=1, row=4)

password_entry_ls = Entry(login_screen)
password_entry_ls.grid(column=2, row=4)

log_button_ls = Button(login_screen, text='Login', highlightthickness=0)
log_button_ls.grid(column=2, row=5)

blankspace1_ls = Label(login_screen, text='', bg=BLUE, font=(FONT_NAME, 12))
blankspace1_ls.grid(column=1, row=6)

# create account
create_acc_text_ls = Label(login_screen, text='Dont have an account?', bg=BLUE, font=(FONT_NAME, 8))
create_acc_text_ls.grid(column=1, row=7)

create_acc_button_ls = Button(login_screen, text='Click Here', highlightthickness=0, font=(FONT_NAME, 8), command=create_acc_button)
create_acc_button_ls.grid(column=2, row=7)


# =============== Create Screen =================== #
# logo
canvas_cs = Canvas(create_screen, width=200, height=190, bg=BLUE, highlightthickness=0)
canvas_cs.create_image(100, 95, image=logo)
canvas_cs.grid(column=1, row=1, columnspan=2)

# create login fields
title_cs = Label(create_screen, text='Account Creation', bg=BLUE, font=(FONT_NAME, 15, 'bold'))
title_cs.grid(column=1, row=2, columnspan=2)

name_text_cs = Label(create_screen, text='Username:', bg=BLUE, font=(FONT_NAME, 12))
name_text_cs.grid(column=1, row=3)

name_entry_cs = Entry(create_screen)
name_entry_cs.grid(column=2, row=3)

password_text_cs = Label(create_screen, text='Password:', bg=BLUE, font=(FONT_NAME, 12))
password_text_cs.grid(column=1, row=4)

password_entry_cs = Entry(create_screen)
password_entry_cs.grid(column=2, row=4)

password_text_confirm_cs = Label(create_screen, text='Confirm Pass:', bg=BLUE, font=(FONT_NAME, 12))
password_text_confirm_cs.grid(column=1, row=5)

password_entry_confirm_cs = Entry(create_screen)
password_entry_confirm_cs.grid(column=2, row=5)

# Blank Space
blankspace1_cs = Label(create_screen, text='', bg=BLUE, font=(FONT_NAME, 12))
blankspace1_cs.grid(column=1, row=6)

# Buttons
back_button = Button(create_screen, text='Return', highlightthickness=0, font=(FONT_NAME, 8), command=return_button)
back_button.grid(column=1, row=7)

create_acc_button = Button(create_screen, text='Create Account', highlightthickness=0, font=(FONT_NAME, 8))
create_acc_button.grid(column=2, row=7)


# =============== Main Screen =================== #






# initialize first screen
login_screen.pack()

if __name__ == '__main__':
    root.mainloop()

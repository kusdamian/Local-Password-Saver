"""
The main file of a local password saver app in which all the GUI elements are found.
"""

import buttons_aux as ba
from frame import *


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

log_button_ls = Button(login_screen, text='Login', highlightthickness=0, command=ba.login_button)
log_button_ls.grid(column=2, row=5)

blankspace1_ls = Label(login_screen, text='', bg=BLUE, font=(FONT_NAME, 12))
blankspace1_ls.grid(column=1, row=6)

# create account
create_acc_text_ls = Label(login_screen, text='Dont have an account?', bg=BLUE, font=(FONT_NAME, 8))
create_acc_text_ls.grid(column=1, row=7)

create_acc_button_ls = Button(login_screen, text='Click Here', highlightthickness=0, font=(FONT_NAME, 8), command=ba.create_acc_button)
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
back_button = Button(create_screen, text='Return', highlightthickness=0, font=(FONT_NAME, 8), command=ba.return_button)
back_button.grid(column=1, row=7)

create_acc_button = Button(create_screen, text='Create Account', highlightthickness=0, font=(FONT_NAME, 8))
create_acc_button.grid(column=2, row=7)


# =============== Main Screen =================== #
# logo
canvas_ms = Canvas(main_screen, width=200, height=190, bg=BLUE, highlightthickness=0)
canvas_ms.create_image(100, 95, image=logo)
canvas_ms.grid(column=2, row=1)

title_ms = Label(main_screen, text='Hello {Name Here}', bg=BLUE, font=(FONT_NAME, 15, 'bold'))
title_ms.grid(column=2, row=2)

logout_button_ms = Button(main_screen, text='Logout', highlightthickness=0, font=(FONT_NAME, 8), command=ba.logout_button)
logout_button_ms.grid(column=3, row=1, sticky='nw')


# Search Section
search_text_ms = Label(main_screen, text='Search Password:', bg=BLUE, font=(FONT_NAME, 12))
search_text_ms.grid(column=1, row=3)

search_entry_ms = Entry(main_screen, width=25)                     # THIS NEEDS TO BE A DROP DOWN IN THE FUTURE
search_entry_ms.grid(column=2, row=3, columnspan=2)

search_button_ms = Button(main_screen, text='Search')
search_button_ms.grid(column=3, row=3)

blankspace1_ms = Label(main_screen, text='', bg=BLUE, font=(FONT_NAME, 12))
blankspace1_ms.grid(column=1, row=4, rowspan=2)

# New Password fields
title2_ms = Label(main_screen, text='New Password:', bg=BLUE, font=(FONT_NAME, 15, 'bold'))
title2_ms.grid(column=2, row=6)

website_text_ms = Label(main_screen, text='Website:', bg=BLUE, font=(FONT_NAME, 12))
website_text_ms.grid(column=1, row=7)

website_entry_ms = Entry(main_screen)
website_entry_ms.grid(column=2, row=7, columnspan=2)

email_text_ms = Label(main_screen, text='Email:', bg=BLUE, font=(FONT_NAME, 12))
email_text_ms.grid(column=1, row=8)

website_entry_ms = Entry(main_screen)
website_entry_ms.grid(column=2, row=8, columnspan=2)

name_text_ms = Label(main_screen, text='Username:', bg=BLUE, font=(FONT_NAME, 12))
name_text_ms.grid(column=1, row=9)

name_entry_ms = Entry(main_screen)
name_entry_ms.grid(column=2, row=9, columnspan=2)

phone_text_ms = Label(main_screen, text='Phone Number:', bg=BLUE, font=(FONT_NAME, 12))
phone_text_ms.grid(column=1, row=10)

phone_entry_ms = Entry(main_screen)
phone_entry_ms.grid(column=2, row=10, columnspan=2)

password_text_ms = Label(main_screen, text='Password:', bg=BLUE, font=(FONT_NAME, 12))
password_text_ms.grid(column=1, row=11)

password_entry_ms = Entry(main_screen)
password_entry_ms.grid(column=2, row=11)

password_gen_button_ms = Button(main_screen, text='Random Pass')
password_gen_button_ms.grid(column=3, row=11)

save_button_ms = Button(main_screen, text='Save Password', highlightthickness=0, font=(FONT_NAME, 8))
save_button_ms.grid(column=2, row=12)

# initialize first screen
login_screen.pack()

if __name__ == '__main__':
    root.mainloop()

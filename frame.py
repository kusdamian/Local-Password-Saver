from tkinter import *

BLUE = '#DFF4FA'
FONT_NAME = "Courier"

user = None

# Main Window
root = Tk()
root.title('Password Saver')
root.resizable(False, False)

# Frames setup
login_screen = Frame(root, padx=25, pady=25, bg=BLUE)
create_screen = Frame(root, padx=25, pady=25, bg=BLUE)
main_screen = Frame(root, padx=25, pady=25, bg=BLUE)

# ALL UI vars that will be referenced or manipulated in some way
# =========================== login Screen ============================= #
name_entry_ls = Entry(login_screen)

password_entry_ls = Entry(login_screen)


# =========================== Create Screen ============================= #
name_entry_cs = Entry(create_screen)

password_entry_cs = Entry(create_screen)

password_entry_confirm_cs = Entry(create_screen)


# =========================== Main Screen =============================== #
title_ms = Label(main_screen, bg=BLUE, font=(FONT_NAME, 15, 'bold'))

search_entry_ms = Entry(main_screen, width=25)                     # THIS NEEDS TO BE A DROP DOWN IN THE FUTURE

website_entry_ms = Entry(main_screen, width=40)

email_entry_ms = Entry(main_screen, width=40)

name_entry_ms = Entry(main_screen, width=40)

phone_entry_ms = Entry(main_screen, width=40)

password_entry_ms = Entry(main_screen, width=27)

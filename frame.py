from tkinter import *

BLUE = '#DFF4FA'
FONT_NAME = "Courier"

# User Var for current open user file
user = None

# Main Window
root = Tk()
root.title('Password Saver')
root.resizable(False, False)

# Frames setup
login_screen = Frame(root, padx=25, pady=25, bg=BLUE)
create_screen = Frame(root, padx=25, pady=25, bg=BLUE)
main_screen = Frame(root, padx=25, pady=25, bg=BLUE)

# Entry Variables
# =========================== login Screen ============================= #
name_entry_ls = Entry(login_screen)

password_entry_ls = Entry(login_screen)


# =========================== Create Screen ============================= #
name_entry_cs = Entry(create_screen)

password_entry_cs = Entry(create_screen)

password_entry_confirm_cs = Entry(create_screen)


# =========================== Main Screen =============================== #
search_entry_ms = Entry(main_screen, width=25)                     # THIS NEEDS TO BE A DROP DOWN IN THE FUTURE

website_entry_ms = Entry(main_screen)

email_entry_ms = Entry(main_screen)

name_entry_ms = Entry(main_screen)

phone_entry_ms = Entry(main_screen)

password_entry_ms = Entry(main_screen)

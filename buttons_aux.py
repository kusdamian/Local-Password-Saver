"""
An auxiliary file containing everything the GUI buttons need to function
"""

import frame


def create_acc_button():
    frame.login_screen.pack_forget()
    frame.create_screen.pack()


def return_button():
    frame.create_screen.pack_forget()
    frame.login_screen.pack()


def login_button():
    frame.login_screen.pack_forget()
    frame.main_screen.pack()


def logout_button():
    frame.main_screen.pack_forget()
    frame.login_screen.pack()

"""
An auxiliary file containing everything the GUI buttons need to function
"""

import frame
from pathlib import Path
import os


# ========================== Button Help ================================ #
def search_folder(filename):
    for root, dirs, files in os.walk('Users'):
        for Files in files:
            try:
                found = Files.find(filename)
                if found != -1:
                    return True
            except:
                print('Error happened')
                exit()


# ============================ Buttons ================================== #
def create_acc_button_click_here():
    frame.login_screen.pack_forget()
    frame.create_screen.pack()


# Button that will create account
# this needs to check if two fields are equal and make sure the username hasn't been used before
# this also needs to create a new file assuming all requirements are met with the title as the username
# and the password as the first line
def create_account_button():
    if not frame.name_entry_cs.get().isspace() and len(frame.name_entry_cs.get()) > 0:
        if not frame.password_entry_cs.get().isspace() and len(frame.password_entry_cs.get()) > 0:
            if frame.password_entry_cs.get() == frame.password_entry_confirm_cs.get():
                try:
                    user_create = open(f'Users/{frame.name_entry_cs.get()}.txt', 'x')
                    user_create.write(f'{frame.password_entry_cs.get()}')
                    user_create.write(' \n')
                    user_create.close()
                    return_button()
                except FileExistsError:
                    print('file already exists')           # Print Statements need to be Pop up windows
                except:
                    print('Something else went wrong')
            else:
                print('Password confirm does not match password')
        else:
            print('Password Empty')
    else:
        print('Username Empty')


def return_button():
    frame.create_screen.pack_forget()
    frame.login_screen.pack()


def login_button():
    if search_folder(f'{frame.name_entry_ls.get()}.txt') and len(frame.name_entry_ls.get()) > 0:
        print('File Found')
        frame.user = f'Users/{frame.name_entry_ls.get()}.txt'
        user_defined = open(frame.user, 'r')
        password_temp = user_defined.readlines()
        password = password_temp[0].split()
        if frame.password_entry_ls.get() == password[0]:
            frame.login_screen.pack_forget()
            frame.main_screen.pack()
            frame.title_ms.config(text=f'Hello {Path(user_defined.name).stem}')
            user_defined.close()
        else:
            print('Incorrect Password')
            user_defined.close()
    else:
        print('No user found')


def logout_button():
    frame.user = None
    frame.main_screen.pack_forget()
    frame.login_screen.pack()


def save_password_button():
    if not frame.website_entry_ms.get().isspace() and len(frame.website_entry_ms.get()) > 0:
        if not frame.password_entry_ms.get().isspace() and len(frame.password_entry_ms.get()) > 0:
            if (not frame.email_entry_ms.get().isspace() and len(frame.email_entry_ms.get()) > 0) or \
                    (not frame.name_entry_ms.get().isspace() and len(frame.name_entry_ms.get()) > 0):
                user_defined = open(frame.user, 'a')
                user_defined.write(
                    f'{frame.website_entry_ms.get()}|{frame.email_entry_ms.get()}|{frame.name_entry_ms.get()}|'
                    f'{frame.phone_entry_ms.get()}|{frame.password_entry_ms.get()}|\n'
                )
                print('Password is saved')
                user_defined.close()
            else:
                print('You must enter either an Email or Username (or both).')
        else:
            print('You must enter a password.')
    else:
        print('You must enter a website.')

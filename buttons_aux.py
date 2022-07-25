"""
An auxiliary file containing everything the GUI buttons need to function
"""

import frame
import os


# ========================== Button Help ================================ #
def search_folder(filename):
    for root, dirs, files in os.walk('Users'):
        for Files in files:
            try:
                found = Files.find(filename)
                # print(found)
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
                    user = open(f'Users/{frame.name_entry_cs.get()}.txt', 'x')
                    user.write(f'{frame.password_entry_cs.get()}')
                    user.close()
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
        user = open(f'Users/{frame.name_entry_ls.get()}.txt', 'r')
        password = user.readline()
        if frame.password_entry_ls.get() == password:
            frame.login_screen.pack_forget()
            frame.main_screen.pack()
        else:
            print('Incorrect Password')
    else:
        print('No user found')


# Do not forget to close the open file here with user.close()
def logout_button():
    frame.main_screen.pack_forget()
    frame.login_screen.pack()

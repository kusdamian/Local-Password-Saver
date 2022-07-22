from tkinter import *

BLUE = '#DFF4FA'
FONT_NAME = "Courier"

# Main Window
root = Tk()
root.title('Password Saver')
root.resizable(False, False)

# Frames setup
login_screen = Frame(root, padx=25, pady=25, bg=BLUE)
create_screen = Frame(root, padx=25, pady=25, bg=BLUE)
main_screen = Frame(root, padx=25, pady=25, bg=BLUE)

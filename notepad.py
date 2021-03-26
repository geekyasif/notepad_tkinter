from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)
    if file is None:
        file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Docuemnts", "*.txt")])
        if file == "":
            file = None
        else:
            root.title(os.path.basename(file) + " - Notepad")
            TextArea.delete(1.0, END)
            f = open(file, "r")
            TextArea.insert(1.0,f.read())
            f.close()

def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            # save as new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")

    else:
        # save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad", "Notepad By GeekyAsif")

def feedback():
    s = tmsg.askquestion("feedback" ,"How was your experience with our Notepad application")
    if s == "yes":
        tmsg.showinfo("Feedback", "You can give feedback on my email - mdasif08737@gmail.com")
    else:
        tmsg.showinfo("Feedback", "Sooryy")

def helpus():
    tmsg.showinfo("Help", "Send us an email on mdasif08737@gmail.com to help you.")



if __name__ == '__main__':
    root = Tk()
    root.title("Notepad Basic")
    root.geometry("550x400")
    root.wm_iconbitmap("notepad_logo.ico")


    # creating menu
    menubar = Menu(root, tearoff=False)

    # creating sub menu and commands
    # file menu and submenu
    file = Menu(menubar, tearoff=0)
    file.add_command(label="New", command=newfile, accelerator="Ctrl+N")
    file.add_command(label="New Window", command=None, state=DISABLED, accelerator="Ctrl+Shift+N")
    file.add_command(label="Open... ", command=openFile, accelerator="Ctrl+O")
    file.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
    file.add_command(label="Save as..", command=None, state=DISABLED, accelerator="Ctrl+Shift+S")
    file.add_separator()
    file.add_command(label="Page Setup...", state=DISABLED, command=None)
    file.add_command(label="Print...", command=None, state=DISABLED, accelerator="Ctrl+P")

    file.add_separator()
    file.add_command(label="Exit", command=root.destroy, accelerator="Ctrl+Q")

    menubar.add_cascade(label="File", menu=file)

    # edit menu and submenu
    edit = Menu(menubar, tearoff=0)
    edit.add_command(label="Undo", command=None, state=DISABLED, accelerator="Ctrl+Z")
    edit.add_separator()
    edit.add_command(label="Cut", command=cut, accelerator="Ctrl+X")
    edit.add_command(label="Copy", command=copy, accelerator="Ctrl+C")
    edit.add_command(label="Paste", command=paste, accelerator="Ctrl+V")
    edit.add_command(label="Delete", command=None, accelerator="Del")
    edit.add_separator()
    edit.add_command(label="Search with bing", command=None, state=DISABLED, accelerator="Ctrl+E")
    edit.add_command(label="Fine...", command=None, state=DISABLED, accelerator="Ctrl+F")
    edit.add_command(label="Find Next", command=None, state=DISABLED, accelerator="F3")
    edit.add_command(label="Find Previous", command=None, state=DISABLED, accelerator="Shift+F3")
    edit.add_command(label="Replace...", command=None, state=DISABLED, accelerator="Ctrl+H")
    edit.add_command(label="Go To...", command=None, state=DISABLED, accelerator="Ctrl+G")
    edit.add_separator()
    edit.add_command(label="Select All", command=None, state=DISABLED, accelerator="Ctrl+A")
    edit.add_command(label="Date/Time", command=None, state=DISABLED, accelerator="F5")
    menubar.add_cascade(label="Edit", menu=edit)

    # format menu and submenu
    format = Menu(menubar, tearoff=0)
    format.add_command(label="Word Wrap", command=None, state=DISABLED)
    format.add_command(label="Font...", command=None, state=DISABLED)
    menubar.add_cascade(label="Format", menu=format)

    # view menu and submenu
    view = Menu(menubar, tearoff=0)
    view.add_command(label="Zoom", command=None, state=DISABLED)
    view.add_command(label="Status Bar", command=None, state=DISABLED)
    menubar.add_cascade(label="View", menu=view)

    # help menu and submenu
    help = Menu(menubar, tearoff=False)
    help.add_command(label="View Help", command=helpus)
    help.add_command(label="Send Feedback", command=feedback)
    help.add_separator()
    help.add_command(label="About Notepad", command=about)
    menubar.add_cascade(label="Help", menu=help)


    #adding shorcuts
    menubar.bind_all("<Control-q>", quit)
    root.config(menu=menubar)


    #creating text area
    TextArea = Text(root, font="lucida 10")
    TextArea.pack(expand=True,fill=BOTH)


    #creating scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)


    root.mainloop()

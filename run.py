from tkinter import Tk
from datetime import datetime
from gui import Gui
from app.model import Model

root=Tk()
root.title('Task Tracker')


if __name__=="__main__":
    root.geometry('500x500+100+100')
    gui=Gui(root)
    gui.attach_buttons()
    gui.show_task()
    root.mainloop()
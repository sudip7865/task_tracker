from tkinter import Tk
from datetime import datetime
from gui import Gui
from app.model import Model

root=Tk()
# m=Model()       #it will help to avoide no data.json file error
# data=Model.all_data()
# tasks=lambda tasks=data[str(datetime.today().date())]: [] if tasks=={'1':{}} else tasks

if __name__=="__main__":
    root.geometry('500x500+100+100')
    gui=Gui(root)
    gui.attach_buttons()
    gui.show_task()
    root.mainloop()
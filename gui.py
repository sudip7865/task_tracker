from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
from datetime import datetime
from app import execute_gui_command
from app.model import Model

class Gui:
    def __init__(self, master):
        self.master=master
        self.upper=Frame(master)
        self.lower=Frame(master)
        self.upper.pack(side=TOP, fill=BOTH, expand=True, pady=10)
        self.lower.pack(side=BOTTOM, fill=BOTH, ipady=20)

    def show_task(self):
        #From here 
        m=Model()       #it will help to avoide no data.json file error
        data=Model.all_data()
        try:
            if data[str(datetime.today().date())]=={'1':{}}:
                tasks=[]
            else:
                tasks=data[str(datetime.today().date())]
        except KeyError:
            tasks=[]
        #to here 
        #This above part nessesary for make that function independent
        #Whenever I call it it will refress it's shown value
        def status(x:int):
            if x == 1:
                return 'In progress'
            elif x == 2:
                return  'complete'
            return ''
        #Aboove function return  task status depend on value of task status
        if tasks == []:
            Label(self.upper, text='"No result found"').pack(side=TOP, padx=10)
        else:
            Label(self.upper, text=f'ID \t NAME \t STATUS ', font=('Helvetica', 15)).pack(anchor='w', padx=10)
            for item in tasks:
                # print(f'Item : {item} \n ')
                if tasks[item] != '': 
                    Label(self.upper, text=f'{item} \t {tasks[item]['task']} \t {status(tasks[item]['status'])}').pack(anchor='w', padx=10)
                    

    def attach_buttons(self):
        add=Button(self.lower, text="Add", command=lambda : self.top_level_window('add'))
        update=Button(self.lower, text='Update', command=lambda : self.top_level_window('update'))
        delete=Button(self.lower, text='Delete', command=lambda : self.top_level_window('delete'))
        mark=Button(self.lower, text='Mark', command=lambda : self.top_level_window('mark'))
        for item in [add, update, delete, mark]:
            item.pack(side=LEFT, expand=True)

    def refresh_task_list(self):
        '''It will remove children and attach again'''
        for child in self.upper.winfo_children():
            child.pack_forget()
        #after removing all children attach again
        self.show_task()

    def top_level_window(self, type: str):
        '''This one create a top level window 
        which one will for add, delete and update operation'''
        top_window=Toplevel()
        top_window.geometry('200x150+100+150')
        self.top_window=top_window
        id=Entry(top_window)        #This one will only take integer value
        name=Entry(top_window)
        status=ttk.Combobox(top_window, values=['Pending', 'Progress', 'Completed'], state='readonly')
        lname=Label(top_window, text='Task Name: ')
        lid=Label(top_window, text='Task Id: ')
        lstatus=Label(top_window, text="Task status")
        done=Button(top_window,)
        self.status=status      # it will help to access from other methd(handler)

        if type.lower() == 'add':   #only entry that need for add new task attch
            top_window.title('Add task')    
            lname.pack(anchor='w', padx=10)
            name.pack(anchor='w', padx=10)
            done['text']='Add'
        elif type.lower() == 'update':    #Entries that need for update a task
            lid.pack(anchor='w', padx=10)
            id.pack(anchor='w', padx=10)
            lname.pack(anchor='w', padx=10)
            name.pack(anchor='w', padx=10)
            done['text']='Update'
        elif type.lower() == 'mark':    #with combobox that have 3 values
            # self.status=status      # it will help to access from other methd(handler)
            lid.pack(anchor='w', padx=10)
            id.pack(anchor='w', padx=10)
            lstatus.pack(anchor='w', padx=10)
            status.pack(anchor='w', padx=10)
            id.bind('<KeyRelease>', lambda event: self.handler(id, event))
            done['text']='Mark'
        else: #case where delete
            lid.pack(anchor='w', padx=10)
            id.pack(anchor='w', padx=10)
            done['text']='Delete'
        done['command']= lambda name=name, id=id: self.manage_top_window_data(id, name, cat=done['text'].lower())
        done.pack(side=BOTTOM, pady=10)
    
    def manage_top_window_data(self, id, name, cat):
        '''This function manage data thoes get from top window
        '''
        task_id=id.get()
        task_name=name.get()
        if task_id == '' and task_name == '':
            ans=showinfo(title='Empty', message="We can't proceed with it.")
            return 
        execute_gui_command(task_id, task_name, self.status.get(), cat)
        self.refresh_task_list()
        self.top_window.destroy()

    def handler(self, id, event):
        '''This method will change status value base on task status'''
        task=Model.get_task(id.get())
        if task is None:
            self.status.set('')
            return 
        self.status.current(task['status'])
        

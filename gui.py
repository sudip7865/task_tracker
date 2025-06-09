from tkinter import *
from tkinter import ttk, font
from tkinter.messagebox import showinfo
from datetime import datetime
from app import execute_gui_command
from app.model import Model

class Gui:
    def __init__(self, master):
        self.master=master
        self.upper=Frame(master,)
        self.lower=Frame(master)
        self.upper.pack(side=TOP, fill=BOTH, expand=True, pady=10)
        self.lower.pack(side=BOTTOM, fill=BOTH, ipady=20)
        self.configure_upper()      #make ready upper for appling grid
    
    def configure_upper(self)->None:       #It will configure master for grid layout
        '''This will create configuration for grid
        like how many column and row will take to render data'''
        m = Model()
        #number of columns and rows
        column_num = 3      #There have thre column  ID, Name, Status
        try:
            number_of_tasks = m.number_of_tasks()  #get number of tasks
            if number_of_tasks < 20:
                row_num = 20
            else:
                row_num = number_of_tasks + 1 # 1 for indexes (Id, Name, Status)
        except KeyError as e:
            row_num = 1         #in case when there have no tasks
        # configuring thoes 
        for i in range(0, column_num):
            self.upper.columnconfigure(i, weight = 1)
        #row configure
        for i in range(0, row_num):
            self.upper.rowconfigure(i, weight = 1)
        
    def attach_grid(widget, column, row, sticky, px=0, py=0, ipx=0, ipy=0)->None:
        '''This will apply grid to widget'''
        widget.grid(column, row, sticky=sticky, padx=px, pady=py, ipadx =ipx, ipady=ipy)


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
                return  'Complete'
            return 'Pending'
        #Aboove function return  task status depend on value of task status
        if m.number_of_tasks() == 0:
            no_result_label = ttk.Label(self.upper, text='"No result found"')
            no_result_label.grid(column = 1, row = 2, sticky=N, padx=10)
        else:       #There have some records
            #counting in-progress tasks
            progress_count_lbl = ttk.Label(self.upper, text="In-Progress: ", foreground='black')
            progress_num_lbl = ttk.Label(self.upper, text=f"{len(m.list_of_task(status = 1))}", foreground='white', background = "blue")

            progress_count_lbl.grid(column=0, row=0, sticky=W, padx = 10)
            progress_num_lbl.grid(column=0, row=0)
            #end counting in-progress task
            #counting pending tasks
            pending_count_lbl = ttk.Label(self.upper, text="Pending: ", foreground='black')
            pending_num_lbl = ttk.Label(self.upper, text=f"{len(m.list_of_task(status = 0))}", foreground='white', background = "blue")

            pending_count_lbl.grid(column=1, row=0, sticky=W, padx = 10)
            pending_num_lbl.grid(column=1, row=0)
            #end counting pending task
            #counting complete tasks
            complete_count_lbl = ttk.Label(self.upper, text="Complete: ", foreground='black')
            complete_num_lbl = ttk.Label(self.upper, text=f"{len(m.list_of_task(status = 2))}", foreground='white', background = "blue")

            complete_count_lbl.grid(column=2, row=0, sticky=W, padx = 10)
            complete_num_lbl.grid(column=2, row=0)
            #end counting completetask


            # Define a bold font only for headers
            bold_font = font.Font(family="Helvetica", size=12, weight="bold")

            # creating 3 column headers label
            id_lbl=ttk.Label(self.upper, text = "ID", font = bold_font) #task id
            name_lbl = ttk.Label(self.upper, text = "NAME", font = bold_font) #task name
            status_lbl = ttk.Label(self.upper, text = "STATUS", font = bold_font) #task status
            #attack grid
            id_lbl.grid(column=0, row=1, sticky=N)
            name_lbl.grid(column=1, row=1, sticky=N)
            status_lbl.grid(column=2, row=1, sticky=N)

            #loop through tasks and create label for each task
            m = Model()  # to get task id
            tasks = m.list_of_task()    #all today tasks
            #need to sort tasks base on task status 
            #attach task to grid
            row, column = 2, 0      #row will start from 1 because row 0 ocupied by column indexes
            for item in self.sort_tasks(tasks):
                # print(key)
                key = item[0]
                task = item[1]
                # set task color base on status 
                color = 'green' if task['status'] == 2 else 'orangered' if task['status'] == 1 else 'black'
                # Create labels for each task
                id_label = ttk.Label(self.upper, text=key, foreground = color)
                name_label = ttk.Label(self.upper, text=task['task'], foreground = color)
                status_label = ttk.Label(self.upper, text = status(task['status']), foreground = color)

                #grid thoes label
                #thoes will start from row 1 
                id_label.grid(column=column, row=row, sticky=N,)
                column +=1
                name_label.grid(column=column, row=row, sticky=N, ipadx = 5)
                column +=1
                status_label.grid(column=column, row=row, sticky=N, ipadx = 5)
                column  = 0  #reset column to 0 for next row
                row += 1  #move to next row for next task
                


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
            # print(child)
            child.grid_forget()
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

    def sort_tasks(self, tasks:dict) -> list:
        '''This will sort tasks base on task status
        1. Pending
        2. In progress
        3. Completed
        '''
        in_progress_tsk, pending_tsk, completed_tsk = [], [], []
        for key in list(tasks.keys()):
            if tasks[key]['status'] == 1:
                in_progress_tsk.append((key, tasks[key]))
            elif tasks[key]['status'] == 2:
                completed_tsk.append((key, tasks[key]))
            else:
                pending_tsk.append((key, tasks[key]))
        # Now we will sort tasks
        return in_progress_tsk + pending_tsk + completed_tsk
        

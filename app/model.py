import os
import json
from datetime import datetime

class Model:
    def __init__(self) -> None:
        '''First check is data.json exits or not if not 
        then create one'''
        ls=os.listdir(os.getcwd())
        if 'data.json' not in ls:   #not present 
            with open('data.json', 'w') as file:
                json.dump({
                    str(datetime.today().date()):{
                        1:{
                            
                        }
                    }
                    }, file)
                
    @staticmethod
    def all_data()->dict:
        '''This on will return all json file data into navtive python dict'''
        with open('data.json' , 'r') as file:
            data=json.load(file)
            return data
        
    def write(self, data: dict)->bool:
        '''This one write data to ``data.json``'''
        with open('data.json', 'w') as file:
            json.dump(data, file)
            return True
        return False

    @staticmethod
    def get_task( task_id:int , date=datetime.today().date()):
        '''It will return only one task based on date and task_id'''
        all_data=Model.all_data()
        return all_data[str(date)][str(task_id)]

    def add(self, task_name:str, desc=None, callback=None, date=datetime.today().date()):
        '''This on add new task and callback was a method
        that will call after perform operation 
        '''
        data=Model.all_data()
        day_data=data[str(date)] #{1:{}, 2:..}
        keys=list(day_data.keys())
        last_key=keys[len(keys)-1]
        if day_data[last_key] != {}:
            last_key=str(int(last_key)+1)
        new_dict={
            'task': task_name, 
            # 'description': desc,
            'status': 0 , 
            'createAt': str(datetime.today()),
            'updateAt': str(datetime.today())
        }
        data[str(date)][last_key]=new_dict
        if self.write(data):
            if callback is not None:
                callback()
            return int(last_key)

    def update(self, task_id:int, task_name:str, callback=None, date=datetime.today().date()):
        '''This one will update records on 
        ``data.json`` file'''
        data=Model.all_data()
        day_data=data[str(date)] #{1:{}, 2:..}
        row=day_data[str(task_id)]
        new_data={
            'task': task_name, 
            'status': row['status'] , 
            'createAt': row['createAt'],
            'updateAt': str(datetime.today())
        }
        data[str(date)][str(task_id)]=new_data  
        if self.write(data):
            if callback is not None:
                callable()
            return True
        return False
    
    def delete(self, task_id: int, callback: str =None, date=datetime.today().date()):
        '''This on delete task on date base on id'''        
        data=Model.all_data()
        delete_part=data[str(date)][str(task_id)]
        data[str(date)][str(task_id)]=''
        self.write(data)
        return delete_part
    
    def mark_task(self, task_id:int, task_type:int, callback=None, date=datetime.today().date()):
        '''It will mark which one process
        each task have 3 state :
        status have 3 state 
        ``0`` -> task not complete yet
        ``1`` -> it is processing
        ``2`` -> it had completed'''
        data=Model.all_data()
        target_data=data[str(date)]
        target_data[str(task_id)]['status']=task_type
        data[str(date)]=target_data
        self.write(data)
        return task_type

    def list_of_task(self, status=None, date=datetime.today().date())->dict:
        '''This will return list of task of a specific 
        date'''
        data=Model.all_data()
        day_data=data[str(date)]
        if status==0:
            not_done={}
            day_keys=list(day_data.keys())
            for i in day_keys:
                try:
                    if day_data[i]['status']==0:
                        not_done[i]=day_data[i]
                except TypeError as e:
                    pass
            return not_done
        elif status==1: #task thoes are on processing
            process_task={}
            day_keys=list(day_data.keys())
            for i in day_keys:
                try:        #A TypeError arise for keys like{3:''}
                    if day_data[i]['status']==1:
                        process_task[i]=day_data[i]
                except TypeError as e:
                    pass
            return process_task
        elif status==2: #task thoes are done
            done_task={}
            day_keys=list(day_data.keys())
            for i in day_keys:
                try:
                    if day_data[i]['status']==2:
                        done_task[i]=day_data[i]
                except TypeError as e:
                    pass
            return done_task

        return day_data
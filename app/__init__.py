import re
from app.error import wrong_command
from app.model import Model

def add_command(command: str)->int:
    '''This one will check add command is accetable 
    or not'''
    pattern=r't-cli add "[A-Za-z]+"'
    if re.search(pattern, command) is None:
        wrong_command()
    ls=command.split('"') #Now ls was [.., target, '']
    task_name=ls[len(ls)-2]      #target task name
    m=Model()
    return m.add(task_name)

def delete_command(command: str):
    '''This will delete record'''
    pattern=r't-cli delete [0-9]+'
    if re.search(pattern, command) is None:
        wrong_command()
    task_id_ls=re.findall(r'\S*[0-9]+\Z|\S*[0-9]+\S*', command)
    # print('task_id list ', task_id_ls)
    if task_id_ls == [] or len(task_id_ls) > 1:
        wrong_command('There have confusion which one was Id')
    task_id=int(task_id_ls[0])      #target task id
    m=Model()
    return m.delete(task_id)

def process_command(command: str):
    '''This will process command'''
    #This part check 't-cli' present at first or not
    if re.match('t-cli ', command) is None:
        wrong_command()
    return True

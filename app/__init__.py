import re
from app.error import wrong_command
from app.model import Model

def add_command(command: str)->int:
    '''This one will check add command is accetable 
    or not'''
    pattern=r't-cli add "([^"]*)"'
    if re.search(pattern, command) is None:
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command()
    ls=command.split('"') #Now ls was [.., target, '']
    task_name=ls[len(ls)-2]      #target task name
    m=Model()
    return m.add(task_name)

def delete_command(command: str)->dict:
    '''This will delete record'''
    pattern=r't-cli delete [0-9]+'
    if re.search(pattern, command) is None:
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command()
    task_id_ls=re.findall(r'\S*[0-9]+\Z|\S*[0-9]+\S*', command)
    if task_id_ls == [] or len(task_id_ls) > 1:
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command('There have confusion which one was Id')
    task_id=int(task_id_ls[0])      #target task id
    m=Model()
    return m.delete(task_id)

def update_command(command: str)->bool:     #It have some serious problem
    '''Update a certain task'''
    pattern=r't-cli update [0-9] "([^"]*)"'
    if re.match(pattern, command) is None:
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command()
    task_id=int(re.findall(r'\s[0-9]+\s', command)[0])
    task_name=command.split('"')
    # print('Task name before extract ', task_name)
    task_name=task_name[len(task_name)-2]
    # print('task name ', task_name)
    m=Model()
    print('From update task name ', task_name)
    return m.update(task_id, task_name)
    
def mark_command(command:str):
    '''mark task '''
    pattern=r't-cli mark-(in-progress|done) [0-9]+'
    if re.match(pattern, command) is None:
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command()
    task_type=re.findall(r'mark-(in-progress|done)', command)
    task_id=int(re.findall(r' [0-9]+\s*', command)[0])
    m=Model()
    if task_type[0]=='in-progress':
        return m.mark_task(task_id, 1)
    return m.mark_task(task_id, 2)

def display_task_data( data: dict)->None:
    '''This one will display data to termainal'''
    print('Structure of task \n "ID"\t"Task Name"\t"Status"')
    data_keys=list(data.keys())
    for key in data_keys:
        row=data[key]
        print(f'{key}.\t|| {row['task']}.\t|| {row['status']}\t||')



def list_command(command: str):
    '''Test all kind of list'''
    pattern=r't-cli list in-progress|[A-Za-z]+$'
    m=Model()
    if re.search(r'list$', command) is not None:
        display_task_data(m.list_of_task())
        return True
    elif re.search(pattern, command) is None:
        print('From if')
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command()
    type_task=re.findall(r'in-progress|[A-Za-z]+$', command)
    list_type=type_task[len(type_task)-1]
    if list_type not in ['todo', 'done', 'in-progress']:
        print('Command:\n\t|\n\t|\n\t-->', command)
        wrong_command()
    if list_type == 'done':     #print all task list
        display_task_data(m.list_of_task(2))
    elif list_type == 'in-progress':
        display_task_data(m.list_of_task(1))
    else:   #tasks thoes status are 0
        display_task_data(m.list_of_task(0))
    return True


def process_command(command: str):
    '''This will process command'''
    part_of_command=re.findall(r't-cli [A-Za-z]+', command)[0]
    task_type=part_of_command.split(' ')[1]
    match task_type:
        case "add":
            result=add_command(command)
        case "update":
            result=update_command(command)
        case "delete":
            result=delete_command(command)
        case "list":
            result=list_command(command)
        case "mark":
            result=mark_command(command)
        
    
    # return True

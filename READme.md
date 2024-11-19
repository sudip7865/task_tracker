# Task Tracker
Task tracker is a CLI application. It tracks your daily life task. To store tasks data it used JSON(data.json) file instead of SQL database.
It have five type of command:

1.Add task\
2.Update task\
3.Delete task\
4.Mark task\
5.List task

Every task have 3 state:\
state- 0 : It was not touch.\
state- 1 : It is in-progress.\
state-2 : It was completed.

## 1.Add task:
To add a new task you should enter below command:
```
t-cli add "<Task Name>"
```
you should replce 'Task Name' with your task name.Any task that add it's status will be '0'.

## 2.Update task:
To update an existing task you should know it's `Id`(And how you can get this mention below)
Update command:
```
t-cli update <task-id> "<Task name>"
```

## 3.Delete task:
To delete an exiting task you again know that's `Id`
command:
```
t-cli delete <task-id>
```

## 4.Mark task:
Mark mean status of task that represent that task is complete(2) or in-progress(1) or not work on it yet(0)
There are two types of command to mark a task.

Mark a task that in-progress.
Command:
```
t-cli mark-in-progress <task-id>
```
Mark a task that done.
Command:
```
t-cli mark-done <task-id>
```

## 5.List task:
It will display list of task base on query. It have four type of command.

To display all task:
```
t-cli list
```
To display  all done task:
```
t-cli list done
```
Display all task in-progress:
```
t-cli list in-progress
```
Show all task todo:

```
t-cli list todo
```

This inspired by [roadmap.sh](https://roadmap.sh/projects/task-tracker)

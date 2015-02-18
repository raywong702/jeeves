#jeeves version0.13
#----OBJECTIVES-----
#I have changed how tasks are stored. Now instead of nested dictionary items, The tasks are in a list nested in the dictionary. This gives better control and access to data.

""" Destription of the Tasks List:
The "TaskList" is simply the master collection of all the individual "task"s (dictionary entries).

Expample:
incompleteList {taskid1:["Subject", "dueDate", "[collab]","estTime"]}
"""
##########################################################
#set Initial Parameters and imports
import json
import os

#loads all files
with open('incompletelist.json', 'r+') as load:
    incompleteList = json.load(load)
with open('completelist.json', 'r+') as load:
    completeList = json.load(load)
with open('counter.json', 'r+') as load:
    num = json.load(load)
##########################################################
#Information Handling
#Methods are in Order of their Menu Item

#Listing Tasks
###########################################################    
def show_incomplete():
    print ('\nPending Tasks')
    if incompleteList != {}:
        for i in sorted(incompleteList):
            print (i + ': ' + incompleteList[i][0])
    else:
        print ('There are 0 pending tasks...\n')
def show_complete():
    print ('Complete Tasks')
    if completeList != {}:
        for i in sorted(completeList):
            print (i + ': ' + completeList[i][0])
    else:
        print ('You have 0 Complete Tasks!!!\n')
def show_all():
    show_incomplete()
    show_complete()
    
def show_task():
    print ("\n[1] Complete tasks: '{0}'\n[2] Incomplete tasks: '{1}'".format(len(completeList),len(incompleteList)))
    print ('-' * 50)
    option = input('Select a list ([h] for help): ')
    show_task_action(option)
    
def show_task_action(option):
    if option == '1':
        show_complete()
    elif option == '2':
        show_incomplete()
    elif option == 'a':
        show_all
    elif option == 'b':
        main_menu()
    elif option == 'h':
        print('''
[1] - Show Completed Tasks\n
[2] - Show Incomplete Tasks\n
[a] - Show All tasks\n
[b] - Go back to Select Option\n
[h] - Display Help Menu
''')
    else:
        option = input ('try again\n Select a list([h] for help): ')
        
###########################################################
#Deleting Tasks
def del_task():
    show_all()
    i = input('select a task to remove: ')
    sure = 'n'
    if i in incompleteList:
        sure = input('are you sure that you want to remove: ' + incompleteList[i][0] + '\n([y]es or [n]o): ' )
        if sure.lower() == 'y':
            print (' deleted.')
        del incompleteList[i]
    if i in completeList:
        sure = input('are you sure that you want to remove: ' + completeList[i][0] + '\n([y]es or [n]o): ' )
        if sure.lower() == 'y':
            print ('deleted.')
            del completeList[i]
    save_task()

#Mark Task as Complete    
def complete_task():
    show_incomplete()
    i = input('select a task to mark as complete: ')
    if i != '':
        completeList[i] = incompleteList[i] #Moves task from incompleteList to completeList 
        del incompleteList[i]
        completeList[i][0] = 'Complete - ' + completeList[i][0]
    else:
        print('no task selected...')
    save_task()
    
#Erase Screen
def cls():
    os.system('cls') #Clear Screen (Windows)

#help
def help_menu():
    print('''Please select the associate letter
a - Print [a]ll tasks\n
c - Mark task as [c]omplete\n
e - [e]rase all text on screen (Windows Only)\n
n - create [n]ew task\n
w - [w]ipe all tasks and reset counters\n
u - [u]nmark as complete
Select an option: ''')

#Create Task
def create_task():
    global num #This assigns the 'num' value to the global variable
    cont = 'y' #inital setting for continue
    while cont == 'y': #until you select '[n]o'
        cont = 'n'
        #This is the input section for new tasks
        numid = str(num)
        """Legend
    [0] - Subject
    [1] - Date
    [2] - Collaborators
    [3] - Description
    [4] - Time interval
    """
        incompleteList[numid] = [input('Subject?: '), input('date?: '),input('Is anyone helping you?: '), input('Description: '), int(input('time-value?: '))]
        num += 1 #increments num to the next number
        cont = input('would you like to add another task? \nSelect [y]es or [n]o: ') #no will continue the loop
        print('You currently have %s tasks' % len(incompleteList))
    save_task()
#Unmark item
def uncomplete_task():
    show_complete()
    i = input('select a task to uncomplete: ')
    if i != '':
        incompleteList[i] = completeList[i] #Moves task from completeList to incompleteList 
        del completeList[i]
        incompleteList[i][0] = incompleteList[i][0].lstrip('Complete - ')
    else:
        print('no task selected...')
    save_task()
#Wipe Tasks
def wipe_task():
    global num
    sure = input('This operation cannot be undone. It will erase everything and start your index over. Continue? [y]es or [n]o: ')
    if sure.lower() == 'y':
        sure = 'n'
        sure = input("I'm being serious you will lose everything? Still Continue [y]es/[n]o: ")
        if sure.lower() == 'y':
            incompleteList.clear()
            completeList.clear()
            num = 1
            print ('All tasks have been removed and the counter is reset')
            save_task()
        else:
            print('Wipe Aborted')
    else:
        print('Wipe Aborted')
#Evaluate Time Function
def evaluateTime():
    global lstPrint
    lst = list()
    for i in incompleteList:
        lst.append(incompleteList[i][4])
    lstHours  = sum(lst) // 60
    lstMinutes = sum(lst) % 60
    lstPrint = str(lstHours) + ' hours ' + str(lstMinutes) + ' minutes'
    print (lst)
    return lstPrint

def select_task():
    show_all()
    option = input('select a task: ')
    if option in completeList: print ('''\nSubject: '{0}' \n {5} \nDate: '{1}' \nCollaborators: '{2}' \nDescription: '{3}' \nTime Interval: '{4} \n'''.format(completeList[option][0],completeList[option][1],completeList[option][2],completeList[option][3],completeList[option][4], hr))
    elif option in incompleteList: print ('''\nSubject: '{0}' \n {5} \nDate: '{1}' \nCollaborators: '{2}' \nDescription: '{3}' \nTime Interval: '{4} \n'''.format(incompleteList[option][0],incompleteList[option][1],incompleteList[option][2],incompleteList[option][3],incompleteList[option][4], hr))
    elif option.lower == 'b': main_menu()
    else:
        print ('try again')
hr = '-' * 50
############################################################
"""Instructions for setting up new options.
When you have an option be sure to add the following code:
<TEST CODE>
elif option.lower() =='<letter>':
    <action>
    </TEST CODE>"""
#This Selects tasks from your list ONLY if there are tasks
def main_menu():
    evaluateTime()
    print("[Main Menu]\n'{2}' \nYou currently have '{0}' tasks pending \nLasting '{1}'\n'{2}'".format(len(incompleteList), lstPrint, hr))
    global num
    if num != 0:
        option = input("""[1] - Create Task
[2] - List Tasks
[3] - Mark Task as Complete
[4] - Delete Tasks
Please select an option (press 'h' for help): """)
        print('-' * 50)
        if option.lower() not in 'abdfgijklmopqrstvxyz-!@#$%^&*()_+=567890': #Checks to see if the command is valid
            if option.lower() == '1': #creates new task
                create_task()
                main_menu()
            elif option.lower() == '2': #lists all tasks
                select_task()
                main_menu()
            elif option.lower() == '3': #mark as complete
                complete_task()
                main_menu()
            elif option.lower() == '4': #deletes task
                del_task()
                main_menu()
            elif option.lower() == 'e': #erase
                cls()
                main_menu()
            elif option.lower() == 'h': #opens help dialogue
                help_menu()
                main_menu()
            elif option.lower() =='u': #unmark tasks
                uncomplete_task()
                main_menu()
            elif option.lower() == 'w': #wipes tasks
                wipe_task()
                main_menu()
        else:
            print ('please try again')
            main_menu()
    else: #Always start by creating a task
        create_task()
########################################################    
#Saving and Loading tasks
#Tasks will be Saved using a JSON format or .txt format
#save tasks as JSON
def save_task(): #This stores that actual Values
    with open('incompletelist.json','w') as save:
        json.dump(incompleteList,save, sort_keys = True)
    with open('completelist.json','w') as save:
        json.dump(completeList,save, sort_keys = True)
    with open('counter.json','w') as save:
        json.dump(num,save)
########################################################
#BEGIN EXECUTION
main_menu()



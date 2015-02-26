#import JSON Module
import json
import yaml
#impor sys to pull files from SupportDocs
#import filemgr
#loads all files

def load_Files():
    global taskList
    global taskCounter
    global taskTags
    with open('taskList.json', 'r+') as load:
       taskList = yaml.load(load)
    with open('taskCounter.json', 'r+') as load:
        taskCounter = yaml.load(load)
    with open('taskTags.json', 'r+') as load:
        taskTags = yaml.load(load)
def save_Files():
    with open('taskList.json', 'w') as save:
        json.dump(taskList,save, sort_keys = True)
    with open('taskCounter.json', 'w') as save:
        json.dump(taskCounter,save, sort_keys = True)
    with open('taskTags.json', 'w') as save:
       json.dump(taskTags,save, sort_keys = True)

def list_Tasks():
    for x in taskList:
        for y in taskList[x]:
            print taskList[x]['task']

def create_Task():
    a = raw_input('Enter the task: ')
    x = int(0)
    if a[0] == '!':
        priority = True
        print 'priority task'
        a = a[1:]
    else:
        priority = False
        print 'normal task'
    while x in taskList:
        x += 1
        print x
    taskList[x] = { 
        'task':a, 
        'priority':priority
        }
    print "Task:'%s' has been created" % taskList[x]['task']
   
    
def create_Tags():
    for x in taskTags:
        print taskTags[x]
    a = raw_input('Enter a Tag: ')
    hasha = '#' + a
    if hasha in taskTags:
        print 'you have selected: %s' % taskTags[hasha]
    else:
        taskTags[hasha] = a
        print "%s not found. Tag: %s created" % (hasha,hasha)

    
load_Files()
create_Task()
list_Tasks()
create_Task()
print taskList
Save_Files()
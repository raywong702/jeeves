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

def list_Tasks(a):
    d = 0
    print '''Priority
=========================''' 
    for d in sorted(a):
        if a[d]['priority'] == True:
            print '[%s]: %s'  %(d,a[d]['task'])
            d = int(d) + 1
    d = 0
    print '''
Tasks
========================='''
    for d in sorted(a):
        if a[d]['priority'] == False:
            print '[%s]: %s'  %(d,a[d]['task'])
            d = int(d) + 1        
class Task:
    def create_Task():
        a = raw_input('Enter the task: ')
        x = int(0)
        if a[0] == '!':
            priority = True
            print 'priority task detected'
            a = a[1:]
        else:
            priority = False
            print 'normal task detected'
        if '#' in a:
            hashtagLocation = a.index('#')
            print 'tag detected at the %d spot' % hashtagLocation
        
        for y in taskList:
            x += 1
        taskList[int(x)] = { 
            'task':a, 
            'priority':priority
            }
        print "Task:'%s' has been created" % taskList[x]['task']
        if raw_input('Continue?: ') == 'y': create_Task()
    
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

def del_Task():
    list_Task()
    d = input ('select a task')
    if input ("are you sure you want to delete '%s'") % (taskList[d]['task']) == 'y': del taskList[d]

def main():
    print '''[n]ew Task
    [l]Task'''

    input
    

print taskList
#main()


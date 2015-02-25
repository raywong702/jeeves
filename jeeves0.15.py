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
    for x in taskList: print x

def create_Tags():
    a = raw_input('Enter a Tag: ')
    hasha = '#' + a
    taskTags[hasha] = a
    save_Files()
    
load_Files()
list_Tasks()
print "tags: %s" % taskTags
create_Tags()
print taskTags




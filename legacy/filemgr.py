#import JSON Module
import json
import yaml

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
        
#saves all files
def save_Files():
    with open('taskList.json', 'w') as save:
        json.dump(taskList,save, sort_keys = True)
    with open('taskCounter.json', 'w') as save:
        json.dump(taskCounter,save, sort_keys = True)
    with open('taskTags.json', 'w') as save:
       json.dump(taskTags,save, sort_keys = True)

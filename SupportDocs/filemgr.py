#import JSON Module
import json

#loads all files
def loadFiles():
    with open('taskList.json', 'r+') as load:
       taskList = json.load(load)
    with open('taskCounter.json', 'r+') as load:
        taskCounter = json.load(load)
    with open('taskCategories.json', 'r+') as load:
        taskCategories = json.load(load)
    with open('taskTags.json', 'r+') as load:
        taskTags = json.load(load)

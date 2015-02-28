from taskmgr import task
#main program        
taskList = []        
def main():
    tid = len(taskList)
    newTask = task(tid)
    newTask.add_tags()
    newTask.check_priority()
    taskList.append(newTask.name)
    for x in taskList:  print x,
    if raw_input('Continue?: ') == 'y': main()
if __name__ == "__main__": main()



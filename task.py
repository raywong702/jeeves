#This is the code taskmgr.py code
class task:
    def __init__(self,tid):

        self.tid = tid
        self.name = raw_input('enter a task: ')
        self.tags = []
        self.priority = False
        
    def add_tags(self):
        phrase = self.name
        print "%d tag(s) found" % phrase.count('#')
        for x in phrase.split():
            if x[0] == '#':
                self.tags.append(x)
    

    def check_priority(self):
        if self.name[0] == '!':
            print 'This task is a Priority!'
            self.priority = True
        else:
            self.priority = False

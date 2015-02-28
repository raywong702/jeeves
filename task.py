class task:

    def __init__(self, tid, desc, priority, tags):
        self.tid = tid
        self.desc = desc
        self.priority = priority
        self.tags = tags.split()


    def __str__(self):
        return """tid: {}
desc: {}
priority: {}
tags: {}""".format(self.tid,
                       self.desc,
                       self.priority,
                       self.tags)


    def add_tags(self, tags):
        for index, tag in enumerate(tags.split()):
            self.tags.append(tag)


    def check_priority(self):
        pass

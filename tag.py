class tag:

    def __init__(self, tag, priority = 0):
        self.tag = tag
        self.priority = priority

    def __str__(self):
        return "{} : {}".format(self.tag, self.priority)
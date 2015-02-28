import tag

class tag_list:

    def __init__(self, tag = None):
        self.tag_list = []
        self.append(tag)

    def __str__(self):
        ret = ""
        for index, tag in enumerate(self.tag_list):
            ret += str(tag) + "\n"
        return ret

    def append(self, tag = None):
        if tag != None:
            self.tag_list.append(tag)

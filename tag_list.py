import tag

class tag_list:

    def __init__(self, tag = None):
        self.tag_list = []
        if tag != None:
            self.tag_list.append(tag)

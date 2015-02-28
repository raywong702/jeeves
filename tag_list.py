import tag

class tag_list:

    def __init__(self, tag = None):
        self.tag_list = []
        self.append(tag)

    def __str__(self):
        ret = "["
        for tag in self.tag_list:
            ret += str(tag) + ", "
        if ", " in ret:
            ret = ret[:ret.rindex(", ")]
        return ret + "]"

    def append(self, tag = None):
        if tag != None:
            self.tag_list.append(tag)

    def exists(self, tag):
        for t in self.tag_list:
            if tag.name == t.name:
                return True
        return False

    def get_tag(self, tag_name):
        for t in self.tag_list:
            if tag_name == t.name:
                return t

    def get_max_priority(self):
        max_priority = 0
        for tag in self.tag_list:
            if self.exists(tag):
                if tag.priority > max_priority:
                    max_priority = tag.priority
        return max_priority

if __name__ == "__main__":
    pass
import tag
import tag_list

class task(object):

    def __init__(self, tid, desc, master_tag_list):
        self.tid = tid
        self.desc = desc
        self.master_tag_list = master_tag_list
        self.tags = tag_list.tag_list()
        self.find_hash_tags(desc) # this will update tags
        self.priority = self.tags.get_max_priority()


    def __str__(self):
        s = ["tid: {}\n".format(self.tid),
             "desc: {}\n".format(self.desc),
             "priority: {}\n".format(self.priority),
             "tags: {}".format(self.tags)]
        return "".join(s)


    # takes in a sentence and tagifys the words
    def add_tags(self, tags):
        for tag_name in tags.split():
            tag = tag.tag(tag_name)
            self.tags.append(tag)
            self.update(tag)

    # takes in a sentence and removes the tagified words
    def remove_tags(self, tags):
        for tag_name in tags.split():
            tag = tag.tag(tag_name)
            self.tags.pop(tag)

    def update(self, t):
        if not self.master_tag_list.exists(t):
            self.master_tag_list.append(t)
        else:
            self.tags.append(self.master_tag_list.get_tag(t.name))

    def find_hash_tags(self, s):
        for word in s.split():
            if word[0] == "#":
                t = tag.tag(word[1:])
                self.update(t)

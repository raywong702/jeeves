import Tag
import TagList

class Task(object):

    def __init__(self, tid, desc, master_tag_list):
        self.tid = tid
        self.desc = desc
        self.master_tag_list = master_tag_list
        self.priority = 0
        self.tags = TagList.TagList()
        self.update(self.find_hash_tags(desc)) # update tags, master, priority

    def __str__(self):
        s = ["tid: {}\n".format(self.tid),
             "desc: {}\n".format(self.desc),
             "priority: {}\n".format(self.priority),
             "tags: {}".format(self.tags)]
        return "".join(s)

    # takes in a sentence and tagifys the words
    def add_tags(self, tags):
        t_list = []
        for tag_name in tags.split():
            t = Tag.Tag(tag_name)
            if self.master_tag_list.exists(t):
                t = self.master_tag_list.get_tag(tag_name)
            t_list.append(t)
        self.update(t_list)

    # takes in a sentence and removes the tagified words
    def remove_tags(self, tags):
        for tag_name in tags.split():
            self.tags.pop(Tag.Tag(tag_name))
        self.priority = self.tags.get_max_priority()

    def update(self, t_list):
        for t in t_list:
            if not self.master_tag_list.exists(t):
                self.master_tag_list.append(t)
                self.tags.append(t)
            else:
                self.tags.append(self.master_tag_list.get_tag(t.name))
        self.priority = self.tags.get_max_priority()

    def find_hash_tags(self, s):
        hash_tags = []
        for word in s.split():
            if word[0] == "#":
                t = Tag.Tag(word[1:])
                hash_tags.append(t)
        return hash_tags

if __name__ == "__main__":
    pass

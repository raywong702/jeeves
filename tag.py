class tag:

    def __init__(self, tag, priority = 0):
        self.name = tag
        self.priority = priority

    def __str__(self):
        return "{}:{}".format(self.name, self.priority)

    def equals(tag):
    	if self.name == tag.name:
    		return True
    	return False

if __name__ == "__main__":
    pass
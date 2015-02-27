class category:
    def __init__(self, **kwargs):
        self.variables = kwargs
        self.variables['priority'] = 0

    def get_variable(self,k):
        return self.variables[k]

    def set_variable(self,k,v):
        self.variable[k] = v
    
def main():
    home = category()
    print home.get_variable('priority')
if __name__ == "__main__": main()

main()

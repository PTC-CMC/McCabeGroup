import mbuild as mb
class oh12(mb.Compound):
    def __init__(self):
        super(oh12,self).__init__()
        mb.load('oh12.mol2', compound=self, relative_to_module=self.__module__)
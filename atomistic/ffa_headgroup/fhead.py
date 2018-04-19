import mbuild as mb
class fhead(mb.Compound):
    def __init__(self):
        super(fhead,self).__init__()
        mb.load('fhead.mol2', compound=self, relative_to_module=self.__module__)
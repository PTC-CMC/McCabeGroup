import mbuild as mb
class chead(mb.Compound):
    def __init__(self):
        super(chead,self).__init__()
        mb.load('chead.mol2', compound=self, relative_to_module=self.__module__)
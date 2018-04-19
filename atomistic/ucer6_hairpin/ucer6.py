import mbuild as mb
class ucer6(mb.Compound):
    def __init__(self):
        super(ucer6,self).__init__()
        mb.load('ucer6.mol2', compound=self, relative_to_module=self.__module__)
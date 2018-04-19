import mbuild as mb
class ucer2(mb.Compound):
    def __init__(self):
        super(ucer2,self).__init__()
        mb.load('ucer2.mol2', compound=self, relative_to_module=self.__module__)
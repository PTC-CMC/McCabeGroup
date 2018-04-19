import mbuild as mb
class ucer3(mb.Compound):
    def __init__(self):
        super(ucer3,self).__init__()
        mb.load('ucer3.mol2', compound=self, relative_to_module=self.__module__)
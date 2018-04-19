import mbuild as mb
class ffa24(mb.Compound):
    def __init__(self):
        super(ffa24,self).__init__()
        mb.load('ffa24.mol2', compound=self, relative_to_module=self.__module__)
import mbuild as mb
class ffa16(mb.Compound):
    def __init__(self):
        super(ffa16,self).__init__()
        mb.load('ffa16.mol2', compound=self, relative_to_module=self.__module__)

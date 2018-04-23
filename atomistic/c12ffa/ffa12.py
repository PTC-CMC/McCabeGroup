import mbuild as mb
class ffa12(mb.Compound):
    def __init__(self):
        super(ffa12,self).__init__()
        mb.load('ffa12.mol2', compound=self, relative_to_module=self.__module__)
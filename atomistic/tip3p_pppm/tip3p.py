import mbuild as mb
class tip3p(mb.Compound):
    def __init__(self):
        super(tip3p,self).__init__()
        mb.load('tip3p.mol2', compound=self, relative_to_module=self.__module__)
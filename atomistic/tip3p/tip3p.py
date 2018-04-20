import mbuild as mb
class HOH(mb.Compound):
    def __init__(self):
        super(HOH,self).__init__()
        mb.load('tip3p.mol2', compound=self, relative_to_module=self.__module__)

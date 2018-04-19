import mbuild as mb
class ecer6(mb.Compound):
    def __init__(self):
        super(ecer6,self).__init__()
        mb.load('ecer6.mol2', compound=self, relative_to_module=self.__module__)
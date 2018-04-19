import mbuild as mb
class ecer2(mb.Compound):
    def __init__(self):
        super(ecer2,self).__init__()
        mb.load('ecer2.mol2', compound=self, relative_to_module=self.__module__)

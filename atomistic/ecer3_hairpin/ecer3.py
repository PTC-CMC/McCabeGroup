import mbuild as mb
class ecer3(mb.Compound):
    def __init__(self):
        super(ecer3,self).__init__()
        mb.load('ecer3.mol2', compound=self, relative_to_module=self.__module__)
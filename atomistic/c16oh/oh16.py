import mbuild as mb
class oh16(mb.Compound):
    def __init__(self):
        super(oh16,self).__init__()
        mb.load('oh16.mol2', compound=self, relative_to_module=self.__module__)
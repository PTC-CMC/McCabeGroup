import mbuild as mb
class oh24(mb.Compound):
    def __init__(self):
        super(oh24,self).__init__()
        mb.load('oh24.mol2', compound=self, relative_to_module=self.__module__)

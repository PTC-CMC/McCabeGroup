import mbuild as mb
class cer1(mb.Compound):
    def __init__(self):
        super(cer1,self).__init__()
        mb.load('cer1.mol2', compound=self, relative_to_module=self.__module__)
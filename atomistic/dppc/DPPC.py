import mbuild as mb
class DPPC(mb.Compound):
    def __init__(self):
        super(DPPC,self).__init__()
        mb.load('DPPC.mol2', compound=self, relative_to_module=self.__module__)
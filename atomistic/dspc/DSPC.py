import mbuild as mb
class DSPC(mb.Compound):
    def __init__(self):
        super(DSPC,self).__init__()
        mb.load('DSPC.mol2', compound=self, relative_to_module=self.__module__)
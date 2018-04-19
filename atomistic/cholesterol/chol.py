import mbuild as mb
class chol(mb.Compound):
    def __init__(self):
        super(chol,self).__init__()
        mb.load('chol.mol2', compound=self, relative_to_module=self.__module__)
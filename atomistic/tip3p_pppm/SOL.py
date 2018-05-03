import mbuild as mb
class SOL(mb.Compound):
    def __init__(self):
        super(SOL,self).__init__()
        mb.load('SOL.mol2', compound=self, relative_to_module=self.__module__)
        self.children[0].charge = -0.83
        self.children[1].charge = 0.415
        self.children[2].charge = 0.415
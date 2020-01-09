import mbuild as mb
class SOL(mb.Compound):
    def __init__(self, use_atom_name=True):
        super(SOL,self).__init__()
        if use_atom_name:
            mb.load('SOL_new.mol2', compound=self, relative_to_module=self.__module__,
                    infer_hierarchy=False)
        else:
            mb.load('SOL.mol2', compound=self, relative_to_module=self.__module__,
                    infer_hierarchy=False)
        self.children[0].charge = -0.83
        self.children[1].charge = 0.415
        self.children[2].charge = 0.415

import mbuild as mb
class fhead(mb.Compound):
    def __init__(self, use_atom_name=True):
        super(fhead,self).__init__()
        if use_atom_name:
            mb.load('fhead_new.mol2', compound=self, 
                    relative_to_module=self.__module__,
                    infer_hiearchy=False)
        else:
            mb.load('fhead.mol2', compound=self, relative_to_module=self.__module__,
                    infer_hierarchy=False)
        self.children[0].charge = 0.0
        self.children[1].charge = 0.89
        self.children[2].charge = -0.68
        self.children[3].charge = 0.42
        self.children[4].charge = -0.63

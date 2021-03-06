import mbuild as mb
class chead(mb.Compound):
    def __init__(self, use_atom_name=True):
        super(chead,self).__init__()
        if use_atom_name:
            mb.load('chead_new.mol2', compound=self, 
                    relative_to_module=self.__module__,
                    infer_hierarchy=False)
        else:
            mb.load('chead.mol2', compound=self, relative_to_module=self.__module__,
                    infer_hierarchy=False)
        self.children[0].charge = 0.006
        self.children[1].charge = 0.107
        self.children[2].charge = -0.56
        self.children[3].charge = 0.34
        self.children[4].charge = 0.107
        self.children[5].charge = 0.1
        self.children[6].charge = -0.3
        self.children[7].charge = 0.1
        self.children[8].charge = 0.1

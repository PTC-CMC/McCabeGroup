import mbuild as mb
import numpy as np

class Chol(mb.Compound):
    def __init__(self):
        """Returns a CG CHOL with the head-to-tail vector pointing in -z.
        """
        super(Chol, self).__init__()
        mb.load('chol.hoomdxml', compound=self, relative_to_module=self.__module__)
        xx = list(self.particles())
        mb.coordinate_transform.z_axis_transform(self,
                new_origin=xx[0], point_on_z_axis=xx[6])
        self.rotate(np.pi, [1, 0, 0])
        masses =[0.611858, 0.723277, 0.556457, 0.737278, 0.751278, 0.779278,
                 0.793278, 0.208819, 0.208819]
        self.mass = np.sum(masses)

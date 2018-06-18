import ecer2
from groupy.gbb import Gbb
from groupy.system import System
from groupy.mdio import write_lammpsdata
import pdb
cmpd_to_xml_dict = {'ecer2': 'ecer2-hairpin.xml'}

mycmpd = ecer2.ecer2()
xml_file = cmpd_to_xml_dict[mycmpd.name]
mygbb = Gbb(xml_prototype=xml_file)
system = System(box=mycmpd.boundingbox, gbbs=[mygbb])
system.print_lammpsdata(system, mycmpd.boundingbox, ff_param_set='charmm')

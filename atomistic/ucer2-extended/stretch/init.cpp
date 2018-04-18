#include "/Users/tcmoore3/group-code/common.hpp"

int main() {
    gbb cer2(129, 128, 247, 452, 4, 0);
    cer2.load_all_topology_no_coord("/Users/tcmoore3/prototypes/charmm/ucer2-hairpin-charmm/"); 
    cer2.v_type.clear(); 
    cer2.load_coord("coords.txt"); 
    cer2.shift_com(); 
    cer2.translate_coord(0, 0, -13.0); 
    box_info box;
    init_box(box, 100, 100, 100); 
    System sys(false, false, false, false); 
    sys.box = box; 
    sys.insert_component(cer2);
    sys.init_from_prototype(); 
    std::ofstream out("cer2.lammpsdata"); 
    system_translator_LAMMPS_full_CHARMM(sys, out); 
    return 0; 
}

import mbuild as mb
class cer1(mb.Compound):
    def __init__(self, use_atom_name=True):
        super(cer1,self).__init__()
        if use_atom_name:
            mb.load('cer1_new.mol2', compound=self, relative_to_module=self.__module__)
        else:
            mb.load('cer1.mol2', compound=self, relative_to_module=self.__module__)
        self.children[0].charge = -0.3
        self.children[1].charge = -0.18
        self.children[2].charge = -0.18
        self.children[3].charge = -0.18
        self.children[4].charge = -0.18
        self.children[5].charge = -0.18
        self.children[6].charge = -0.18
        self.children[7].charge = -0.18
        self.children[8].charge = -0.18
        self.children[9].charge = -0.18
        self.children[10].charge = -0.18
        self.children[11].charge = -0.18
        self.children[12].charge = -0.18
        self.children[13].charge = -0.09
        self.children[14].charge = -0.09
        self.children[15].charge = 0.03
        self.children[16].charge = -0.56
        self.children[17].charge = 0.34
        self.children[18].charge = 0.15
        self.children[19].charge = 0.06
        self.children[20].charge = -0.54
        self.children[21].charge = 0.34
        self.children[22].charge = -0.54
        self.children[23].charge = 0.26
        self.children[24].charge = 0.58
        self.children[25].charge = -0.53
        self.children[26].charge = -0.26
        self.children[27].charge = -0.18
        self.children[28].charge = -0.18
        self.children[29].charge = -0.18
        self.children[30].charge = -0.18
        self.children[31].charge = -0.18
        self.children[32].charge = -0.18
        self.children[33].charge = -0.18
        self.children[34].charge = -0.18
        self.children[35].charge = -0.18
        self.children[36].charge = -0.18
        self.children[37].charge = -0.18
        self.children[38].charge = -0.18
        self.children[39].charge = -0.18
        self.children[40].charge = -0.18
        self.children[41].charge = -0.18
        self.children[42].charge = -0.18
        self.children[43].charge = -0.18
        self.children[44].charge = -0.18
        self.children[45].charge = -0.18
        self.children[46].charge = -0.18
        self.children[47].charge = -0.18
        self.children[48].charge = -0.18
        self.children[49].charge = -0.18
        self.children[50].charge = -0.18
        self.children[51].charge = -0.18
        self.children[52].charge = -0.18
        self.children[53].charge = -0.18
        self.children[54].charge = 0.08
        self.children[55].charge = -0.49
        self.children[56].charge = 0.9
        self.children[57].charge = -0.63
        self.children[58].charge = -0.22
        self.children[59].charge = -0.18
        self.children[60].charge = -0.18
        self.children[61].charge = -0.18
        self.children[62].charge = -0.18
        self.children[63].charge = -0.18
        self.children[64].charge = -0.18
        self.children[65].charge = -0.09
        self.children[66].charge = -0.09
        self.children[67].charge = -0.18
        self.children[68].charge = -0.09
        self.children[69].charge = -0.09
        self.children[70].charge = -0.18
        self.children[71].charge = -0.18
        self.children[72].charge = -0.18
        self.children[73].charge = -0.18
        self.children[74].charge = -0.3
        self.children[75].charge = 0.1
        self.children[76].charge = 0.1
        self.children[77].charge = 0.1
        self.children[78].charge = 0.09
        self.children[79].charge = 0.09
        self.children[80].charge = 0.09
        self.children[81].charge = 0.09
        self.children[82].charge = 0.09
        self.children[83].charge = 0.09
        self.children[84].charge = 0.09
        self.children[85].charge = 0.09
        self.children[86].charge = 0.09
        self.children[87].charge = 0.09
        self.children[88].charge = 0.09
        self.children[89].charge = 0.09
        self.children[90].charge = 0.09
        self.children[91].charge = 0.09
        self.children[92].charge = 0.09
        self.children[93].charge = 0.09
        self.children[94].charge = 0.09
        self.children[95].charge = 0.09
        self.children[96].charge = 0.09
        self.children[97].charge = 0.09
        self.children[98].charge = 0.09
        self.children[99].charge = 0.09
        self.children[100].charge = 0.09
        self.children[101].charge = 0.09
        self.children[102].charge = 0.09
        self.children[103].charge = 0.09
        self.children[104].charge = 0.08
        self.children[105].charge = 0.12
        self.children[106].charge = 0.105
        self.children[107].charge = 0.105
        self.children[108].charge = 0.13
        self.children[109].charge = 0.13
        self.children[110].charge = 0.09
        self.children[111].charge = 0.09
        self.children[112].charge = 0.09
        self.children[113].charge = 0.09
        self.children[114].charge = 0.09
        self.children[115].charge = 0.09
        self.children[116].charge = 0.09
        self.children[117].charge = 0.09
        self.children[118].charge = 0.09
        self.children[119].charge = 0.09
        self.children[120].charge = 0.09
        self.children[121].charge = 0.09
        self.children[122].charge = 0.09
        self.children[123].charge = 0.09
        self.children[124].charge = 0.09
        self.children[125].charge = 0.09
        self.children[126].charge = 0.09
        self.children[127].charge = 0.09
        self.children[128].charge = 0.09
        self.children[129].charge = 0.09
        self.children[130].charge = 0.09
        self.children[131].charge = 0.09
        self.children[132].charge = 0.09
        self.children[133].charge = 0.09
        self.children[134].charge = 0.09
        self.children[135].charge = 0.09
        self.children[136].charge = 0.09
        self.children[137].charge = 0.09
        self.children[138].charge = 0.09
        self.children[139].charge = 0.09
        self.children[140].charge = 0.09
        self.children[141].charge = 0.09
        self.children[142].charge = 0.09
        self.children[143].charge = 0.09
        self.children[144].charge = 0.09
        self.children[145].charge = 0.09
        self.children[146].charge = 0.09
        self.children[147].charge = 0.09
        self.children[148].charge = 0.09
        self.children[149].charge = 0.09
        self.children[150].charge = 0.09
        self.children[151].charge = 0.09
        self.children[152].charge = 0.09
        self.children[153].charge = 0.09
        self.children[154].charge = 0.09
        self.children[155].charge = 0.09
        self.children[156].charge = 0.09
        self.children[157].charge = 0.09
        self.children[158].charge = 0.09
        self.children[159].charge = 0.09
        self.children[160].charge = 0.09
        self.children[161].charge = 0.09
        self.children[162].charge = 0.09
        self.children[163].charge = 0.09
        self.children[164].charge = 0.09
        self.children[165].charge = 0.09
        self.children[166].charge = 0.09
        self.children[167].charge = 0.09
        self.children[168].charge = 0.09
        self.children[169].charge = 0.09
        self.children[170].charge = 0.09
        self.children[171].charge = 0.09
        self.children[172].charge = 0.09
        self.children[173].charge = 0.09
        self.children[174].charge = 0.09
        self.children[175].charge = 0.09
        self.children[176].charge = 0.09
        self.children[177].charge = 0.09
        self.children[178].charge = 0.09
        self.children[179].charge = 0.09
        self.children[180].charge = 0.09
        self.children[181].charge = 0.09
        self.children[182].charge = 0.09
        self.children[183].charge = 0.09
        self.children[184].charge = 0.09
        self.children[185].charge = 0.09
        self.children[186].charge = 0.09
        self.children[187].charge = 0.09
        self.children[188].charge = 0.09
        self.children[189].charge = 0.09
        self.children[190].charge = 0.09
        self.children[191].charge = 0.09
        self.children[192].charge = 0.09
        self.children[193].charge = 0.09
        self.children[194].charge = 0.1
        self.children[195].charge = 0.1
        self.children[196].charge = 0.1

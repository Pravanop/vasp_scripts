from pymatgen.io.lobster import Grosspop
import numpy as np
import matplotlib.pyplot as plt

doping_list = ["0" , '0,5', "1" ,'1,5', "2"]
phase_list = ['pca21' , 'p42nmc' , 'pbcm']

oxy_list = {
					'pca21'  : {
							'0' : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
							'0,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'1' : [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)] ,
							'1,5': [(8 , 9 , 10 , 11) , (4 , 5 , 6 , 7)],
							'2' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							
							} ,
					'pbcm'   : {
							'0' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'0,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'1,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'2' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
							} ,
					'p42nmc' : {
							'0' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'0,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'1' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)] ,
							'1,5': [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)],
							'2' : [(4 , 5 , 6 , 7) , (8 , 9 , 10 , 11)]
							}
						
					}

for phase in phase_list :
	print(phase + ':')
	pop_zr = []
	pop_polar = []
	pop_non_polar = []
	for doping in doping_list :
		grosspop = Grosspop(
				filename = f"/Users/pravanomprakash/Downloads/zro2_relaxed_doped/{phase}"
				           f"_{doping}/GROSSPOP.lobster"
				)
		
		p_list = oxy_list[phase][doping][0]
		np_list = oxy_list[phase][doping][1]
		
		pop_zr.append(list(grosspop.list_dict_grosspop[0]["Mulliken GP"].values()))
		pop_polar.append(list(grosspop.list_dict_grosspop[p_list[0]]["Mulliken GP"].values()))
		pop_non_polar.append(list(grosspop.list_dict_grosspop[np_list[0]]["Mulliken GP"].values()))
	
	pop_zr = np.array(pop_zr).T
	pop_polar = np.array(pop_polar).T
	pop_non_polar = np.array(pop_non_polar).T
	
	print(pop_non_polar.T)
	# o_orbital = ['2s', '$2p_y$', '$2p_z$', '$2p_x$', 'Total']
	# zr_orbital = ['5s', '$4p_y$', '$4p_z$', '$4p_x$', '$4d_{xy}$', '$4d_{yz}$', '$4d_z^{2}$', '$4d_{xz}$',
	#               '$4d_{x^{2}-y^{2}$', 'Total']
	# holes = [0, 0.05, 0.1, 0.15, 0.2]
	

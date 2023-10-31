import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols , diff , Eq , solve
from tqdm import tqdm

import warnings
warnings.filterwarnings("ignore")

N = 200
T = np.round(np.linspace(700 , 1800 , N) , 2)
x_si , dx = np.linspace(0.0001 , 1.00 , 3001 , retstep = True)

G_hcp_mg = -0.0135 * T ** 2 - 39.41 * T + 6340.7
G_diamond_Si = -0.011 * T ** 2 - 25.125 * T + 5573
G_liquid_mg = -0.0002 * T ** 2 - 8.9146 * T + 8339.1 + G_hcp_mg
G_liquid_Si = 0.0002 * T ** 2 - 30.497 * T + 50882 + G_diamond_Si
G_hcp_Si = 49200 - 20.8 * T + G_diamond_Si
G_Mg2Si = -92250 + 440.4 * T - 75.9 * T * np.log(T) - 0.0018 * T ** 2 + 630000 / T
G_Mg2Si = 1 / 3 * (G_Mg2Si)

Lo = -83864.26 + 32.44438 * T
L1 = 18027.41 - 19.61202 * T
L2 = 2486.67 - 0.31084 * T
L3 = 18541.17 - 2.31766 * T
L4 = -12338.84 + 1.54236 * T

L_hcp = -7148.79 + 0.89361 * T
R = 8.314

def gibbs_solution(G_phase1 , G_phase2 , exchange , T) :
	temp = (1 - x_si) * G_phase1 + x_si * G_phase2 + R * T * ((1 - x_si) * np.log(1 - x_si) + x_si * np.log(x_si))
	gex = 0
	
	for idx , i in enumerate(exchange) :
		gex += i * (1 - 2 * x_si) ** idx
	
	temp += gex * x_si * (1 - x_si)
	return np.round(temp , 1)

def slope(y) :
	return np.diff(y)

def tangent(phase) :
	def line_eqn(x , y , y1 , x1) :
		slope = (np.diff(y)[np.where(x == x1)] / dx)
		intercept = -slope * x1 + y1
		return round(slope[0] , 1) , round(intercept[0] , 1)
	
	tangent_list = []
	for idx , i in enumerate(phase) :
		if idx == len(x_si) - 1 :
			continue
		if idx == 0 :
			continue
		
		tangent_list.append(line_eqn(x_si , phase , i , x_si[idx]))
	
	return tangent_list

def two_point_line(point1 , point2) :
	return [(point1[1] - point2[1]) / (point1[0] - point2[0])] * (x_si - point1[0]) + point1[1]

G_liquid = []
G_hcp = []
for i in range(N) :
	G_liquid.append(gibbs_solution(G_liquid_mg[i] , G_liquid_Si[i] , [Lo[i] , L1[i] , L2[i] , L3[i]] , T[i]))
	G_hcp.append(gibbs_solution(G_hcp_mg[i] , G_diamond_Si[i] , [L_hcp[i]] , T[i]))

# for temp, temp_value in enumerate(T):
# 	plt.plot(x_si, G_hcp[temp], c= 'black')
# 	plt.plot(x_si, G_liquid[temp], c= 'red')
# 	plt.scatter(0.33, G_Mg2Si[temp], c= 'orange')
# 	plt.scatter(1, G_diamond_Si[temp], c = 'blue')
# 	plt.legend(['$alpha$', 'L', '$Mg_{2}Si$', '$Si_{diamond}$'])
# 	plt.title(f"T={temp_value - 273} $C^o$")
# 	plt.ylabel("G (kJ/mol)")
# 	plt.xlabel("$x_{Si}$")
# 	plt.yticks(rotation = 45)
# 	plt.show()
	


tolerance = 20
energy_tolerance = 1
comp_temp = []
tangent_info = {}
points = {}
for temp , temp_value in enumerate(T) :
	
	# find tangent of curves
	tangent_hcp = np.array(tangent(G_hcp[temp]))
	tangent_liquid = np.array(tangent(G_liquid[temp]))
	
	
	# common tangent between liquid and solid with Mg2si
	if G_Mg2Si[temp] <= G_hcp[temp][329] and G_Mg2Si[temp] <= G_liquid[temp][329]:
		
		y_mg2si_liquid = np.round(abs(tangent_liquid[: , 0] * 0.33 + tangent_liquid[: , 1] - G_Mg2Si[temp]) , 2)
		y_mg2si_solid = np.round(abs(tangent_hcp[: , 0] * 0.33 + tangent_hcp[: , 1] - G_Mg2Si[temp]) , 2)
		cond_mg2si_liquid = np.argwhere(y_mg2si_liquid < tolerance).flatten()
		cond_mg2si_solid = np.argwhere(y_mg2si_solid < tolerance).flatten()
		tangent_points_mg2si_liquid = cond_mg2si_liquid
		tangent_points_mg2si_solid = cond_mg2si_solid
	
	else :
		tangent_points_mg2si_liquid = ["no"]
		tangent_points_mg2si_solid = ["no"]
	
	# common tangent between liquid and solid with Si
	if True:
		y_si_liquid = np.round(abs(tangent_liquid[: , 0] * 1 + tangent_liquid[: , 1] - G_diamond_Si[temp]) , 2)
		cond_si_liquid = np.argwhere(y_si_liquid < tolerance).flatten()
		tangent_points_si_liquid = cond_si_liquid
	else :
		tangent_points_si_liquid = ["no"]
	
	# line between Mg2Si and Si
	
	
	comb_slope = np.round(np.array(np.meshgrid(tangent_hcp[: , 0] , tangent_liquid[: , 0])).T.reshape(-1 , 2) , 2)
	comb_intercept = np.round(np.array(np.meshgrid(tangent_hcp[: , 1] , tangent_liquid[: , 1])).T.reshape(-1 , 2) , 2)
	
	diff_slope = abs(comb_slope[: , 0] - comb_slope[: , 1])
	diff_intercept = abs(comb_intercept[: , 0] - comb_intercept[: , 1])
	slope_cond = np.argwhere(diff_slope < tolerance / 10).flatten()
	intercept_cond = np.argwhere(diff_intercept < tolerance).flatten()
	final = np.intersect1d(slope_cond , intercept_cond , assume_unique = True)
	
	# print(
	# 		f"T: {np.round(temp_value - 273 , 2)}, Si-liquid: {tangent_points_si_liquid}, "
	# 		f"Mg2Si-solid: {tangent_points_mg2si_solid}, Mg2Si_liquid: {tangent_points_mg2si_liquid},"
	# 		f"hcp_liquid:{final}"
	# 		)
	points[temp] = {
			'hcp-liquid' : [],
			'si-liquid' : [],
			'mg2si-si': [],
			'mg2si-solid': [],
			'mg2si-liquid': [],
			}
	
	if final.size != 0:
		tangent_hcp_liquid = []
		for i in final :
			point1 = np.argwhere(tangent_hcp == comb_slope[i][0]).flatten()[0]
			point2 = np.argwhere(tangent_liquid == comb_slope[i][1]).flatten()[0]
			
			points[temp]["hcp-liquid"].append([point1, point2])
			
			tangent_hcp_liquid.append(
				two_point_line(
						(x_si[point1] , G_hcp[temp][point1]) , (x_si[point2] , G_liquid[temp][
							point2])
						)
				)
	else:
		tangent_hcp_liquid = ["no"]
		
	if tangent_points_si_liquid != [] and "no" not in tangent_points_si_liquid:
		
		tangent_si_liquid = []
		for i in tangent_points_si_liquid :
			points[temp]["si-liquid"].append([1, i])
			tangent_si_liquid.append(two_point_line((1 , G_diamond_Si[temp]) , (x_si[i] , G_liquid[temp][i])))
	else:
		tangent_si_liquid = ["no"]
	if tangent_points_mg2si_liquid != [] and "no" not in tangent_points_mg2si_liquid:
		tangent_mg2si_liquid = []
		for i in tangent_points_mg2si_liquid :
			points[temp]["mg2si-liquid"].append([0.33 , i])
			tangent_si_liquid.append(two_point_line((0.33 , G_Mg2Si[temp]) , (x_si[i] , G_liquid[temp][i])))
	else:
		tangent_mg2si_liquid = ["no"]
	if tangent_points_mg2si_solid != [] and "no" not in tangent_points_mg2si_solid:
		tangent_mg2si_solid = []
		for i in tangent_points_mg2si_solid :
			points[temp]["mg2si-solid"].append([0.33 , i])
			tangent_mg2si_solid.append(two_point_line((0.33 , G_Mg2Si[temp]) , (x_si[i] , G_hcp[temp][i])))
	else:
		tangent_mg2si_solid = ["no"]
	
	slope_mg2si_si = (G_diamond_Si[temp] - G_Mg2Si[temp]) / (1 - 0.3333)
	points[temp]["mg2si-si"].append([0.33, 1])
	# print(points[temp])
	
	tangent_info[temp] = {
			'hcp_liquid': tangent_hcp_liquid,
			'mg2si_liquid': tangent_mg2si_liquid,
			'mg2si_solid': tangent_mg2si_solid,
			'si_liquid': tangent_si_liquid,
			'mg2si_si': slope_mg2si_si * (x_si - 0.33) + G_Mg2Si[temp]
			}
temp_arr = []
comp_values_total = []
count = 0
for temp, temp_value in enumerate(T):
	comp_values = []
	for keys, values in points[temp].items():
		np_values = np.array(values).flatten()
		if np_values.size != 0:
			count +=1
			if 1.0 in np_values or 0.33 in np_values:
				if 0.33 not in np_values:
					np_values = np_values[np_values != 1].astype(int)
					comp_values += list(np.unique(np.round(x_si[np_values] , 2)))
				elif 1.0 not in np_values:
					np_values = np_values[np_values != 0.33].astype(int)
					comp_values += list(np.unique(np.round(x_si[np_values] , 2)))
				else:
					comp_values += list(np_values)
			else:
				comp_values += list(np.unique(np.round(x_si[np_values] , 2)))
		
			temp_arr.append(temp_value)
	
	comp_values_total.append(comp_values)


for idx, comp_value in enumerate(comp_values_total):
	plt.scatter(comp_value, [T[idx]-273]*len(comp_value), c = 'black', marker='.')
#
plt.ylim(400, 1500)
plt.xlim([0, 1])
plt.show()
# for temp , temp_value in enumerate(T) :
# 	if "no" not in tangent_info[temp]['hcp_liquid']:
# 		for i in tangent_info[temp]['hcp_liquid']:
# 			if "no" not in i:
# 				plt.plot(x_si , i , c = 'black')
# 	if "no" not in tangent_info[temp]['mg2si_liquid'] :
# 		for i in tangent_info[temp]['mg2si_liquid']:
# 			plt.plot(x_si , i , c = 'black')
# 	if "no" not in tangent_info[temp]['mg2si_solid'] :
# 		for i in tangent_info[temp]['mg2si_solid']:
# 			plt.plot(x_si , i , c = 'black')
# 	if "no" not in tangent_info[temp]['si_liquid'] :
# 		for i in tangent_info[temp]['si_liquid']:
# 			plt.plot(x_si , i , c = 'black')
# 	if "no" not in tangent_info[temp]['mg2si_si']:
# 		plt.plot(x_si , tangent_info[temp]['mg2si_si'] , c = 'black')
#
# 		plt.plot(x_si , G_liquid[temp] , c = 'red')
# 		plt.plot(x_si , G_hcp[temp] , c = 'red')
# 		plt.scatter(0.33 , G_Mg2Si[temp] , c = 'orange')
# 		plt.scatter(1 , G_diamond_Si[temp] , c = 'orange')
# 		plt.title(f"T = {round(temp_value , 2) - 273} C")
# 		plt.show()
#
# temp_values = []
# point1, point2 = [], []
# for key, value in tangent_info.items():
# 	if value != 'No common tangent':
# 		temp_values.append(T[key]-273.15)
# 		point1.append(x_si[value['point1']])
# 		point2.append(x_si[value['point2']])

# plt.scatter(point1, temp_values)
# plt.scatter(point2, temp_values)
# plt.ylim(400, 2000)
# plt.xlim(0, 1)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

for dope in [0, 0.05, 0.1, 0.15, 0.2]:
	do = np.array([0.688 ,0.684 ,0.669 ,0.666 ,0.660])
	dt = np.array([0.555 ,0.553 , 0.564 , 0.564 , 0.566])
	p0_sa = 67
	p0_si = 53
	pt_sa = p0_sa*do/do[0]
	pt_si = p0_si*dt/dt[0]
	doping = [0, 0.05, 0.1, 0.15, 0.2]
	ind = doping.index(dope)
	x_sa = np.linspace(-1.5, 1.5, 19)
	x_si = np.linspace(-1.5, 1.5, 19)
	p42nmc = {
			0    : [174 , 64 , 6 , -10 , 2 , 23 , 39 , 36 , 16 , 0 , 16 , 36 , 39 , 23 , 2 , -10 , 6 , 64 , 174] ,
			0.05 : [197 , 79 , 18 , 3 , 15 , 37 , 51 , 44 , 18 , 0 , 18 , 44 , 51 , 37 , 15 , 3 , 18 , 79 , 197] ,
			0.1  : [264 , 120 , 47 , 27 , 40 , 63 , 76 , 64 , 28 , 0 , 28 , 64 , 76 , 63 , 40 , 27 , 47 , 120 , 264] ,
			0.15 : [394 , 181 ,73 ,44 ,62 ,93 ,111 ,93 ,40 ,0 ,40 ,93 ,111 ,93 ,62 ,44 ,73 ,181 ,394] ,
			0.2  : [476 ,252 ,137 ,108 ,127 ,157 ,167 ,130 ,53 ,0 ,53 ,130 ,167 ,157 ,127 ,108 ,137 ,252 ,476]
			}
	
	pbcm = {
			0    : [44 ,-61 ,-116 ,-133 ,-120 ,-90 ,-55 ,-25 ,-6 ,0 ,-6 ,-25 ,-55 ,-90 ,-120 ,-133 ,-116 ,-61 ,44],
			0.05 : [72 ,-28 ,-83 ,-99 ,-87 ,-58 ,-30 ,-10 ,-1 ,0 ,-1 ,-10 ,-30 ,-58 ,-87 ,-99 ,-83 ,-28 ,72] ,
			0.1  : [138 ,33 ,-25 ,-41 ,-28 ,-4 ,11 ,13 ,6 ,0 ,6 ,13 ,11 ,-4 ,-28 ,-41 ,-25 ,33 ,138] ,
			0.15 : [240 ,121 ,56 ,39 ,52 ,67 ,63 ,41 ,14 ,0 ,14 ,41 ,63 ,67 ,52 ,39 ,56 ,121 ,240] ,
			0.2  : [384 ,239 ,160 ,139 ,152 ,159 ,134 ,81 ,25 ,0 ,25 ,81 ,134 ,159 ,152 ,139 ,160 ,239 ,384]
			}
	
	y_sa = pbcm[dope]
	y_si = p42nmc[dope]
	polar = -4
	y_sa = [i - y_sa[polar] for i in y_sa]
	y_si = [i - y_si[polar] for i in y_si]
	
	def polyfit(x, y, deg):
		
		coeff = np.polyfit(x , y , deg = deg)
		f = np.poly1d(coeff)
		df = f.deriv()
		y_c = f(x)
		print(np.around(coeff, decimals = 8))
		return y_c, df
	
	y_c_si, df_si = polyfit(x_si, y_si, 8)
	y_c_sa, df_sa = polyfit(x_sa, y_sa, 8)
	
	print(f"Pbcm max slope: {max(df_sa(x_sa)[3:-4])}, P42nmc max slope: {max(df_si(x_si)[3:-4])}")
	plt.plot(x_sa, y_c_sa, c = 'red')
	plt.scatter(x_sa, y_sa, c = 'red')
	plt.plot(x_si, y_c_si, c = 'blue')
	plt.scatter(x_si, y_si, c = 'blue')
	# plt.plot(x_sa,df_sa(x_sa), c = "red")
	# plt.plot(x_si,df_si(x_si), c = "blue")
	# plt.show()

import matplotlib.pyplot as plt

holes = [0, 0.1, 0.2, 0.3, 0.4]
holes_zro = [0, 0.05, 0.1, 0.15, 0.2]
fontsize = 10

zro = {
		'$P4_{2}/nmc$': [0, 0, 0, 0, 0],
		'$Pca2_{1}$': [-10, 45, 114, -204, -421],
		'$Pbcm$': [122, 85, -29, -204, -421],
		
		}
bfo = {
		'$Pnma$': [0, 0, 0, 0, 0],
		'$Pm3m$': [902, 923, 778, 659, 520],
		'$R3c$': [- 30, 86, 100, 89, 57],
		}
stable_zro = [-10, 0, -29, -204, -421]
for keys, value in zro.items():
	zro[keys] =  [value[i] - zro['$Pca2_{1}$'][i] for i in range(len(value))]
# fig, ax = plt.subplots(figsize=(10, 6))
# phase = '$P4_{2}/nmc$'
# # Customize scatter plot appearance
# for key, value in disp[phase].items():
# 	y = value
# 	ax.plot(holes_zro, y, alpha=0.7, marker = '^')

# Add labels and title
fig , (ax1 , ax2) = plt.subplots(2 , 1 , figsize = (5 ,12))
fig.subplots_adjust(wspace = 0.1)
# Customize the first panel (ax1)
ax1.set_xticks(holes)
ax1.plot(
		holes , zro['$P4_{2}/nmc$'] , marker = 'o' , color = '#44BB99' , linestyle = '--' ,
		linewidth = 0.8, alpha = 1
		)

ax1.plot(
		holes , zro['$Pca2_{1}$'], marker = '^' , color = '#77AADD' , linestyle = '--' ,
		linewidth = 0.8, alpha = 1
		)
ax1.plot(
		holes, zro['$Pbcm$'] , marker = '*', ms='10' , color = '#EE8866' , linestyle = '--' ,
		linewidth = 0.8, alpha = 1
		)

ax1.legend(list(zro.keys()), title = '$Phases$' , ncols = 4, bbox_to_anchor = (0.1, 1.0))

# Customize the second panel (ax2)
ax2.plot(
		holes, bfo['$Pnma$'] , marker = 'o' , color = '#EE8866' , linestyle = '--' ,
		linewidth = 1
		)
ax2.plot(
		holes , bfo['$Pm3m$'], marker = '^' , color = '#77AADD' , linestyle = '--' ,
		linewidth = 0.01
		)
ax2.plot(
		holes , bfo['$R3c$'] , marker = '*' ,ms='10', color = '#44BB99' , linestyle = '--' ,
		linewidth = 0.01
		)
ax1.set_ylabel('Energy (meV/f.u.)')
ax1.set_xlabel('Holes/f.u.')
# ax2.legend(list(bfo.keys()), title = '$Phases$' , ncols = 4, bbox_to_anchor = (0.1, 1.0))

fig.supxlabel('Holes/f.u.', fontsize =fontsize)

# Adjust the spacing between subplots


# Save or display the plot
plt.savefig('/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/fig1a.png', dpi=100,
            bbox_inches='tight')
plt.show()

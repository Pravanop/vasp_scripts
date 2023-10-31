import matplotlib.pyplot as plt

holes = [0, 0.1, 0.2, 0.3]
holes_zro = [0, 0.05, 0.1, 0.15, 0.2]

disp = {'$Pnma$': {
		'$R_{5}^{-}$': [0.73, 0.71, 0.70, 0.69],
		'$X_{5}^{-}$': [0.32, 0.32, 0.31, 0.305],
		'$M_{2}^{+}$': [0.58, 0.57, 0.57, 0.57]
		},
		'$R3c$': {
				'$R_{5}^{-}$': [0.69, 0.72, 0.70, 0.69],
				'$\Gamma_{4}$': [0.51, 0.46, 0.4, 0.34],
				},
		'$P4mm$': {
				'$\Gamma_{4}$':[0.7495, 0.6851, 0.616, 0.5262]
				},
		'$P4_{2}/nmc$': {
				'$\Gamma_{4}$': [0.24,	0.24,	0.24,	0.25, 0.25],
				'$X_{5}^{+}$': [0.67,	0.67,	0.68,	0.69, 0.69],
				'$X_{2}^{-}$': [0.47,	0.47,	0.47,	0.47, 0.47],
				'$X_{5}^{-}$': [0.20,	0.19,	0.19,	0.19, 0.19],
				'$X_{3}^{-}$': [0.09,	0.10,	0.10,	0.11, 0.11],
				},
		'$Pbcm$': {
				'$\Gamma_{2}$': [0.68 ,  0.66,   0.63,  0.61, 0.59]
				}
		}

# fig, ax = plt.subplots(figsize=(10, 6))
# phase = '$P4_{2}/nmc$'
# # Customize scatter plot appearance
# for key, value in disp[phase].items():
# 	y = value
# 	ax.plot(holes_zro, y, alpha=0.7, marker = '^')

# Add labels and title
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey = True, sharex = True)
fig.subplots_adjust(wspace=0)
phase = '$Pnma$'
# Customize the first panel (ax1)
ax1.set_xticks(holes)
# ax1.plot(holes_zro, disp['$Pnma$']['$\Gamma_{4}$'], marker = '^', color='#EE8866', linestyle='-.',
#          linewidth=1)
ax1.plot(holes, disp[phase]['$R_{5}^{-}$'], marker = 'o', color='#77AADD', linestyle='-.', linewidth=1)
ax1.plot(holes, disp[phase]['$X_{5}^{-}$'], ms = 8, marker = '*', color='#44BB99', linestyle='-.', linewidth=1)
ax1.plot(holes, disp[phase]['$M_{2}^{+}$'], ms = 8, marker = '*', color='#EE7733', linestyle='-.', linewidth=1)
# ax1.plot(holes, disp['$Pnma$']['$M_{2}^{+}$'], marker = 's', color='#AA4499', linestyle='-.', linewidth=1)
# ax1.plot(holes_zro, disp['$P4_{2}/nmc$']['$X_{5}^{-}$'], marker = '^', color='#228833', linestyle='-', linewidth=1)
ax1.legend(list(disp[phase].keys()), loc = 'right', title=f'Modes for {phase}', ncols = 4,
           bbox_to_anchor = (.65, 1.10), fontsize = 10)
phase = '$R3c$'
# Customize the second panel (ax2)
ax2.plot(holes, disp[phase]['$R_{5}^{-}$'], marker = 'o', color='#77AADD', linestyle='--', linewidth=1)
ax2.plot(holes, disp[phase]['$\Gamma_{4}$'], marker = 'o', color='#44BB99', linestyle='--', linewidth=1)
# ax2.plot(holes, disp['$R3c$']['$\Gamma_{4}$'], marker = '^', color='#EE8866', linestyle='--', linewidth=1)
# ax2.set_xlabel('Holes/f.u.')
ax2.legend(list(disp[phase].keys()), loc = 'right', title=f'Modes for {phase}', ncols = 4,
           bbox_to_anchor = (.65, 1.10), fontsize = 10)


ax1.set_ylabel('Normalized Mode Amplitude ($\AA$)', fontsize = 10, )
fig.supxlabel('Holes/f.u.', fontsize = 10)

# Adjust the spacing between subplots


# Save or display the plot
plt.savefig('/Users/pravanomprakash/Library/CloudStorage/Box-Box/Charge Doping/Figures/Modes_BFO.png', dpi=100,
            bbox_inches='tight')
plt.show()






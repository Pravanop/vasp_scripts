from pymatgen.io import vasp
import matplotlib.pyplot as plt

loc = vasp.Locpot.from_file("/Users/pravanomprakash/Downloads/LOCPOT")
print(len(loc.get_average_along_axis(0)))
plt.plot(loc.get_average_along_axis(2))
plt.title('Z-axis')
# print(loc.get_average_along_axis(2))
plt.show()

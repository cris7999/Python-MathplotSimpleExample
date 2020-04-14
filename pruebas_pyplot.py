
import matplotlib.pyplot as plt

anno = [1950,1960,1970,1980,1990, 2000,2010,2020]
poblacion = [2.5,3.04,3.7,4.45,5.32,6.14,6.95,7.79]


#Annadir datos de 1850 y 1900, 1.2 y 1.6

anno += [1850,1900]
poblacion = [1.2,1.6] + poblacion 
anno=sorted(anno)

plt.title("Poblacion mundial")
plt.ylabel("Poblacion")
plt.xticks(anno)
plt.xticks(rotation = 45)
plt.plot(anno,poblacion)
plt.show()
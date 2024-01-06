from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()

objectsManager.saveObject(lista, 'coherence_values_wizz-air_2')

coherence_values = objectsManager.getSavedObject('coherence_values_wizz-air_2')



print(coherence_values)

limit=11; start=1; step=1;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.title("Wizz-Air Cluster_3 Coherence plot")
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()
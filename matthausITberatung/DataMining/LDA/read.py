from matplotlib import pyplot as plt

from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager

objectsManager = ObjectsManager()

lista = [
0.31892893059805333,
0.33905884332747194,
0.30008699080544216,
0.294688596229559,
0.3234355612291152,
0.2932500486380217,
0.30837720905133764,
0.3020909788684398,
0.30813365901765016,
0.3056755442103423
]

objectsManager.saveObject(lista, 'coherence_values_ryanair_2')

coherence_values = objectsManager.getSavedObject('coherence_values_ryanair_2')



print(coherence_values)

limit=11; start=1; step=1;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.title("Ryanair Cluster_3 Coherence plot")
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()
from matplotlib import pyplot as plt
from matthausITberatung.objectsManager.ObjectsManager import ObjectsManager
from matthausITberatung.objectsManager.PathsManager import PathsManager

objectsManager = ObjectsManager()
pathsManager = PathsManager()

airline = pathsManager.LUFTHANSA
clusterNumber = 0

coherence_values = objectsManager.getSavedObject('coherence_values_'+airline+'_'+str(clusterNumber))

clusterLabel = 'Airports and Operational Aspects'

print(coherence_values)

limit=16; start=1; step=1;
x = range(start, limit, step)
plt.plot(x, coherence_values)
plt.title(airline+' '+clusterLabel+' Coherence plot')
plt.xlabel("Num Topics")
plt.ylabel("Coherence score")
plt.legend(("coherence_values"), loc='best')
plt.show()
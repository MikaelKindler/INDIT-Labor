import numpy as np
import matplotlib.pyplot as plt

#Winkelwerte von 0-360 Grad
angles = np.arange(0, 361)

#Genauigkeit berechnen; Cosinus
accuracy = np.cos(np.deg2rad(angles))

#Plot erstellen
plt.plot(angles, accuracy)
plt.title("Genauigkeit in Winkelgrad")
plt.xlabel("Winkel in Grad")
plt.ylabel("Genauigkeit")
plt.grid(True)
plt.show()

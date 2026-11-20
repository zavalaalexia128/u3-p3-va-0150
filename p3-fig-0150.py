import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import cv2

## Zavala Medina | NC= 0150
print("Zavala Medina| NC= 0150")
print("UIII Act3 colocar puntos a una imagen en blanco y negro VA")

mi_imagen = cv2.imread("Michealjackson.jpg")
mi_imagen_rgb = cv2.cvtColor(mi_imagen, cv2.COLOR_BGR2RGB)

plt.imshow(mi_imagen_rgb)
plt.title("Micheal Jackson y Zavala Medina")
plt.show()

print("+-+- Puntos en la imagen -+-+")

plt.imshow(mi_imagen_rgb)
plt.title("Imagen con Puntos 0150")

x = [100, 100, 300]
y = [100, 400, 500]
plt.scatter(x, y, s=20, c="red")
plt.show()
print("+-+- cuadro en la imagen -+-+")
img_micheal = cv2.imread("Michealjackson.jpg")
img_micheal_rgb = cv2.cvtColor(img_micheal, cv2.COLOR_BGR2RGB)

plt.imshow(img_micheal_rgb)
plt.title("Imagen con Cuadro 0150")
x = [50, 50, 300, 300, 50]
y = [450, 50, 50, 450, 450]

plt.plot(x, y, c="blue")
plt.show()

print("+-+- circulo en la imagen -+-+")
I = cv2.imread("Michealjackson.jpg")
I_rgb = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
plt.imshow(I_rgb)

N = 50 # Aumentado ligeramente para que el círculo se vea más suave
x = np.zeros((N+1,))
y = np.zeros((N+1,))

# Centro y radio ajustados exactamente a la cara de Michael Jackson
(xc, yc) = (148, 142)
r = 22  # radio
plt.title("Imagen con Circulo 0150")
for i in range(N+1):
    t = 2*np.pi/N * i
    x[i] = xc + r*np.cos(t)
    y[i] = yc + r*np.sin(t)

plt.plot(x, y, c="red", linewidth=2)
plt.show()
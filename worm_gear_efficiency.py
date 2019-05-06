from math import cos, tan, pi, radians, degrees
import numpy as np
import matplotlib.pyplot as plt

phi_n = radians(20) # Normal pressure angle = 20°
mu_values = [0.02, 0.04, 0.06] # Coeficient friction values
lead_angles = np.linspace(1, 60, 100) # in degrees

for mu in mu_values:
    eff = [
        (
            (cos(phi_n) - mu * tan(radians(lead_angle))) /
            (cos(phi_n) + mu / tan(radians(lead_angle)))
        ) * 100 for lead_angle in lead_angles
    ]
    plt.plot(lead_angles, eff, label=f'\u03BC={mu}')

plt.title("Eficiencia de la transmisión tornillo sinfín y corona")
plt.ylim(bottom=0, top=100)
plt.grid(True)
plt.xlabel('Ángulo de avance, \u03BB (grados)')
plt.ylabel('Eficiencia, \u03B7 (%)')
plt.text(30, 10, f'\u03A6\u2099 = {degrees(phi_n)}°')
plt.legend()
plt.show()

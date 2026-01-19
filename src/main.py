import numpy as np
import matplotlib.pyplot as plt

from envelope_protection import EnvelopeProtection
from aircraft_model import AircraftModel
from simulation import run_simulation

dt = 0.01
t = np.arange(0, 10, dt)

pilot_cmd = np.zeros_like(t)
pilot_cmd[t > 1.0] = 18.0  # aggressive pitch-up

protection = EnvelopeProtection()
aircraft = AircraftModel()

pitch, alpha, protected_cmd = run_simulation(
    protection, aircraft, pilot_cmd, t, dt
)

plt.figure(figsize=(10, 6))
plt.plot(t, pilot_cmd, '--', label="Pilot Command")
plt.plot(t, protected_cmd, label="Protected Command")
plt.plot(t, alpha, label="Angle of Attack")
plt.axhline(12.0, color='r', linestyle=':', label="AoA Limit")

plt.xlabel("Time (s)")
plt.ylabel("Degrees")
plt.title("Flight Envelope Protection System")
plt.legend()
plt.grid()
plt.savefig("plots/envelope_protection.png")
plt.show()
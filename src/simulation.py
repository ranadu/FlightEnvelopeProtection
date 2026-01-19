import numpy as np

def run_simulation(protection, aircraft, pilot_cmd, t, dt):
    pitch = []
    alpha = []
    protected_cmd = []

    prev_pitch = 0.0

    for cmd in pilot_cmd:
        pitch_rate = (aircraft.pitch - prev_pitch) / dt

        safe_cmd = protection.protect(
            cmd, aircraft.alpha, pitch_rate, aircraft.pitch
        )

        prev_pitch = aircraft.pitch
        p, a, _ = aircraft.update(safe_cmd, dt)

        pitch.append(p)
        alpha.append(a)
        protected_cmd.append(safe_cmd)

    return np.array(pitch), np.array(alpha), np.array(protected_cmd)
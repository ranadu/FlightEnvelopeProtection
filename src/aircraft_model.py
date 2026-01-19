class AircraftModel:
    def __init__(self, k_pitch=1.5, k_alpha=0.8):
        self.k_pitch = k_pitch
        self.k_alpha = k_alpha
        self.pitch = 0.0
        self.alpha = 0.0

    def update(self, pitch_cmd, dt):
        pitch_dot = self.k_pitch * (pitch_cmd - self.pitch)
        self.pitch += pitch_dot * dt

        alpha_dot = self.k_alpha * (self.pitch - self.alpha)
        self.alpha += alpha_dot * dt

        return self.pitch, self.alpha, pitch_dot
import numpy as np

class EnvelopeProtection:
    def __init__(self, alpha_max=12.0, pitch_rate_max=20.0):
        self.alpha_max = alpha_max
        self.pitch_rate_max = pitch_rate_max
    
    def protect(self, pilot_cmd, alpha, pitch_rate, current_pitch):
        cmd = pilot_cmd

    # Smooth AoA protection (soft saturation)
        aoa_error = max(0.0, alpha - self.alpha_max)
        cmd -= 5.0 * aoa_error  # feedback gain
    
    # Pitch rate protection
        if abs(pitch_rate) > self.pitch_rate_max:
         cmd = current_pitch

        return cmd
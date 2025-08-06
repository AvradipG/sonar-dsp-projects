
import numpy as np

def steering_vector(N, d, wavelength, theta_deg):
    theta_rad = np.radians(theta_deg)
    n = np.arange(N)
    return np.exp(-1j * 2 * np.pi * d * n * np.sin(theta_rad) / wavelength)

def compute_array_response(weights, sv):
    return np.abs(np.dot(weights.conj().T, sv))

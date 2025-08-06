
import numpy as np

def db_scale(x, eps=1e-12):
    return 10 * np.log10(np.abs(x)**2 + eps)

def normalize(signal):
    return signal / np.max(np.abs(signal)) if np.max(np.abs(signal)) > 0 else signal

def compute_snr(signal, noise_floor=1e-12):
    power_signal = np.mean(np.abs(signal)**2)
    return 10 * np.log10(power_signal / noise_floor)

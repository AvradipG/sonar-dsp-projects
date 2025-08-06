
import numpy as np
from scipy.signal import correlate

def matched_filter(received_signal, reference_waveform):
    """Applies matched filtering by correlating the received signal with reference."""
    matched_output = correlate(received_signal, reference_waveform.conj(), mode='full')
    return matched_output

def compute_snr(signal, noise_floor=None):
    """Computes Signal-to-Noise Ratio (SNR) in dB."""
    power_signal = np.mean(np.abs(signal)**2)
    if noise_floor is None:
        noise_floor = 1e-12
    return 10 * np.log10(power_signal / noise_floor)

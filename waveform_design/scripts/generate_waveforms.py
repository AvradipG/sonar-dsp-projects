
import numpy as np

def generate_lfm_chirp(duration, fs, f0, f1):
    """Generates a Linear Frequency Modulated (LFM) chirp."""
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    k = (f1 - f0) / duration
    phase = 2 * np.pi * (f0 * t + 0.5 * k * t**2)
    return t, np.exp(1j * phase)

def generate_barker_code(code):
    """Generates a waveform from a given Barker code sequence."""
    return np.array(code, dtype=np.float32)

def generate_step_fm_waveform(duration, fs, freqs):
    """Generates a Step-FM waveform with given step frequencies."""
    n_steps = len(freqs)
    step_duration = duration / n_steps
    samples_per_step = int(fs * step_duration)
    waveform = np.array([], dtype=np.complex64)

    for f in freqs:
        t = np.linspace(0, step_duration, samples_per_step, endpoint=False)
        wave = np.exp(1j * 2 * np.pi * f * t)
        waveform = np.concatenate((waveform, wave))

    return waveform


import numpy as np

def generate_chirp(fs, duration, f_start, f_end):
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    chirp_signal = np.sin(2 * np.pi * (f_start + (f_end - f_start) * t / duration) * t)
    return t, chirp_signal

def create_array_signals(chirp, fs, array_length, doa_deg, sound_speed=1500):
    N_sensors = array_length
    f_avg = 0.5 * (2000 + 6000)
    wavelength = sound_speed / f_avg
    d = wavelength / 2
    doa_rad = np.deg2rad(doa_deg)

    delays = np.array([n * d * np.sin(doa_rad) / sound_speed for n in range(N_sensors)])
    sample_delays = np.round(delays * fs).astype(int)

    sensor_signals = []
    for delay in sample_delays:
        delayed = np.pad(chirp, (delay, 0), mode='constant')[:len(chirp)]
        sensor_signals.append(delayed)
    return np.array(sensor_signals)



def delay_and_sum(signals, fs, angles_deg, d, sound_speed=1500):
    """
    Compute beamformed output for a range of look directions.
    """
    n_sensors, n_samples = signals.shape
    angles_rad = np.deg2rad(angles_deg)
    beam_output = []

    for theta in angles_rad:
        delays = np.array([i * d * np.sin(theta) / sound_speed for i in range(n_sensors)])
        sample_delays = np.round(delays * fs).astype(int)

        aligned = []
        for i, delay in enumerate(sample_delays):
            shifted = np.pad(signals[i], (max(0, delay), 0), mode='constant')[:n_samples]
            aligned.append(shifted)
        summed = np.sum(aligned, axis=0)
        power = np.sum(summed ** 2)
        beam_output.append(power)
    
    return np.array(beam_output)

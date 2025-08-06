import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io import wavfile

def apply_lowpass_filter(data, fs, cutoff=100, order=4, ftype='iir'):
    if ftype == 'iir':
        b, a = signal.butter(order, cutoff, fs=fs, btype='low')
        return signal.filtfilt(b, a, data)
    elif ftype == 'fir':
        numtaps = 101
        taps = signal.firwin(numtaps, cutoff, fs=fs)
        return signal.lfilter(taps, 1.0, data)
    else:
        raise ValueError("Filter type must be 'iir' or 'fir'")

# Example usage
if __name__ == "__main__":
    fs = 1000
    t = np.linspace(0, 1.0, fs)
    sig = np.sin(2 * np.pi * 50 * t) + np.random.normal(0, 0.5, fs)

    filtered = apply_lowpass_filter(sig, fs, cutoff=100, ftype='iir')

    plt.plot(t, sig, label='Noisy')
    plt.plot(t, filtered, label='Filtered')
    plt.legend()
    plt.title("Filtering with IIR")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

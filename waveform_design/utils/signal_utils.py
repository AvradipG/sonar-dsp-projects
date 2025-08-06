
import numpy as np
import matplotlib.pyplot as plt

def plot_time_domain(t, signal, title="Signal in Time Domain", xlabel="Time (s)", ylabel="Amplitude"):
    plt.figure(figsize=(10, 4))
    plt.plot(t, np.real(signal), label='Real')
    plt.plot(t, np.imag(signal), label='Imaginary', linestyle='--')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_frequency_domain(signal, fs, title="Frequency Spectrum", log_scale=False):
    N = len(signal)
    freqs = np.fft.fftfreq(N, d=1/fs)
    spectrum = np.fft.fft(signal)
    magnitude = np.abs(spectrum)

    plt.figure(figsize=(10, 4))
    if log_scale:
        plt.semilogy(freqs[:N//2], magnitude[:N//2])
    else:
        plt.plot(freqs[:N//2], magnitude[:N//2])
    plt.title(title)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def db_scale(x, eps=1e-12):
    return 10 * np.log10(np.abs(x)**2 + eps)

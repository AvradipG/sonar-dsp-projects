import numpy as np
import pywt
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def wavelet_denoise(signal, wavelet='db4', level=4, threshold=0.4):
    coeffs = pywt.wavedec(signal, wavelet, level=level)
    coeffs_thresh = [pywt.threshold(c, threshold, mode='soft') if i > 0 else c for i, c in enumerate(coeffs)]
    return pywt.waverec(coeffs_thresh, wavelet)

def lowpass_filter(signal, fs, cutoff=100):
    b, a = butter(4, cutoff / (0.5 * fs), btype='low')
    return filtfilt(b, a, signal)

if __name__ == "__main__":
    fs = 1000
    t = np.linspace(0, 1, fs)
    clean = np.sin(2*np.pi*50*t)
    noise = np.random.normal(0, 0.5, fs)
    noisy = clean + noise

    wavelet_d = wavelet_denoise(noisy)
    lowpass_d = lowpass_filter(noisy, fs)

    plt.figure(figsize=(12, 6))
    plt.plot(t, noisy, label='Noisy', alpha=0.5)
    plt.plot(t, clean, label='Clean')
    plt.plot(t, wavelet_d[:len(t)], label='Wavelet Denoised', linestyle='--')
    plt.plot(t, lowpass_d, label='Low-pass Filtered', linestyle='-.')
    plt.legend()
    plt.grid(True)
    plt.title('Wavelet vs Low-pass Denoising')
    plt.show()

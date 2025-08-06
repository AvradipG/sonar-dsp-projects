import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

st.title("Time-Frequency Visualizer (FFT + Gabor Transform)")

uploaded_file = st.file_uploader("Upload a WAV file", type=["wav"])

if uploaded_file is not None:
    fs, data = wavfile.read(uploaded_file)
    if data.ndim > 1:
        data = data[:, 0]

    st.write(f"Sample Rate: {fs} Hz")

    # FFT
    st.subheader("FFT")
    f_fft = np.fft.rfftfreq(len(data), 1/fs)
    fft_vals = np.abs(np.fft.rfft(data))
    fig_fft, ax_fft = plt.subplots()
    ax_fft.plot(f_fft, fft_vals)
    ax_fft.set_title("FFT of Signal")
    ax_fft.set_xlabel("Frequency (Hz)")
    ax_fft.set_ylabel("Magnitude")
    ax_fft.grid(True)
    st.pyplot(fig_fft)

    # Gabor Spectrogram
    st.subheader("Gabor Spectrogram")
    std = st.slider("Gaussian window std dev", 10, 100, 50)
    nperseg = st.slider("Window length (nperseg)", 64, 512, 128)
    noverlap = st.slider("Overlap", 0, nperseg - 1, nperseg // 2)

    f, t_spec, Sxx = signal.spectrogram(data, fs, window=('gaussian', std), nperseg=nperseg, noverlap=noverlap)
    fig_spec, ax_spec = plt.subplots()
    pcm = ax_spec.pcolormesh(t_spec, f, 10*np.log10(Sxx), shading='gouraud')
    ax_spec.set_title("Gabor Spectrogram")
    ax_spec.set_xlabel("Time (s)")
    ax_spec.set_ylabel("Frequency (Hz)")
    fig_spec.colorbar(pcm, ax=ax_spec, label='Power/Frequency (dB/Hz)')
    st.pyplot(fig_spec)

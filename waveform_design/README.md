# Waveform Design for Sonar DSP

This module covers theoretical and practical aspects of waveform design in sonar and signal processing systems.

## 🔍 Topics Covered

- Theory of waveform design (chirps, codes, time-bandwidth product)
- LFM (chirp) signal generation
- Barker code generation and matched filtering
- Ambiguity function analysis
- Time-frequency plots (spectrogram, FFT)
- Matched filter SNR analysis

## 📂 Structure

| Folder | Content |
|--------|---------|
| `notebooks/` | Theory notebooks with simulations |
| `scripts/`   | Python modules for waveform generation & filtering |
| `data/`      | Example .wav and .npy waveforms |
| `figures/`   | Plots: ambiguity functions, spectrograms |
| `utils/`     | Helper functions (e.g., SNR, plotting) |

## 🧪 How to Run

```bash
pip install -r requirements.txt
jupyter notebook notebooks/waveform_design_theory.ipynb
```

## 🛠 Requirements

- numpy
- matplotlib
- scipy
- IPython

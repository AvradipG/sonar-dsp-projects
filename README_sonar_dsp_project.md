# Sonar DSP Projects 🎧🌊

This repository preserves earlier learning projects in signal processing. Avradip Ghosh's current professional focus is digital rock simulation and pore-scale fluid flow.

It covers a full signal processing pipeline using synthetic sonar-like signals, and includes educational notebooks, reusable scripts, and real-time simulations.

---

## 📚 Project Modules

| Module                   | Description |
|--------------------------|-------------|
| `waveform_design/`       | LFM, Barker, and Step-FM waveform generation with ambiguity and time-frequency analysis |
| `beamformer/`            | Delay-and-sum beamforming simulation, array steering, and directional plots |
| `broadband_processing/`  | Comparison of narrowband vs true broadband beamforming techniques |
| `detection/`             | Matched filtering, ROC curves, SNR-based signal detection, and hypothesis testing |
| `sonar_processing/`      | End-to-end sonar pulse → echo → matched filtering pipeline |
| `performance_analysis/`  | Evaluation of algorithm performance using SNR gain and ROC metrics |
| `embedded_integration/`  | Real-time frame-based signal processing emulating an embedded sonar system |

---

## 🔧 Technologies Used

- Python 3
- NumPy, SciPy
- Matplotlib
- scikit-learn (for ROC curves)
- Jupyter Notebooks

---

## 🧠 Learning Objectives

- Understand key sonar/DSP operations: waveform design, beamforming, filtering, detection
- Translate theory into working Python simulations
- Evaluate algorithm performance using practical metrics
- Build DSP pipelines ready for embedded and real-time environments

---

## 📁 Structure

Each module contains:

- `notebooks/`: Educational, self-contained Jupyter notebooks
- `scripts/`: Reusable Python logic (e.g., waveform generation, steering vector)
- `utils/`: Plotting, math helpers
- `figures/`: Optional folder for saved plots
- `README.md`: Module-specific summary

---

## ✅ Goals

- Preserve earlier signal-processing learning work
- Demonstrate signal chain understanding from waveform to detection
- Provide a launching point for real-time and sonar simulation development

---

## 📬 Contact

Earlier learning work by **Avradip Ghosh**, whose current focus is digital rock simulation and fluid flow through porous media.  
📧 [LinkedIn Profile](https://www.linkedin.com/in/avradip-ghosh)

---

> This repo is intended for educational and demonstration purposes only — not for deployment in production sonar systems.
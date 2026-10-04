# Sonar and Signal Processing

Python simulations and notebooks exploring how waveforms, arrays and detection methods fit together in underwater acoustics.

This repository retains earlier signal-processing learning projects. My current professional focus is digital rock simulation and pore-scale fluid flow. These earlier examples remain available as numerical learning work.

## A useful route through the repository

| Start with | The question it explores | Open |
| --- | --- | --- |
| Waveform design | How do signal bandwidth and coding change the transmitted waveform? | [Waveform simulations](waveform_design/notebooks/waveform_simulations.ipynb) |
| Beamforming | How does an array use arrival-time differences to explore direction? | [Beamforming simulation](beamformer/notebooks/beamforming_simulation.ipynb) |
| Signal chain | How do the individual DSP operations combine? | [Full sonar pipeline](utils/full_sonar_pipeline.ipynb) |
| Detection | What separates a candidate signal from noise? | [Detection notebook](detection/notebooks/detection_theory.ipynb) |
| Time-frequency analysis | When is a spectrum alone insufficient? | [Analysis notebook](non_sonar_dsp/fft_spectrogram_visualizer/time_frequency_analysis.ipynb) |

## What is here

- Waveform generation: linear chirps, Barker-code sequences and stepped-frequency examples.
- Array-processing notebooks and delay-and-sum simulation code.
- Matched filtering, signal-generation, correlation, FFT and spectrogram utilities.
- Detection, ROC and performance-analysis notebooks.
- General DSP examples: digital filtering, wavelet denoising and source separation.
- A Streamlit WAV-file visualizer for FFT and Gaussian-window spectrograms.

The collection contains exploratory notebooks and some incomplete examples. Repository contents demonstrate the topics investigated, not a claim that every module is finished.

## Run locally

For the core scientific notebooks:

```bash
python -m venv .venv
# Activate the environment using your operating system's command.
python -m pip install numpy scipy matplotlib jupyter
python -m jupyter notebook
```

Open one of the notebooks linked above. Individual modules may require additional packages listed in their documentation or imports.

For the interactive FFT/spectrogram example:

```bash
python -m pip install streamlit numpy scipy matplotlib
python -m streamlit run non_sonar_dsp/fft_spectrogram_visualizer/visualizer_app.py
```

Use a non-sensitive WAV file. The interface shows its spectrum and a spectrogram with adjustable window parameters.

## Scientific scope

These are educational simulations and visualization tools. They do not establish operational sonar performance, hardware timing or acoustic calibration. Integer-sample array delays, steering sign conventions, complex correlation behavior and performance metrics need targeted validation before engineering use.

This documentation update does not change the numerical implementations or claim that their full test suites have passed. The methods, assumptions and limitations are part of what a reviewer should inspect.

## About me

[Avradip Ghosh's skills portfolio](https://github.com/AvradipG/new_test_repo-) provides context for my independent mathematical and scientific computing work. Employer materials, client data, private research results and credentials are excluded from public presentation.

The earlier [project overview](README_sonar_dsp_project.md) remains available as historical documentation. This README states the scope of the current public collection more precisely.

# Project
text to speech pre-train with Nemo tools

# Problem
Limited availability of pre-trained text-to-speech models for generating high-quality, natural-sounding speech.

# Solution
Utilize NeMo Tools, a framework for building and training neural models, to pre-train text-to-speech models, enabling the generation of synthetic speech with improved quality, expressiveness, and naturalness.

# Methodology
1. install and setup environment
2. Download and Load the SpectrogramGenerator model
3. Download and Load the Vocoder model
4. Character to tokenized id
5. Tokenised id to mel-spectrogram
6. Mel-spectrogram to audio
7. comparative 5 SpectrogramGenerator and 6 Vocoder
    - Text2Wav
8. Generate speech from trained models (local)
    - download the trained model to local
    - get text input and predict speech output

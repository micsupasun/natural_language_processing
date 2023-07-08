# Project
custom text to speech 

# Problem
Lack of personalized or customized voice options for text-to-speech applications.

# Solution
Develop a custom text-to-speech system that allows users to create or select personalized voices, enabling a more tailored and engaging audio experience for different applications.

# Methodology
1. install library
2. Modify Parser for Thai phoneme
3. Changing input from text to phoneme
4. Building Thai TTS using Tacotron2
    - Prepare transcription files
    - Prepare phoneme transcription files
5. Automatic phoneme forced alignment
6. Modify the config file
7. Create a script for training
8. Inference Thai TTS using trained checkpoint
9. Load the Tacotron2Model
10. Tacotron2Model is a SpectrogramGenerator to help parse and generator in NeMo
11. get text input and predict speech output

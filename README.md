# Real-Time Voice Changer with RVC (Python)

This Python script provides a simple way to change your voice in real-time using RVC (Retrieval-based Voice Conversion) technology.

## Features

* **Real-time Voice Change:**  Press 'V' to toggle voice recording and transformation.
* **Multiple Character Profiles:** Cycle through different voice profiles (e.g., Peter, Trump, Neon) by pressing 'L'.
* **Virtual Audio Output:**  Output the changed voice to a specific audio device for easy integration with other applications.

## Requirements

* **RVC Environment:** Install RVC and its dependencies. Detailed instructions can be found in the RVC documentation.
* **Python Libraries:**  `pyaudio`, `wave`, `pydub`, `rvc_python`, `sounddevice`, `soundfile`, `keyboard`, `pynput`, `threading`
* Install them using `pip install pyaudio wave pydub rvc_python sounddevice soundfile keyboard pynput` 

## Usage

1. **Run the Script:**
   ```bash
   python voice_changer.py
   ```

2. **Voice Change:** Press and hold 'V' to record and change your voice. Release 'V' to stop recording and hear the transformed audio.
3. **Change Character:** Press 'L' to cycle to the next character profile. The current character's name will be printed to the console.

## Disclaimer

This project is intended for experimentation and entertainment purposes. The use of voice transformation technology may be restricted in certain situations, so please use it responsibly. 

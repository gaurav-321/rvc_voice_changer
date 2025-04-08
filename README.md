# RVC Voice Changer

🚀 **Project Title:** RVC Voice Changer

✨ **Description:** RVC Voice Changer is a Python program that leverages Retrieval-based Voice Conversion (RVC) technology to provide real-time voice change capabilities. It allows users to switch between different character profiles and output the transformed voice through a virtual audio device.

---

## 🚀 Features
- Real-time voice transformation based on selected character profiles.
- User-friendly interface for recording and switching voice profiles.
- Output of transformed voice through a virtual audio device.
- Detailed logs for error tracking and debugging.

---

## ⛓ Installation

To set up RVC Voice Changer, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gag3301v/rvc_voice_changer.git
   cd rvc_voice_changer
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📦 Usage

### VoiceChanger Example

```python
from voicechanger import VoiceChanger, CharacterProfileManager

# Initialize the VoiceChanger and CharacterProfileManager
voice_changer = VoiceChanger()
profile_manager = CharacterProfileManager()

# Load a character profile
profile_manager.load_profile("character1")

# Start recording and transforming voice
voice_changer.start_recording_and_transform(profile_manager.current_profile)
```

### rvc_test.py Example

```python
from rvc_test import record_audio, change_pitch, play_audio

# Record audio from the default input device
recorded_audio = record_audio()

# Change the pitch of the recorded audio
processed_audio = change_pitch(recorded_audio, semitone_shift=2)

# Play the processed audio through a virtual output device
play_audio(processed_audio)
```

---

## 🔧 Configuration

- **Environment Variables:**
  - `RVC_API_KEY`: API key for accessing RVC services (if required).

- **Config Files:**
  - `config.ini`: Contains settings for voice profiles and other configurations.

---

## 🧪 Tests

To run tests, execute the following command:

```bash
pytest tests/
```

Ensure you have pytest installed:
```bash
pip install pytest
```

---

## 📁 Project Structure

```
rvc_voice_changer/
├── README.md
├── requirements.txt
├── voicechanger/
│   ├── __init__.py
│   ├── VoiceChanger.py
│   └── CharacterProfileManager.py
└── rvc_test.py
```

---

## 🙌 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository.**
2. **Create a new branch:**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes and commit them:**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a pull request.**

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![Python Version](https://img.shields.io/pypi/pyversions/rvc_voice_changer)](https://pypi.org/project/rvc_voice_changer/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
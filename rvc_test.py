import os
import random
import time
import traceback
from pynput.keyboard import Controller
import pyaudio
import wave
from pydub import AudioSegment
from pydub.playback import play
from rvc_python.infer import infer_file
import timeit
import sounddevice as sd
import soundfile as sf
import keyboard
from threading import Thread

character = ("peter", 1)
keyboard_ctrl = Controller()


def is_key_pressed(key):
    return keyboard.is_pressed(key)


def play_wav_through_virtual_output(wav_file, device_id=45):
    try:
        data, samplerate = sf.read(wav_file)
        sd.play(data, samplerate, device=device_id)
        sd.wait()
    except Exception as e:
        print("Error playing audio:", e)


def play_sound(sound_file):
    try:
        sound = AudioSegment.from_file(sound_file)
        play(sound)
    except Exception as e:
        print("Error playing sound:", e)


def record_audio(output_file, duration=5, channels=1, rate=44100, chunk=1024, format=pyaudio.paInt16):
    global pressed
    if pressed:
        audio = pyaudio.PyAudio()
        stream = audio.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
        frames = []
        while pressed:
            data = stream.read(chunk)
            frames.append(data)
        stream.stop_stream()
        stream.close()
        audio.terminate()
        print("Frames count", len(frames))
        wf = wave.open(output_file, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
        wf.close()
        if len(frames) > 25:
            return True
        else:
            return False
    else:
        return False


def get_input_device_index(device_name):
    p = pyaudio.PyAudio()
    for i in range(p.get_device_count()):
        device_info = p.get_device_info_by_index(i)
        if device_name in device_info['name']:
            return i
    return None


def play_audio(file_path, input_device_index):
    chunk = 1024
    wf = wave.open(file_path, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,  # Set to output
                    input_device_index=input_device_index)  # Specify input device index
    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


def process_file(input_file):
    result = infer_file(
        input_path="output.wav",
        model_path=rf"F:\Windows_Tools\RVC1006Nvidia\RVC1006Nvidia\assets\weights\{character[0]}.pth",
        index_path=rf"F:\Windows_Tools\RVC1006Nvidia\RVC1006Nvidia\logs\{character[0]}.index",
        device="cuda",
        f0method="rmvpe",
        opt_path="out.wav",
        index_rate=0,
        filter_radius=3,
        resample_sr=0,
        rms_mix_rate=0.25,
        protect=0.33,
        version="v2",
        f0up_key=character[1]  # pitch

    )
    print("Inference completed. Output saved to:", result)
    return True


pressed = False


def on_press(key):
    global pressed
    pressed = True


def on_release(key):
    global pressed
    pressed = False


def change_voice(key):
    global character
    character_settings = [("peter", 1), ("trump", -1), ("neon", 8)]
    # set random character
    character = character_settings[(character_settings.index(character) + 1) % len(character_settings)]
    print(character)


def main():
    keyboard.on_press_key("v", on_press)
    keyboard.on_release_key("v", on_release)
    keyboard.on_release_key("l", change_voice)
    while True:
        if record_audio("output.wav"):
            try:
                process_file("output.wav")
                keyboard_ctrl.press("v")
                play_wav_through_virtual_output("out.wav")
                keyboard_ctrl.release("v")

            except Exception as e:
                traceback.print_exc()
                continue
        else:
            continue


if __name__ == "__main__":
    main()

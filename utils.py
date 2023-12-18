import os

import numpy as np
import wave


def output_wave(file_name: str,
                sampling_frequency: int,
                signal: np.ndarray,
                channels: int = 1) -> None:
    audio = (signal * (2 ** 15 - 1)).astype("<h")
    with wave.open(file_name, 'w') as f:
        f.setnchannels(channels)
        f.setframerate(sampling_frequency)
        f.setsampwidth(2)
        f.writeframes(audio.tobytes())


def get_output_path(file_name: str) -> str:
    path = os.path.dirname(__file__)
    output = os.path.join(path, 'output', file_name)
    return output

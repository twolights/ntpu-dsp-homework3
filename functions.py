from typing import Callable, Tuple, Optional

import numpy as np


def magnitude(x: complex) -> float:
    return np.sqrt(x.real ** 2 + x.imag ** 2)


def hamming_window(M: int) -> np.ndarray:
    result = np.ndarray(shape=(M, ))
    for n in range(0, M):
        result[n] = 0.54 - 0.46 * np.cos(np.pi * 2 * n / (M - 1))
    return result


def dtft(y: np.ndarray, omega: float) -> complex:
    result = 0 + 0j
    for n, v in enumerate(y):
        result += v * np.exp(-1j * omega * n)
    return result


def impulse_response(H: Callable, M: int) -> Tuple[np.ndarray, np.ndarray]:
    x = np.arange(0, 2 * M + 1, dtype=np.clongdouble)
    y = H(x)
    return x, y


def create_sine_wave(frequency: int,
                     seconds: int,
                     sampling_frequency: Optional[int] = None) -> Tuple[np.ndarray, np.ndarray]:
    if sampling_frequency is None:
        sampling_frequency = frequency * 6
    step = 1 / sampling_frequency
    x = np.arange(0, seconds, step=step)
    x_padding = np.arange(seconds, seconds + 100 * step, step=step)
    y_padding = np.zeros(101)
    y = np.concatenate([np.sin(2 * np.pi * frequency * x), y_padding])
    return np.concatenate([x, x_padding]), y

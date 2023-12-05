from typing import Callable

import numpy as np
import functools
import functions


def low_pass_filter(cutoff_frequency: float, sampling_frequency: float, M: int, x: np.ndarray):
    h_M = np.zeros_like(x, dtype='float64')
    omega_c = cutoff_frequency * np.pi * 2 / sampling_frequency
    for i, n in enumerate(x):
        if n == M:
            h_M[i] = omega_c / np.pi
            continue
        h_M[i] = np.sin((n - M) * omega_c) / ((n - M) * np.pi)
    window = functions.hamming_window(2 * M + 1)
    return h_M * window


def create(cutoff_frequency: float, sampling_frequency: float, M: int) -> Callable:
    return functools.partial(low_pass_filter, cutoff_frequency, sampling_frequency, M)

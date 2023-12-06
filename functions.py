import numpy as np


def magnitude(x: complex) -> float:
    return np.sqrt(x.real ** 2 + x.imag ** 2)


def hamming_window(M: int) -> np.ndarray:
    result = np.ndarray(shape=(M, ))
    for n in range(0, M):
        result[n] = 0.54 - 0.46 * np.cos(np.pi * 2 * n / M)
    return result


def dtft(y: np.ndarray, omega: float) -> complex:
    result = 0 + 0j
    for n, v in enumerate(y):
        result += v * np.exp(-1j * omega * n)
    return result

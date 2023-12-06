import os
from typing import Callable, Optional

import matplotlib.pyplot as plt
import numpy as np

import functions


def _show_or_save(fileName: Optional[str]):
    if fileName is None:
        plt.show()
    else:
        path = os.path.dirname(__file__)
        output = os.path.join(path, 'output', fileName)
        plt.savefig(output)
    plt.close()


def plot_impulse_response(H: Callable, M: int,
                          fileName: Optional[str] = None) -> None:
    x = np.arange(0, 2 * M + 1)
    y = H(x)
    plt.vlines(x, 0, y)
    _show_or_save(fileName)


def plot_frequency_magnitude(H: Callable, M: int,
                             fileName: Optional[str] = None) -> None:
    n = np.arange(0, 2 * M + 1)
    y = H(n)
    x = np.linspace(-np.pi, np.pi, 1001)
    result = np.zeros_like(x)
    for i, omega in enumerate(x):
        result[i] = functions.magnitude(functions.dtft(y, omega))
    plt.plot(x, result)
    _show_or_save(fileName)

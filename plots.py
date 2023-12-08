from typing import Callable, Optional

import matplotlib.pyplot as plt
import numpy as np

import constants
import functions
import lccde
from utils import get_output_path

FIGURE_PADDING = 2.0
FIGURE_WIDTH = 8
FIGURE_HEIGHT = 6


def _show_or_save(file_name: Optional[str]):
    if file_name is None:
        plt.show()
    else:
        output = get_output_path(file_name)
        plt.savefig(output)
    plt.close()


def plot_impulse_response(H: Callable, M: int,
                          file_name: Optional[str] = None) -> None:
    x, y = functions.impulse_response(H, M)
    plt.suptitle(f"Impulse Response of $H_{{lp}}$ - M = {M}")
    plt.vlines(x, 0, y, linewidth=0.5)
    _show_or_save(file_name)


def _save_csv(y: np.ndarray, file_name: str):
    np.savetxt(file_name, y, delimiter=',')


def plot_and_save_frequency_magnitude(H: Callable, M: int,
                                      file_name: Optional[str] = None) -> None:
    n = np.arange(0, 2 * M + 1)
    y = H(n)
    x = np.linspace(-np.pi, np.pi, 1001)
    result = np.zeros_like(x)
    for i, omega in enumerate(x):
        result[i] = functions.magnitude(functions.dtft(y, omega))
    plt.suptitle(f"Frequency Response of $H_{{lp}}$ - M = {M}")
    plt.plot(x, result, linewidth=0.5)
    _show_or_save(file_name + '.png')
    _save_csv(y, get_output_path(file_name + '.csv'))


def plot_head_tail_transient(M: int,
                             H: Callable,
                             signal_frequency: int,
                             x: np.ndarray,
                             y: np.ndarray,
                             file_name: Optional[str] = None) -> None:
    result = H(y)
    plt.close()
    figure, (upper, lower) = plt.subplots(2)
    figure.suptitle(f"Filtered Signal, Head & Tail - M = {M}\nSine Signal at {signal_frequency} Hz")
    figure.tight_layout(pad=FIGURE_PADDING)
    figure.set_figwidth(FIGURE_WIDTH)
    figure.set_figheight(FIGURE_HEIGHT)
    num_points = max(200, M * 2)
    upper.plot(x[:num_points], result[:num_points], linewidth=0.5)
    lower.plot(x[-num_points:], result[-num_points:], linewidth=0.5)
    _show_or_save(file_name)


def plot_linear_and_minimum_phase_coefficients(M: int,
                                               linear_coefficients: np.ndarray,
                                               min_phase_coefficients: np.ndarray,
                                               file_name: Optional[str]) -> None:
    figure, (upper, lower) = plt.subplots(2)
    figure.tight_layout(pad=FIGURE_PADDING)
    figure.set_figwidth(FIGURE_WIDTH)
    figure.set_figheight(FIGURE_HEIGHT)
    figure.suptitle(f"Impulse Response - M = {M}")

    x_coefficients = np.arange(0, linear_coefficients.shape[0])
    upper.vlines(x_coefficients, 0, linear_coefficients, linewidth=0.5)
    upper.set_xlabel('Linear Phase')

    x_min_phase_coefficients = np.arange(0, min_phase_coefficients.shape[0])
    lower.vlines(x_min_phase_coefficients, 0, min_phase_coefficients, linewidth=0.5)
    lower.set_xlabel('Minimum Phase')

    _show_or_save(file_name)
    plt.close()

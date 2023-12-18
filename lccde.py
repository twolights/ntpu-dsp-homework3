import functools
from typing import Callable

import numpy as np
from numpy.polynomial.polynomial import Polynomial

import functions
import lowpass_filter


def _LCCDE_prototype(coefficients: np.ndarray, x: np.ndarray) -> np.ndarray:
    def _value_or_initial_rest(o: np.ndarray, index: int) -> complex:
        if index < 0:
            return 0
        return o[index]

    output = np.zeros_like(x)
    for n, v in enumerate(x):
        for i, b_k in enumerate(coefficients):
            output[n] += b_k * _value_or_initial_rest(x, n - i)
    return output


def _get_impulse_response(sampling_frequency, cutoff_frequency, M):
    H_lp = lowpass_filter.create(cutoff_frequency, sampling_frequency, M)
    _, impulse_response = functions.impulse_response(H_lp, M)
    return impulse_response


def create(cutoff_frequency: float, sampling_frequency: float, M: int) -> Callable:
    impulse_response = _get_impulse_response(sampling_frequency, cutoff_frequency, M)
    return functools.partial(_LCCDE_prototype, impulse_response)


def create_with_coefficients(coefficients: np.ndarray) -> Callable:
    return functools.partial(_LCCDE_prototype, coefficients)


def create_minimum_phase(cutoff_frequency: float, sampling_frequency: float, M: int) -> Callable:
    min_phase_coefficients = get_min_phase_coefficients(cutoff_frequency, sampling_frequency, M)
    return create_with_coefficients(min_phase_coefficients)


def get_min_phase_coefficients(cutoff_frequency, sampling_frequency, M) -> np.ndarray:
    impulse_response = _get_impulse_response(sampling_frequency, cutoff_frequency, M)
    all_pass_coefficient = 1
    z = Polynomial(impulse_response)
    zeroes = z.roots()
    for i, zero in enumerate(zeroes):
        m = functions.magnitude(zero)
        if m > 1:
            zero_before = zero
            zero = np.reciprocal(np.conjugate(zero))
            zeroes[i] = zero
            all_pass_coefficient *= np.real(zero_before)
    min_phase_coefficients = np.real(np.flip(np.polynomial.polynomial.polyfromroots(zeroes)))
    return min_phase_coefficients * all_pass_coefficient

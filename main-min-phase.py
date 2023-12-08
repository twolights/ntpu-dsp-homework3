import constants
import functions
import lccde
import lowpass_filter
import plots

TEST_FREQ = 3500

x, y = functions.create_sine_wave(TEST_FREQ, 5, constants.Fs)

for FREQ in constants.TEST_SINE_FREQUENCIES:
    x, y = functions.create_sine_wave(FREQ, constants.SIGNAL_LENGTH_IN_SECONDS, constants.Fs)
    for M in constants.MIN_PHASE_Ms:
        H_linear = lowpass_filter.create(constants.Fc, constants.Fs, M=M)
        _, ir = functions.impulse_response(H_linear, M=M)

        min_phase_coefficients = lccde.get_min_phase_coefficients(constants.Fc, constants.Fs, M=M)
        file_name = f"MIN_PHASE_M-{M}-linear-vs-minimum-phase-ir.png"
        plots.plot_linear_and_minimum_phase_coefficients(M, ir, min_phase_coefficients, file_name)

        H = lccde.create_with_coefficients(min_phase_coefficients)
        y = H(y)
        file_name = f"MIN_PHASE_M-{M}-input-freq-{FREQ}Hz.png"
        plots.plot_head_tail_transient(M, H, FREQ, x, y, file_name)

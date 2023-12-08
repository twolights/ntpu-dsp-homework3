import constants
import functions
import lccde
import plots
from constants import TEST_SINE_FREQUENCIES, SIGNAL_LENGTH_IN_SECONDS

for FREQ in TEST_SINE_FREQUENCIES:
    x, y = functions.create_sine_wave(FREQ, SIGNAL_LENGTH_IN_SECONDS, constants.Fs)
    for M in constants.Ms:
        H = lccde.create(constants.Fc, constants.Fs, M)
        y = H(y)
        file_name = f"LINEAR_PHASE_M-{M}-input-freq-{FREQ}Hz.png"
        plots.plot_head_tail_transient(M, H, FREQ, x, y, file_name)

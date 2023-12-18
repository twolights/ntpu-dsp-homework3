import constants
import functions
import lccde
import plots
import utils
from constants import TEST_SINE_FREQUENCIES, SIGNAL_LENGTH_IN_SECONDS

ORIGINAL_WAV_FORMAT = 'original-sine-wave-%dHz.wav'

for FREQ in TEST_SINE_FREQUENCIES:
    x, y = functions.create_sine_wave(FREQ, SIGNAL_LENGTH_IN_SECONDS, constants.Fs)
    original_wave_name = utils.get_output_path(ORIGINAL_WAV_FORMAT % FREQ)
    utils.output_wave(original_wave_name, constants.Fs, y)
    for M in constants.Ms:
        H = lccde.create(constants.Fc, constants.Fs, M)
        y = H(y)
        file_name = f"LINEAR_PHASE_M-{M}-input-freq-{FREQ}Hz"
        plots.plot_head_tail_transient(M, H, FREQ, x, y, file_name + '.png')
        wave_name = utils.get_output_path(file_name + '.wav')
        utils.output_wave(wave_name, constants.Fs, y)

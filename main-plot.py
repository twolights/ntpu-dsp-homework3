import sys
from typing import Tuple

import constants
import lowpass_filter
import plots

COMMAND_GEN = 'gen'
COMMAND_SHOW = 'show'
COMMANDS = (COMMAND_GEN, COMMAND_SHOW)
DEFAULT_COMMAND = COMMANDS[0]

PLOT_IMPULSE_RESPONSE = 'ir'
PLOT_FREQUENCY = 'freq'
PLOTS = (PLOT_IMPULSE_RESPONSE, PLOT_FREQUENCY)
DEFAULT_PLOT = PLOT_FREQUENCY


def get_command() -> Tuple[str, str]:
    if len(sys.argv) <= 1:
        command = DEFAULT_COMMAND
    else:
        command = sys.argv[1]
    if command not in COMMANDS:
        raise RuntimeError(f"Unsupported command {command}")
    if len(sys.argv) <= 2:
        plot_name = DEFAULT_PLOT
    else:
        plot_name = sys.argv[2]
    if plot_name not in PLOTS:
        raise RuntimeError(f"Unknown plot {plot_name}")
    return command, plot_name


def main() -> None:
    command, plot_name = get_command()
    for M in constants.Ms:
        H_lp = lowpass_filter.create(constants.Fc, constants.Fs, M)

        fileName = None
        if plot_name == PLOT_IMPULSE_RESPONSE:
            if command == COMMAND_GEN:
                fileName = 'ir_M-%d.png' % M
            plots.plot_impulse_response(H_lp, M, fileName)
        elif plot_name == PLOT_FREQUENCY:
            if command == COMMAND_GEN:
                fileName = 'freq_M-%d.png' % M
            plots.plot_frequency_magnitude(H_lp, M, fileName)


if __name__ == '__main__':
    main()

import sys
from typing import Tuple

import constants
import lowpass_filter
import plots

COMMAND_GEN = 'gen'
COMMAND_SHOW = 'show'
COMMANDS = (COMMAND_GEN, COMMAND_SHOW)

PLOT_IMPULSE_RESPONSE = 'ir'
PLOT_FREQUENCY = 'freq'
PLOTS = (PLOT_IMPULSE_RESPONSE, PLOT_FREQUENCY)


def get_command() -> Tuple[Tuple[str], Tuple[str]]:
    if len(sys.argv) <= 1:
        command = COMMANDS
    else:
        command = sys.argv[1]
        if command not in COMMANDS:
            raise RuntimeError(f"Unsupported command {command}")
        command = (command, )
    if len(sys.argv) <= 2:
        plot_name = PLOTS
    else:
        plot_name = sys.argv[2]
        if plot_name not in PLOTS:
            raise RuntimeError(f"Unknown plot {plot_name}")
        plot_name = (plot_name, )
    return command, plot_name


def main() -> None:
    commands, plot_names = get_command()
    for M in constants.Ms:
        H_lp = lowpass_filter.create(constants.Fc, constants.Fs, M)

        for command in commands:
            for plot_name in plot_names:
                file_name = None
                if plot_name == PLOT_IMPULSE_RESPONSE:
                    if command == COMMAND_GEN:
                        file_name = 'LOWPASS_ir_M-%d.png' % M
                    plots.plot_impulse_response(H_lp, M, file_name)
                elif plot_name == PLOT_FREQUENCY:
                    if command == COMMAND_GEN:
                        file_name = 'LOWPASS_freq_M-%d' % M
                    plots.plot_and_save_frequency_magnitude(H_lp, M, file_name)


if __name__ == '__main__':
    main()

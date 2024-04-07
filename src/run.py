"""Script for calibration document decoding."""

import argparse
from pathlib import Path

from calibration import CalibrationDocDecoder


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path,
                        help='Path to the calibration document.')
    return parser.parse_args()


if __name__ == '__main__':
    """App entry point."""
    args = parse_args()
    decoder = CalibrationDocDecoder()
    output = decoder(args.path)
    print('Total sum of the calibration values: ', output)

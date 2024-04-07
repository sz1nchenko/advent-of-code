"""Structure for calibration document decoding."""

import re
from pathlib import Path


class CalibrationDocDecoder:
    """
    Structure that represents decoder for the calibration document.
    It reads the calibration document, decodes each line by extracting the first
    and last digit (including written numbers), and sums these
    values to produce a total calibration value.
    """

    def __init__(self):
        """Init decoder."""
        self.__digit_names = ['one', 'two', 'three', 'four', 'five',
                              'six', 'seven', 'eight', 'nine']
        self.__pattern = '(?=(' + '|'.join(self.__digit_names) + '|\\d))'

    def __call__(self, path: Path) -> int:
        """
        Perform decoding of the calibration document.

        Parameters
        ----------
        path: Path
            Path to the calibration document.

        Returns
        -------
        int
            The total sum of the calibration values computed
            from the document.
        """
        total_sum = 0
        name2digit = (lambda x:
                      str(self.__digit_names.index(x) + 1)
                      if x in self.__digit_names else x)
        with path.open('r') as doc_file:
            for line in doc_file:
                digits = list(map(name2digit, re.findall(self.__pattern, line)))
                total_sum += int(digits[0] + digits[-1])
        return total_sum

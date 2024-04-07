"""Tests for calibration document decoder."""

import pytest
from calibration import CalibrationDocDecoder


@pytest.fixture
def calibration_doc(tmp_path):
    """Fixture to create a temporary calibration document."""
    def _calibration_doc(content):
        doc_path = tmp_path / 'input.txt'
        doc_path.write_text(content)
        return doc_path
    return _calibration_doc


def test_decode_digits(calibration_doc):
    """Test decoding with only digits."""
    content = '123\n456\n789'
    doc_path = calibration_doc(content)
    decoder = CalibrationDocDecoder()
    assert decoder(doc_path) == 138


def test_decode_written_numbers(calibration_doc):
    """Test decoding with written numbers."""
    content = 'one\ntwo\nthree'
    doc_path = calibration_doc(content)
    decoder = CalibrationDocDecoder()
    assert decoder(doc_path) == 66


def test_decode_mixed_numbers(calibration_doc):
    """Test decoding with a mix of digits and written numbers."""
    content = '14five3four\none5nine'
    doc_path = calibration_doc(content)
    decoder = CalibrationDocDecoder()
    assert decoder(doc_path) == 33


def test_decode_overlapped_numbers(calibration_doc):
    """Test decoding with a overlapped written numbers."""
    content = 'xtwone3four\nzoneight234'
    doc_path = calibration_doc(content)
    decoder = CalibrationDocDecoder()
    assert decoder(doc_path) == 38


def test_decode_empty_document(calibration_doc):
    """Test with an empty document."""
    doc_path = calibration_doc('')
    decoder = CalibrationDocDecoder()
    assert decoder(doc_path) == 0

"""
Module: reader_commons
"""

def remove_channels():
  return[
    'T8-P8-1',
  ]

def rename_channels():
  return {
    'T8-P8-0':'T8-P8',
    }

def selected_channels():
  """
    Returns a list of selected EEG (Electroencephalography) channel names commonly used in neurophysiological studies.
    A list of selected EEG channel names. Each channel name represents a specific electrode placement on the scalp.
    """
  return [
    'P8-O2',
    'CZ-PZ',
    'T7-P7',
    'FZ-CZ',
    'C3-P3',
    'P4-O2',
    'C4-P4',
    'FP1-F7',
    'F3-C3',
    'F4-C4',
    'P7-O1',
    'FP2-F8',
    'F7-T7',
    'FP2-F4',
    'FP1-F3',
    'P3-O1',
    'F8-T8',
    'T8-P8',
  ]
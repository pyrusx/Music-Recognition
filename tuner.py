import numpy as np 
import pyaudio


NOTES = 'C C# D D# E F F# G G# A A# B'.split()

MIN_FREQ = 27.5 #A0

MAX_FREQ = 4186.0 #C8

REF_FREQ = 440 #A4

def number_octaves(freq1, freq2):
    return np.log2(freq2/freq1)

def note_to_frequency(note):
    return (2^(note/12)) * REF_FREQ

def 
# All semitones have ratio of 2^(1/12)
print(number_octaves(23, 4))
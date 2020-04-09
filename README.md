# SARS-CoV-2
Music generated from the genome of the SARS-CoV-2 coronavirus. Listen on my [SoundCloud](https://soundcloud.com/skrubstudio/sars-cov-2)!

The DNA transcription is composed of four nucleotides, symbolized by the letters A, C, G, and T. A, C, and G have natural musical analogues: I map them to A3, C4, and G4. For T, I simply counted letters up the scale from A3 to arrive at F6. Each nucleotide is played as a 1/32 note at 150 BPM such that the entire work lasts about 25 minutes. Repeated nucleotides are merged together into notes of longer duration (e.g. a sequence of 2 T's becomes a 1/16 F6 note). It certainly becomes tedious but eventually does come to an end.

MIDI file available [here](https://github.com/michaelburks/sars-cov-2/blob/master/output/sars-cov-2.mid) or generate the audio directly by running `$ python player.py`.

### References
SARS-CoV-2 genome source: https://www.ncbi.nlm.nih.gov/nuccore/MT072688

Python Synthesizer: https://pypi.org/project/synthesizer/

MIDIUtil: https://pypi.org/project/MIDIUtil/

### Dependencies (MacOS)
* `$ pip install synthesizer`
* `$ brew install portaudio`
* `$ pip install pyaudio`
* `$ pip install MIDIUtil`

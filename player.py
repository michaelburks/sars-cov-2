# https://pypi.org/project/synthesizer/

from synthesizer import Player, Synthesizer, Waveform

import genome

player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)

w = 0.5
l = 0.05

nuc_freqs = {'a': 440.00 * w, 'g': 392.00 * 2 * w, 'c': 523.25 * w, 't': 2793 * w}

merge_repeated_nucleotides = True

if (merge_repeated_nucleotides):
  for nuc_seg in genome.segments():
    player.play_wave(synthesizer.generate_constant_wave(nuc_freqs[nuc_seg[0]], l * nuc_seg[1]))
else:
  for nucleotide in genome.sequence():
    player.play_wave(synthesizer.generate_constant_wave(nuc_freqs[nucleotide], l))

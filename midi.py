from midiutil import MIDIFile

from genome import segments

midi = {}
midi['a'] = midi_a3 = 57
midi['c'] = midi_c4 = 60
midi['g'] = midi_g4 = 67
midi['t'] = midi_f6 = 89

track    = 0
channel  = 0
time     = 0     # In beats
duration = 0.125 # In beats
tempo    = 150   # In BPM
volume   = 100   # 0-127

if __name__ == '__main__':
  genomeMIDI = MIDIFile(1)  # One track, defaults to format 1
  genomeMIDI.addTempo(track, time, tempo)

  for (note, beats) in segments():
      pitch = midi[note]
      note_duration = beats * duration
      genomeMIDI.addNote(track, channel, pitch, time, note_duration, volume)
      time += note_duration

  with open("output/sars-cov-2.mid", "wb") as output_file:
      genomeMIDI.writeFile(output_file)

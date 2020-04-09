def sequence():
  '''
    Returns the genome sequence as a raw string.
  '''
  with open("data/genome.txt", 'r') as input:
    genome = input.readline()
  return genome

def segments():
  '''
    Returns the genome sequence as a list of segments (nucleotide, number of repetitions).
  '''
  genome_str = sequence()
  genome_segments = []

  seg = (genome_str[0], 1)
  for i in range(1, len(genome_str)):
    nuc = genome_str[i]
    if (nuc == seg[0]):
      seg = (nuc, seg[1]+1)
    else:
      genome_segments.append(seg)
      seg = (nuc, 1)
  genome_segments.append(seg)
  return genome_segments

raw = "genome_raw.txt"

genome_components = []

with open(raw, 'r') as input:
  for line in input:
    comps = line[:-1].split(" ")[1:] # Drop trailing \n and counter at start of line
    genome_components += comps

genome = "".join(genome_components)

with open("genome.txt", 'w') as output:
  output.write(genome)
  print(len(genome))

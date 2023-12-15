import warnings
from Bio.PDB import PDBParser

warnings.filterwarnings("ignore")

# create parser
parser = PDBParser()

pdb_file = r"C:\Monika\module 6\8TIM.pdb"

# read structure from file
structure = parser.get_structure('8TIM', pdb_file)

model = structure[0]
chain = model['A']

# this example uses only the first residue of a single chain.
# it is easy to extend this to multiple chains and residues.
for residue1 in chain:
    for residue2 in chain:
        if residue1 != residue2:
            # compute distance between CA atoms
            try:
                distance = residue1['CA'] - residue2['CA']
            except KeyError:
                ## no CA atom, e.g. for H_NAG
                continue
            if distance < 6:
                print(
                    f"Helix ID: ({residue1.get_id()}, {residue2.get_id()}), Distance: {distance:.3f} \u00C5"
                )
        # stop after first residue
        break


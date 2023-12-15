import warnings
from Bio.PDB import PDBParser

warnings.filterwarnings("ignore")

parser = PDBParser()

pdb_file = r"C:\Monika\module 6\8TIM.pdb"

structure = parser.get_structure('8TIM', pdb_file)

model = structure[0]
chain = model['A']

for residue1 in chain:
    for residue2 in chain:
        if residue1 != residue2:
            try:
                distance = residue1['CA'] - residue2['CA']
            except KeyError:
                continue
            if distance < 6:
                print(
                    f"Helix ID: ({residue1.get_id()}, {residue2.get_id()}), Distance: {distance:.3f} \u00C5"
                )
        break


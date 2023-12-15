from Bio import PDB
import csv
import pandas as pd
from collections import defaultdict

def pdb_to_csv(pdb_file, csv_file):
    structure = PDB.PDBParser(QUIET=True).get_structure('structure', pdb_file)

    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        # Write header
        csv_writer.writerow(['Record', 'Atom', 'Residue', 'Chain', 'X', 'Y', 'Z', 'B-Factor'])

        # Write data
        for model in structure:
            for chain in model:
                for residue in chain:
                    for atom in residue:
                        row = [
                            atom.get_full_id()[0],  # Record type (ATOM or HETATM)
                            atom.get_name(),        # Atom name
                            residue.get_resname(),   # Residue name
                            chain.get_id(),          # Chain identifier
                            *atom.get_coord(),       # X, Y, Z coordinates
                            atom.get_bfactor()       # B-factor
                        ]
                        csv_writer.writerow(row)


def process_loops(structure):
    loops = defaultdict(list)

    for model in structure:
        for chain in model:
            residues = list(chain.get_residues())
            current_loop = [residues[0]]
            loop_data = {'b_factors':[], 'residues':[]}
            
            for i in range(1, len(residues)):
                if residues[i].id[1] - residues[i - 1].id[1] == 1:
                    current_loop.append(residues[i])
                else:
                    if len(current_loop) > 1:
                        # Calculate average B-factor for the loop
                        b_factors = [atom.get_bfactor() for residue in current_loop for atom in residue.get_atoms()]
                        loop_data['b_factors'].extend(b_factors)

                        #store residue information
                        loop_data['residues'].extend([(residue.get_resname(), residue.id[1]) for residue in current_loop])

                    #start a new loop
                    current_loop = [residues[i]]

            #check if the last loop needs to processed
            if len(current_loop) > 1:
                b_factors = [atom.get_bfactor() for residue in current_loop for atom in residue.get_atoms()]
                loop_data['b_factors'].extend(b_factors)
                loop_data['residues'].extend([(residue.get_resname(), residue.id[1]) for residue in current_loop])


            # Calculate mean and standard deviation for B-factors
            if loop_data['b_factors']:
                loop_data['avg_b_factor'] = sum(loop_data['b_factors']) / len(loop_data['b_factors'])
                loop_data['std_b_factor'] = (sum((bf - loop_data['avg_b_factor']) ** 2 for bf in loop_data['b_factors']) / len(loop_data['b_factors'])) ** 0.5
            

            # Store loop information
                loop_id = f"loop_{len(loops) + 1}"
                loops[loop_id].append(loop_data)    

    return loops 

def print_loop_summary(loops): 
    print("Loop ID    B-factor")
    print("-------    --------")

    for loop_id, loop_data in loops.items():
        avg_b_factor = loop_data[0]['avg_b_factor']
        std_b_factor = loop_data[0]['std_b_factor']

        print(f"{loop_id.ljust(13)}{avg_b_factor:.1f} ± {std_b_factor:.2f}")

def print_loop_details(loops):
    for loop_id, loop_data in loops.items():
        print(f"\n{'=' * 8} {loop_id} {'=' * 8}")
        print("    Amino Acid      Position")
        print("    ----------      --------")

        for residue in loop_data[0]['residues']:
            print(f"    {residue[0].ljust(16)}{residue[1]}")

if __name__ == "__main__":
    pdb_file = '8tim.pdb'  # Replace with your PDB file path
    pdb_parser = PDB.PDBParser(QUIET=True)
    structure = pdb_parser.get_structure('structure', pdb_file)

    loops = process_loops(structure)

    # Print loop summary
    print_loop_summary(loops)

    # Print loop details
    print_loop_details(loops)



                    
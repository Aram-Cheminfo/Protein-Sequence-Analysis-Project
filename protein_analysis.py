from Bio import SeqIO
from Bio.SeqUtils import molecular_weight, IsoelectricPoint
from collections import Counter
import os

for file in os.listdir("data"):

    if file.endswith(".fasta"):

        print("\n" + "=" * 50)

        record = SeqIO.read(f"data/{file}", "fasta")
        sequence = str(record.seq)

        mw = molecular_weight(sequence, seq_type="protein")

        ip = IsoelectricPoint.IsoelectricPoint(sequence)
        pi = ip.pi()

        aa_counts = Counter(sequence)

        print("Protein File:", file)
        print("Protein ID:", record.id)
        print("Length:", len(sequence))
        print("Molecular Weight:", round(mw, 2))
        print("pI:", round(pi, 2))

        print("\nAmino Acid Composition:")
        for aa, count in sorted(aa_counts.items()):
            print(f"{aa}: {count}")

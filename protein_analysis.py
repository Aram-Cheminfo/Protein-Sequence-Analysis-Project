import os
from Bio import SeqIO
from Bio.SeqUtils import molecular_weight, IsoelectricPoint
from collections import Counter

for file in os.listdir("data"):
    if file.endswith(".fasta"):

        print("\n==============================")

        record = SeqIO.read(f"data/{file}", "fasta")
        seq = str(record.seq)

        mw = molecular_weight(seq, seq_type="protein")
        ip = IsoelectricPoint.IsoelectricPoint(seq).pi()
        aa = Counter(seq)

        print("Protein:", file)
        print("Length:", len(seq))
        print("Molecular Weight:", round(mw, 2))
        print("pI:", round(ip, 2))

        print("\nAmino Acid Composition:")
        for k, v in sorted(aa.items()):
            print(k, v)

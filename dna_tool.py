import random

dna = input("Enter a DNA sequence (A, T, C, G): ").upper()

if len(dna) == 0:
    print("Error: No DNA sequence entered")
    exit()

valid = True

for base in dna:
    if base not in "ATCG":
        valid = False
        break

if not valid:
    print("Error: Invalid DNA sequence (only A, T, C, G allowed)")
else:   
    print("DNA is valid")
    
    rna = dna.replace("T", "U")
    print("Transcribed RNA:", rna)

    codon_table = {
    "UUU":"Phe","UUC":"Phe","UUA":"Leu","UUG":"Leu",
    "UCU":"Ser","UCC":"Ser","UCA":"Ser","UCG":"Ser",
    "UAU":"Tyr","UAC":"Tyr","UAA":"STOP","UAG":"STOP",
    "UGU":"Cys","UGC":"Cys","UGA":"STOP","UGG":"Trp",

    "CUU":"Leu","CUC":"Leu","CUA":"Leu","CUG":"Leu",
    "CCU":"Pro","CCC":"Pro","CCA":"Pro","CCG":"Pro",
    "CAU":"His","CAC":"His","CAA":"Gln","CAG":"Gln",
    "CGU":"Arg","CGC":"Arg","CGA":"Arg","CGG":"Arg",

    "AUU":"Ile","AUC":"Ile","AUA":"Ile","AUG":"Met",
    "ACU":"Thr","ACC":"Thr","ACA":"Thr","ACG":"Thr",
    "AAU":"Asn","AAC":"Asn","AAA":"Lys","AAG":"Lys",
    "AGU":"Ser","AGC":"Ser","AGA":"Arg","AGG":"Arg",

    "GUU":"Val","GUC":"Val","GUA":"Val","GUG":"Val",
    "GCU":"Ala","GCC":"Ala","GCA":"Ala","GCG":"Ala",
    "GAU":"Asp","GAC":"Asp","GAA":"Glu","GAG":"Glu",
    "GGU":"Gly","GGC":"Gly","GGA":"Gly","GGG":"Gly"
}

    protein = ""
    started = False

    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        
        if len(codon) < 3:
            break
        
        amino_acid = codon_table.get(codon)

        if not started:
            if codon == "AUG":
                started = True
                protein += "MET "
            continue

        if amino_acid == "STOP":
            break

        protein += amino_acid + " "
    
    print("Protein:", protein)

    pairs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }

    complement = ""
    for base in dna:
        complement += pairs[base]
    
    print("Complementary DNA:", complement)

    reversed_complement = complement[::-1] 
    print("Reverse Complement:", reversed_complement)

    g_count = dna.count("G")
    c_count = dna.count("C")
    total_bases = len(dna)

    gc_percentage = ((g_count + c_count) / total_bases) * 100

    print(f"GC Content: {gc_percentage:.2f}%")

    mutate = input("Do you want to simulate a mutation? (yes/no):").lower()
    
    if mutate == "yes":
        bases = ["A", "T", "C", "G"]
        position = random.randint(0, len(dna) - 1)
        original_base = dna[position]
        new_base = random.choice(bases)
        while new_base == original_base:
            new_base = random.choice(bases)
        
        mutated_dna = dna[:position] + new_base + dna[position+1:]

        print("\n--- MUTATION OCCURED ---")
        print("Position:", position)
        print("Original base:", original_base)
        print("New base:", new_base)
        print("Mutated DNA:", mutated_dna)

        mutated_rna = mutated_dna.replace("T", "U")
        print("Mutated RNA:", mutated_rna)

    else:
        print("No mutation applied.")


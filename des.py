# Implementing DES
# Bit-Oriented Cipher
# brackets are subscripts
# Generate keys
# Process plaintext in 64-bit chuncks
# Initial Permutation - IP(x)
# Split 64-bit plaintext into 32-bit halves
# plug r[i] into f function with the key
# XOR L[i] with output of f function
# swap l[i -1 ] = r[i], output of XOR = r[i]
# at round 16 use final permutation table to get ciphertext

# F function
# 1. Expansion using E table
# 2. XOR Output of Expansion with key
# 3. Using the S-Box table do S-Box substitution
# 4. Use that output and plug into Permutation table
import Tables.tables.tables as t

if __name__ == '__main__':
    ip = t.initial_permutation_table()
    fp = t.final_permutation_table()
    expTable = t.expansion_table()
    perTable = t.permution_table()
    s_box = t.s_boxes()
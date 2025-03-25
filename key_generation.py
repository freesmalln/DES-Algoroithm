# Key Schedule
# Start with 64-bit key
# Use PC-1 table to remove parity bits, output is 56-bit
# split into 2 28-bit halves, c[0], d[0]
# In rounds i = 1, 2, 9 ,16, the two halves are each rotated left by one bit.
# In all other rounds where the two halves are each rotated left by two bits.
# After left shift use PC-2 table every round to get each subkey

import random
import Tables.tables.tables as t
import Util.file_operations as fo

key0 = random.getrandbits(64)
key0_after_pc1 = ""
fPath = "Util/key0.txt"

if __name__ == '__main__':
    pc1 = t.permuted_choice_1()
    pc2 = t.permuted_choice_2()
    
    if (fo.isEmpty(fPath)):
        fo.write(fPath, str(key0))
    else:
        key0 = fo.read(fPath)

    key0 = bin(key0)[2:]
    key0 = key0.zfill(64)
    for i in enumerate(pc1):
        key0_after_pc1 += str(key0[i[1]])

    r0 = key0_after_pc1[28:]
    l0 = key0_after_pc1[:28]

    if i in {1, 2, 9, 16}:
        print("1 left shift")
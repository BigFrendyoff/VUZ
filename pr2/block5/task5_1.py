def ham_dist(a, b):
    dim = max(len(bin(a)), len(bin(b))) - 2
    c = str(bin(a ^ b))[2:].rjust(dim, '0')
    print(c.count('1'))


ham_dist(0b11001111000101, 0b10111001010011)
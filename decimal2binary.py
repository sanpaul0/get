def decimal2binary(val):
    return [int(elem) for elem in bin(val)[2:].zfill(8)]

print(decimal2binary(10))
from struct import *
#Store as bytes data

packed_data = pack('iif',6 ,19 ,4.34)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

#To get bytes data back to normal(b'\x06\x00\x00\x00\x13\x00\x00\x00H\xe1\x8a@')
original_data = unpack('iif', packed_data)
print(original_data)

print(unpack('iif', b'\x06\x00\x00\x00\x13\x00\x00\x00H\xe1\x8a@'))
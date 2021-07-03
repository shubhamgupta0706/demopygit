fRead = open('Data', 'r') # Read Mode
print(fRead.readlines())
# fRead = open('Data', 'w') # Write Mode
fWrite = open('MyData', 'a')  # Append Mode
# fWrite.write('\nTarun Dubey')
# fWrite.write('\nVipin Shrivatri')


for data in fRead:
    fWrite.write(data)

dataTuples = (1,4,6,7,1,3)
print(dataTuples)
print(dataTuples.count(1))

print(dataTuples.index(1))

dataSet = {1,2,4,4,6,88,5}
print(dataSet)
dataSet.remove(1)
dataSet.remove(88)
print(dataSet)
dataSet.add(75)
print(dataSet)

datDiri = {
    'nama' : 'Andrian',
    'nim' : 2201010289,
    'jurusan' : 'S1 Ilkom'
}
print(datDiri)
datDiri.update({
    'nama' : 'Andrian Cimen',
    'nim' : 1901050024,
    'jurusan' : 'D3 Sistem Informasi'
})
print(datDiri)

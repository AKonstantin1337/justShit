import re   
from collections import Counter

inputCipherText = "fwqzrmszrgxtorqnurtzkzernbnxtrl wgrnjrtwgrxmrl wgjriwervjrntormszrjmnejrqnurtzkzernbnxtrjsxtzrnjrtwgrmszurjsxtzr wtbrlziwezrwfmwlzerezmvetjrjznjrwirl wworgx  "

inputData = open("./Six-Centuries-of-English-Poetry--Tennyson-to-Chaucer_30235/30235-8.txt", "r")
test = 51

normalData = []
neededData = [4, 3, 4, 3, 5, 5, 4, 2, 3, 2, 5, 3, 2, 3, 3]

for line in inputData:
    if test == 50:
        break
    else:
        test += 1
        for word in line.split():
            normalData.append([len(re.sub('[.,;:\'\"0-9\{\}")(!]', '', word.lower())), word])

myincrement = 0
output = []
shit = []

counter = Counter(inputCipherText)
for x in counter.most_common():
    tmp = inputCipherText.replace(x[0], "#")
    tmp2 = []
    for y in tmp.split("#"):
        tmp2.append(len(y))

    shit.append([counter[x], tmp, tmp2])

for x in shit:
    print(x)

#for x in normalData:
#    if x[0] == neededData[myincrement]:
#        myincrement += 1
#        output.append(x)
#    else:
#        kek = ''
#        if len(output) >= 5:
#            for x in output:
#                kek += x[1] + ' '
#            print(kek)
#        myincrement = 0
#        output = []
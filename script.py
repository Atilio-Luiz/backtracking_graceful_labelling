from doctest import REPORT_UDIFF
from re import X
import sys
import ast
from tempfile import tempdir

file_out = open("best.txt", 'w')
file_in = open('labellings.txt')

edges = file_in.readline().rstrip('\n')
a = []
max = -1
def maximum(list):
    max = list[0]
    for e in list:
        if (e> max ):
            max = e
    return max
while edges:
    eliabe = ast.literal_eval(edges)
    tempMax = []
    for e in eliabe:
        tempMax.append(int(e))
    a.append(tempMax)
    edges = file_in.readline().rstrip('\n')

i =0 
max = maximum(a[0])
tempMaxS = 0
for lista in a :
    if(maximum(lista) < max):
        i = tempMaxS
        max = maximum(lista)
    tempMaxS = tempMaxS+1
print("Rotulação ótima ", a[i])
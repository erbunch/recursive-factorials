#!/usr/bin/env python

import sys


class Aubie:

    def __init__(self, data, seq):
        self._gene = data
        self._seq = seq
        self._ID = self.samID()
        self._phenotype = self.phenotype()
        self._date = self.date()
        return

    def samID(self):
        ID = self._gene.split('_')
        return ID[0].split('>')

    def date(self):
        ID = self._gene.split('_')
        date = ID[1].split(' ')
        return date[0]

    def phenotype(self):
        ser = ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC']
        arg = ['AGA', 'AGG', 'CGU', 'CGC', 'CGA', 'CGG']
        phenotype = ''
        for element in ser:
            if self._seq[9:12] == element:
                phenotype = 'orange'
        for element in arg:
            if self._seq[9:12] == element:
                phenotype = 'blue'
        return phenotype




def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)

def freq(k, n, p):
    q = float(p) - 1
    top = factorial(n)
    bottom = factorial(n-k) * factorial(k)
    frac = top/bottom
    mult = float(p)**float(k)
    mult2 = q**(n-k)
    ans = frac * mult * mult2
    return ans

def main():
    with open(sys.argv[1], 'r') as fasta:
        with open(sys.argv[3], 'w') as output:
            p = sys.argv[2]
            data_list = []
            seq_list = []
            kb = 0
            ko = 0
            for line in fasta:
                if line[0] == '>':
                    data_list.append(line)
                else:
                    seq_list.append(line)
            #print(len(seq_list))
            #print(len(data_list))
            obj_list = []
            for i in range(len(data_list)):
                obj = Aubie(data_list[i], seq_list[i])
                obj_list.append(obj)
            for obj in obj_list:
                if obj._phenotype == 'blue':
                    kb += 1
                elif obj._phenotype == 'orange':
                    ko += 1
            n = len(obj_list)
            ans = freq(5, 32, p)
            s = "Results \n\n p (the frequency of \'orange\' in the population) = " + str(p) + '\n' + "n (the number of sampled individuals) = " + str(n) + '\n' + "k (the number of \'orange\' individuals in the sample set) = " + str(ko) + '\n' + "Probability of collecting 32 individuals with 5 being \"orange\" (given a population frequency of 0.3) = " + str(ans)
            output.write(s)

main()






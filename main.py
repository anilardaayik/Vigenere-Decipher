#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:25:06 2022

@author: anilardaayik
"""
lowercase = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
         'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16,
         'r':17, 's':18,  't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
         'z':25}

inv_lowercase = {0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i',
         9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q',
         17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y',
         25:'z'}

letterFrequency = {'e' : 12.7,
't' : 9.1,
'a' : 8.2,
'o' : 7.5,
'i' : 7.0,
'n' : 6.7,
's' : 6.3,
'h' : 6.1,
'r' : 6.0,
'd' : 4.3,
'l' : 4.0,
'u' : 2.8,
'c' : 2.8,
'm' : 2.4,
'w' : 2.3,
'f' : 2.2,
'g' : 2.0,
'y' : 2.0,
'p' : 1.9,
'b' : 1.5,
'v' : 1.0,
'k' : 0.8,
'j' : 0.2,
'x' : 0.1,
'z' : 0.1,
'q' : 0.1 }

def divisor(letterlist, keylength, remainder):
    coeff = 0
    sublist = []
    while coeff*keylength+remainder < len(letterlist):
        sublist.append(letterlist[coeff*keylength+remainder])
        coeff += 1
        
    return sublist

def frequency_calculator(letterList):
    
    frequency = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,
         'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,
         'r':0, 's':0,  't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0,
         'z':0}

    for letter in letterList:
        frequency[letter] = frequency.get(letter) + 1

    lettercount = 0                
    for element in frequency.values():
        lettercount += element
        
    result = 0
    for letter in frequency.keys():
        ratio = frequency.get(letter)/lettercount
        result += ratio*ratio
        
    return result


#textt = "Fwg atax: P’tx oh li hvabawl jwgvmjs, nw fw tfiapqz lziym, rqgv uuwfpxj wpbk jxlnlz fptf noqe wgw. Qoifmowl P bdg mg xv qe ntlyk ba bnjh vcf ekghn izl fq blidb eayz jgzbwx sqwm lgglbtqgy xlip. Pho fvvs ktf C smf ur ecul ywndxlz uv mzcz xxivw? Qomdmowl P bgzg, oblzqdxj C swas, B kyl btm udujs dcbfm vn yg eazl, pqzx, oblzq Q’ow mwmzb lg ghvk gxslz, emamwx apqu, wwmazagxv nomy bhlustk. Ghm qvv’f nbfx h vqe vgoubdg, pgh’a nuvw shvbtmk kbvzq. Baam jqfg pafs ixetqm wcdanw svc. Kwn’df dixs mzy ziym llllmfa, zjid wxl bf nom eifw hlqspuglowall, loyv sztq cu btmlw mhuq phmmla. Kwn’df htiirk yul gx bf noqe kbls. Kwz’b agjl naz mzcuoe mekydpqzx: lblzq’a gg moqb nhj svc, fpxjy’z va zhsx. Uwi basn fwg’dx ouzbql rgoy tunx zyym, uv mzcz ayied wvzzmk, qib’dq lxknywkmw an ldqzroblzq qg lbl eazev."
text = input().lower().strip()
wordList = text.split()
letterList = []
characterList = [] 


for word in wordList:
    for letter in word:
        if letter not in lowercase:
            continue
        letterList.append(letter)
        
        
for word in wordList:
    for character in word:
            characterList.append(character)
    

freqlist = {}
#II limited the keylength from above as if the keylength gets bigger it will become
#almost impossible to apply frequency analysis
for keylength in range(2, 20):
    moduledLetterList = divisor(letterList, keylength, 0)
    freq_sum = frequency_calculator(moduledLetterList)
    freqlist[keylength] = freq_sum    

values = []
for element in freqlist.values():
    values.append(element)

maxindex = values.index(max(values))
keylength = maxindex + 2


def key_finder(wordList):
    frequency = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0,
             'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0,
             'r':0, 's':0,  't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0,
             'z':0}
    analysis = {}
    for element in wordList:
        length = len(element)
        for i in range(length):
            letter = element[i]
            if letter in lowercase:
                frequency[letter] = frequency.get(letter) + 1

    lettercount = 0                
    for element in frequency.values():
        lettercount += element

    for key in range(26):
        result = 0
        for harf in lowercase.keys():
            value = lowercase.get(harf) + key 
            value = value % 26
        
            newharf = inv_lowercase.get(value)  
            product = letterFrequency.get(harf)/100 * frequency.get(newharf)/lettercount
            result += product
        analysis[key] = result
    
    differences = {}
    inv_differences = {}
    for key in analysis.keys():
        if analysis.get(key) < 0.065:
            differences[key] = 0.065 - analysis.get(key)
            inv_differences[differences.get(key)] = key
        else:
            differences[key] = analysis.get(key) - 0.065
            inv_differences[differences.get(key)] = key

    minimal = min(differences.values())
    realkey = inv_differences.get(minimal)
    uzunluk = len(wordList)

    for index in range(uzunluk):
        realindex = lowercase.get(wordList[index]) - realkey
        if realindex < 0:
            realindex = realindex + 26
        
        wordList[index] = inv_lowercase.get(realindex)
                           
    return realkey

reelkey = ""
for remainder in range(keylength):
    moduledList = divisor(letterList, keylength, remainder)
    key = key_finder(moduledList)
    reelkey += inv_lowercase.get(key)
    for index in range(remainder, len(letterList), keylength):
        otherindex = int((index-remainder)/keylength)
        
        letterList[index] = moduledList[otherindex]
        
plaintext = ""
for letter in letterList:
    plaintext += letter

reeltext = ""
totalindex = 0
for word in wordList:

    harfler = 0
    for i in range(len(word)):
        if word[i] in lowercase:
            harfler += 1
    other = len(word) - harfler
    
    realWord = plaintext[totalindex:totalindex+harfler] + " "
    totalindex += harfler
    
    for i in range(len(word)):
        if word[i] not in lowercase:
            realWord = realWord[0:i] + word[i] + realWord[i:len(word)]
     
    reeltext += realWord

print(reelkey)
print(reeltext)
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
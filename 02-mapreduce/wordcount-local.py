#!/usr/bin/python

import sys
import glob

import codecs

inputdir="."

if len(sys.argv) >= 1:
	inputdir = sys.argv[1]

def processdir(dir):

    dirList = glob.glob(dir)
    wordcount={}
    for f in dirList:
        wordcountfile(f,wordcount)
    for w in wordcount:
        print(w,wordcount[w])


def wordcountfile(f, wordcount):
    try:
        file = codecs.open(f, "r", "utf-8")
        for word in file.read().split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        file.close()
    except UnicodeDecodeError:
        print('error abriendo archivo=',f)      
    return wordcount        

processdir(inputdir)
# -*- coding: utf-8 -*-
import os, sys, pickle
import numpy as np
import binascii
from sklearn.metrics.pairwise import cosine_similarity

"""
A MinHash-based near duplicate detection for the WLO dataset.

(based on a tutorial on MinHash https://github.com/chrisjmccormick/MinHash)
"""

class Prediction:

	docNames, docs, signatures, arr, coeffA, coeffB = None, None, None, None, None, None
	docsAsShingleSets = None

	numHashes=100

	def __init__(self):

		with open('../data/hashes.p', 'rb') as f:
			self.signatures = pickle.load(f)

		with open('../data/docnames.p', 'rb') as f:
			self.docNames = pickle.load(f)

		with open('../data/docs.p', 'rb') as f:
			self.docs = pickle.load(f)

		with open('../data/coeffa.p', 'rb') as f:
			self.coeffA = pickle.load(f)

		with open('../data/coeffb.p', 'rb') as f:
			self.coeffB = pickle.load(f)

#		with open('./data/shingles.p', 'rb') as f:
#			self.docsAsShingleSets=pickle.load(f)

		self.arr = np.array(self.signatures)


	def shingleWords(self, words): # has to be the same method as for hash creation
		shinglesInDoc = set()
		words = [x.replace('\n','') for x in words if x]
		for index in range(0, len(words) - 2):
			shingle = words[index] + " " + words[index + 1] + " " + words[index + 2]
			crc = binascii.crc32(shingle.encode()) & 0xffffffff
			shinglesInDoc.add(crc)
		return shinglesInDoc

	def getSignature(self, shingleIDSet): # has to be the same method as for hash creation
		signature = []
		nextPrime = 4294967311

		for i in range(0, self.numHashes):
			minHashCode = nextPrime + 1

			for shingleID in shingleIDSet:
				hashCode = (self.coeffA[i] * shingleID + self.coeffB[i]) % nextPrime 
			
				if hashCode < minHashCode:
					minHashCode = hashCode

			signature.append(minHashCode)
		return signature


	def run(self, text):
		shingles = self.shingleWords(text.split())
		sig = self.getSignature(shingles)

		dists = cosine_similarity(self.arr , [sig])
		sorted_arg = np.argsort(dists.ravel())

		closest = reversed(sorted_arg[-10:])
		#print(sorted_arg[-10:])
		result=[]

		for d in closest:
			#print (d, dists[d])
			#print (self.docNames[d])
			#print (" ".join(self.docs[self.docNames[d]]))
			#print ("----")
			if (dists[d][0]>0.8):
				result.append([self.docNames[d], dists[d][0], " ".join(self.docs[self.docNames[d]])])

		return result



if __name__ == '__main__':	

	text = sys.argv[1]

	print ("Searching near duplicates for: '" + text + "'")

	r = Prediction()
	for r in r.run(text):
		print (r)




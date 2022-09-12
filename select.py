import heapq
import random

file = open("word.txt", encoding="utf8")
l = file.readlines()
w = dict()
for word in l:
	#print(word)
	toks = word.split(":", 1)
	if(len(toks) != 2):
		print("\nword wrong format : ", word)
		print()
	else:
		eng = toks[0].strip()
		chi = toks[1].strip()
		w[eng] = chi
w2 = []
for k in w.keys():
	w2.append([k, w[k]])
w = w2
#print(w)
print("\ntotal number of words : ", len(w))
print()
a = 0
b = 0
c = 0
while True:
	r = input("select the range of words you want to recite (enter two numbers): ")
	rtoks = r.split(" ")
	rtoks2 = r.split(",")
	if(len(rtoks) != 2 and (len(rtoks) != 3 or rtoks[1] != ',') and (len(rtoks) != 1 or len(rtoks2) != 2)):
		print("\nre-enter your input\n")
	else:
		if(len(rtoks) == 3):
			rtoks.pop(1)
		if(len(rtoks) == 1):
			rtoks = rtoks2
		v1 = rtoks[0].strip(",")
		v2 = rtoks[1].strip(",")
		a = int(v1)
		b = int(v2)
		if(a < 1):
			print("\nfirst number too small, should be >= 1\n")
		elif(a > len(w)):
			print("\nfirst number too large\n")
		elif(b < 1):
			print("\nsecond number too small, should be >= 1\n")
		elif(b > len(w)):
			print("\nsecond number too large\n")
		elif(a > b):
			print("\nfirst number should not be larger than the second\n")
		else:
			break
while True:
	r = input("\nenter the number of words you want to recite this time: ")
	c = int(r)
	if(c < 0):
		print("\nvalue can't be negative\n")
	elif(c > b - a + 1):
		print("\nasked for more words than present in the selected range\n")
	else:
		break
a -= 1
b -= 1

w2 = []
for i in range(a, b + 1):
	w2.append(w[i])
w = w2

w2 = []
visited = set()
for ww in w:
	while True:
		rand = random.randint(0, 1000 * len(w))
		if rand not in visited:
			visited.add(rand)
			w2.append([rand, ww[0], ww[1]])
			break
wall = w2
heapq.heapify(wall)

while True:
	w = []
	for i in range(c):
		w.append(heapq.heappop(wall))
	print("\n\n\n")
	for ww in w:
		print(ww[1], "\n")
		input("Your Answer: ")
		print()
		print("Correct Answer:", ww[2])
		print("\n\n\n")

	if(len(wall) == 0):
		print("\ndone\n")
		break
	print(len(wall), end = "")
	r = input(" words remaining. Want to continue reciting the rest of the words (1 for yes, 0 for no)? ")
	r = int(r)
	if(r == 0):
		break
	else:
		print()
		while True:
			r = input("how many do you want to recite this time? ")
			r = int(r)
			if(r <= 0):
				print("\nneed positive number of words\n")
			elif(r > len(wall)):
				print("\nasked for more words than present in the selected range\n")
			else:
				print()
				c = r
				break





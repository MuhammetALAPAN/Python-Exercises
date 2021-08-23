freq = {}

s = input()
for word in s.split():
    freq[word] = freq.get(word, 0) + 1

words = dict(sorted(freq.items()))

for word in words:
    print("%s:%d" % (word,words[word]), end=" ")

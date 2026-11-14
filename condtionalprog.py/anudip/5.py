sentence = "Python is great, Python is fast! Python is easy."

# 1. Punctuation hatayein aur lowercase karein
for punctuation in "!,.:;?":
    sentence = sentence.replace(punctuation, "")
sentence = sentence.lower()

# 2. Words ki list banayein
words = sentence.split()

# 3. Simple loop se count karein
freq = {}
for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

# 4. Result print karein
print(freq)
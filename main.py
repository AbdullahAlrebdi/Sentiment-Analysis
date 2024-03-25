with open("words_positive.txt") as f:
    positive_words = []
    for line in f:
        positive_words.append(line.rstrip())


with open("words_negative.txt") as f:
    negative_words = []
    for line in f:
        negative_words.append(line.rstrip())


with open("words_positive.txt") as f:
    positive_words = []
    for line in f:
        positive_words.append(line.rstrip())
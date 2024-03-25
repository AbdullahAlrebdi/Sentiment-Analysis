with open("words_positive.txt") as f:
    positive_words = []
    for line in f:
        positive_words.append(line.rstrip())


with open("words_negative.txt") as f:
    negative_words = []
    for line in f:
        negative_words.append(line.rstrip())
        
        
with open("tweets.txt") as f:
    tweets = []
    for line in f:
        if line.rstrip() == '':
            continue
        tweets.append(line.rstrip())
        

# print(tweets[0].split())


# {positve: 1, negative: 0}
# {postive 0, negative: 12}


def neg_pos(tweets, negative_words, positive_words):
    splited_tweet = ''
    my_dic = {"tweet": '', 'positve': 0, "negative": 0}
    reslut_list = []

    for tweet in tweets:
        splited_tweet = tweet.split()
        my_dic['tweet'] = tweet
        
        for i in splited_tweet:
            if i in positive_words:
                my_dic['positve'] += 1
            elif i in negative_words:
                my_dic['negative'] += 1
                
        reslut_list.append(my_dic)
        my_dic['positve'] = 0
        my_dic['negative'] = 0
    return reslut_list
    

print(neg_pos(['my name is good'], ['bad', 'awful'], ['good', 'exlennt']))
        
        
    
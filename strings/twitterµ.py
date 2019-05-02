tweet = input('geef tweet: ')

i_hashtag = tweet.find('#')
while i_hashtag != -1:
tweet = tweet[(i_hashtag)+1:]
i_spatie = tweet.find(' ')

print(tweet[:i_spatie])
i_hasthag = tweet.find('#')

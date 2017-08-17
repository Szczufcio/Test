from collections import Counter

text = 'The Kali mini ISO is a convenient way to install a minimal Kali system and install it from scratch. The mini install ISO will download all required packages from our repositories, meaning you need to have a fast Internet connection to use this installation method.'

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
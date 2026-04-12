fruit_list = ["Banana", "Mango", "Apple", "Grapse", "Pineapple"]



def longest_words(words):
    longest = fruit_list[0]
    for word in words:
        if len(longest)< len(word):
            longest = word
    return longest
longest = longest_words(fruit_list)

print(longest) #interpreter hai isliy line by line read krega code ko

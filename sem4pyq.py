
# s = "MANGO"
# n = 9
# def removenth(s, n):
#    if n >= len(s):
#       return s
   
#    else:
      
#       return s[:n] +s[n+1:]
   

# print(removenth(s, n))



# words = input("Enter words separated by comma:")
# Accept input from user
words = input("Enter comma-separated words: ")

# Split the words by comma and strip extra spaces
word_list = [word.strip() for word in words.split(",")]


print(word_list)
# Sort the list alphabetically
word_list.sort()

# Join back into a comma-separated string
sorted_words = ", ".join(word_list)

# Print the result
print(sorted_words)
print(type(sorted_words))
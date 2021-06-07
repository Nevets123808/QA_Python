def near(word1, word2):
    for index, letter in enumerate(word1):
        new_word = word1[:index] + word1[index+1:]
        result = False
        if new_word == word2:
            result = True
            break
    return result


print(near("hello","hell"))
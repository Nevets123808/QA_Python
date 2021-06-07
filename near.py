def near(word1, word2):
    for index, letter in enumerate(word1):
        new_word = word1[:index] + word1[index+1:]
        result = False
        if new_word == word2:
            result = True
            break
    print(result)


print("near(\"reset\", \"rest\")")
near("reset", "rest")

print("near(\"dragoon\", \"dragon\")")
near("dragoon", "dragon")

print("near(\"eave\", \"leave\")")
near("eave", "leave")

print("near(\"sleet\", \"lets\")")
near("sleet", "lets")
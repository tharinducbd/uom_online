# Strings
word = "Hello " 'world!'    # 'Nearby concatenation'
print(word)

word = "Life, Universe, and Everything"
print(word[6])
print(word[6:])
print(word[6:14])

print(word[-1::-1])
print(word[-10:])

print(word[:-16])

# Membership operator
print(("U" in word))
print(("X" in word))

# Raw strings: to suppress Escape characters
print(r"\n")

# String formattings
print("My name is %s and I am %d years old!" % ('Marvin', 2000))

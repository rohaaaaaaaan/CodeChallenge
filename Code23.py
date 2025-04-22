# Function to check if a word is abecedarian
def is_abecedarian(word):
    return list(word) == sorted(word)

# List of sample words to test
words = input("Enter words separated by spaces: ").split()

# Count abecedarian words and print each word with "true" or "false"
count = 0
for word in words:
    result = is_abecedarian(word)
    print('true' if result else 'false')
    if result:
        count += 1

# Final count of abecedarian words
print(f"\nNumber of abecedarian words: {count}")

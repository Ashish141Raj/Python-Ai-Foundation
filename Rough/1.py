# numbers = [1,2,3,4,5,6,7,8,9]
# result = [(n,'even') if n % 2 == 0 else (n,'odd') for n in numbers]
# print(result)

words = ['tree', 'sky', 'mountain', 'river', 'cloud', 'sun']

def is_long_word(word):
    return len(word) > 4

long_words = list(filter(is_long_word, words))
print(long_words) # ['mountain', 'river', 'cloud']

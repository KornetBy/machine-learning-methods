"""
Два слова являются анаграммами, если состоят из одинаковых букв.
Например, анаграммами являются слова "binary" и "brainy", или "раздвоение"
и "дозревание"
"""
def are_anagrams(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if are_anagrams(word1, word2):
    print(f"'{word1}' и '{word2}' являются анаграммами ")
else:
    print(f"'{word1}' и '{word2}' не являются анаграммами ")

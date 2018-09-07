def disemvowel(word):
  
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word_list = list(word)

    for vowel in vowels:
        while True:
            try:
                word_list.remove(vowel)
            except ValueError:
                break


    return ''.join(word_list)

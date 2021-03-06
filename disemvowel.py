# === Instructions ===
# OK, I need you to finish writing a function for me. The function disemvowel takes a single 
# word as a parameter and then returns that word at the end. 
# I need you to make it so, inside of the function, all of the vowels ("a", "e", "i", "o", and 
# "u") are removed from the word. Solve this however you want, it's totally up to you!
# Oh, be sure to look for both uppercase and lowercase vowels!

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

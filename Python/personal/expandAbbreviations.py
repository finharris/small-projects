def properfySentence(txt, shortcuts, full_words):
    words = txt.split(' ') # split the sentence into an array of words

    for word in words: # loop through the words...
        if word in shortcuts: # and check if the word is in the shortcuts
            words[words.index(word)] = full_words[shortcuts.index(word)] # replace the shortcut with the full length word

    txt_changed = ' '.join(words) # rejoin the words with spaces
    
    return txt_changed # return the result



def main():
    
    shortcut_word = ["js", "fb", "p"]

    properly_word = ["Javascript", "Facebook", "Python"]

    txt = "I like js and i use fb"

    print(
        properfySentence(txt,shortcut_word,properly_word)
    )


if __name__ == "__main__":
    main()
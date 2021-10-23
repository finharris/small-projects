while True:
    eng = ["Hello", "Good", "Yes", "Library", "Goodbye"]
    fre = ["Bonjour", "Bon", "Oui", "Bibliotheque", "Au revoir"]
    userinp = str(input("Word: "))

    for i in range(len(eng)):
        if userinp == eng[i]:
            print(fre[i], "\n")

    # if eng.index(userinp) == 0:
    #     print(fre[0])
    # elif eng.index(userinp) == 1:
    #     print(fre[1])
    # elif eng.index(userinp) == 2:
    #     print(fre[2])
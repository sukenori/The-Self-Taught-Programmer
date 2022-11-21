def hangman(word):
    letters=list(word)
    board=["_"]*len(word)
    wrong=0
    stages=["__________",
            "|      |  ",
            "|      |  ",
            "|      O  ",
            "|     /|\ ",
            "|     / \ ",
            "|         ",
            "|_________"]
    while "_" in board:
        char=input("予想した文字を入力してください ")
        if char in letters:
            i=letters.index(char)
            letters[i]="$"
            board[i]=char
            print("".join(board)+"\n")
        else:
            wrong+=1
            print("".join(board))
            print("\n".join(stages[0:wrong])+"\n")
            if wrong==len(stages):
                print("あなたの負けです")
                print("正解は"+word)
                break
    else:
        print("あなたの勝ちです")

hangman("cat")
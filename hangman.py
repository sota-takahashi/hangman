#! python3
# hangman

def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   "
              "|         |         "
              "|         ○         "
              "|        /|\        "
              "|        / \        "
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print('ハングマンへようこそ！')

    while True:
        print('答えは{}です'.format(board))
        print('解答を入力してください:')
        answer = input()
        aletters = list(answer)

        if answer == word:
            win = True
            return True
            break

        for i in aletters:
            try:
                board[rletters.index(i)] = i
                break
            except:
                continue

        wrong += 1
        for i in range(wrong):
            print("{}\n".format(stages[i]))

        if wrong > len(stages):
            return win
            break



result = hangman('partner')

if result == True:
    print('YOU WIN!')
else:
    print('YOU LOSE!\nなんで負けたか，明日までに考えといてください。ほな、いただきます！')

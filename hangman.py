def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ['_'] * len(word)
    win = False  #最後に負けを表示するif文で使う
    print('ハングマンへようこそ！')  #スタート画面

    while wrong < len(stages) - 1:
        print("\n")  #スタート画面の見やすさのために改行
        msg = '1文字を予想'  #スタート画面
        char = input(msg)  #回答をcharに代入
        if char in rletters:
            cind = rletters.index(char)  #回答した文字をrlettersの中から選んで、そのインデックス値をcindに代入する
            board[cind] = char  #スコアボードの正しい位置に回答を代入する
            rletters[cind] = '$'  #rletters内の回答した文字を$に変えて、ダブりに対応する
        else:
            wrong += 1
        
        print(" ".join(board))  #スコアボードを画面へ出力する
        
        e = wrong + 1  #リストの終了インデックス値は、指定した値-1までしかスライスされない

        print("\n".join(stages[0:e]))  #ミスの度にハングマンのリストを一つずつ出力する
        
        if '_' not in board:  #正解で"_"埋まる
            print('あなたの勝ち！')
            print(" ".join(board))  #正解したスコアボードを改めて画面に出力する
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong+1]))  #ハングマン完成形を改めて出力
        print('あなたの負け！正解は{}'.format(word))


hangman('cat')
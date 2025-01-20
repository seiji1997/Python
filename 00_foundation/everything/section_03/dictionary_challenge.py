age = int(input("何歳ですか？:"))
casino_age = 18

game_dict = {'1': 'ルーレット', '2': 'ブラックジャック', '3': 'ポーカー'}

if age >= casino_age:
    print("どうぞお入りください")
    while True:
        print("プレイするゲームを選択してください")
        for num, game_name in game_dict.items():
            print(f"{num}: {game_name}")
        game = input(":")
        if game in game_dict:
            print(f"あなたは{game_dict[game]}を選びました")
            break
        else:
            print("1~3を選んでください")
else:
    print(f"{casino_age}歳未満の方はカジノへは入れません！")

try:
    # tryの中で特定のErrorをraiseすることで，
    # TODO 後で削除する
    raise ValueError("raise ValueError for test")
except ValueError:
    # exceptを実行することができる
    print("Do something")
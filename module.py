import random

PLAYER_STATE = {
    "hp": [20, 30, 50, 70, 85, 100],
    "atk": [5, 8, 10, 15, 20, 30],
    "lv": 1,
    "needExp": [
        10, 100, 150, 200, 250, 000
    ]
}

ENEMY_INFO = {
    "phase1": [
        {
            "name": "スライム",
            "hp": 10,
            "atk": 3,
            "exp": 10,
            "discription": "青い物体。くそ雑魚"
        },
        {
            "name": "スライムベス",
            "hp": 15,
            "atk": 5,
            "exp": 20,
            "discription": "スライムのオレンジ版、強さはそこまで"
        },
        {
            "name": "おおきづち",
            "hp": 20,
            "atk": 7,
            "exp": 40,
            "discription": "大きな棍棒を持っている。殴られると痛そう"
        }
    ]
}

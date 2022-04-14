import random

PLAYER_STATE = {
    "hp": [20, 30, 50, 70, 85, 100],
    "atk": [10, 20, 30, 40, 50, 60],
    "lv": 1,
    "needExp": [
        50, 100, 150, 200, 250, 000
    ]
}

ENEMY_INFO = {
    "phase1": [
        {
            "name": "スライム",
            "hp": 10,
            "dmg": random.randint(1, 5),
            "exp": 5,
        },
        {
            "name": "ゴブリン",
            "hp": 20,
            "dmg": random.randint(5, 10),
            "exp": 10
        }
    ]
}

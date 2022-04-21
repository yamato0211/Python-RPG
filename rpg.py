import random
import sys
import module
import time
import playsound

current_user_lv = module.PLAYER_STATE["lv"]
leved_hp = module.PLAYER_STATE["hp"][current_user_lv-1]
current_user_state = {
    "hp": module.PLAYER_STATE["hp"][current_user_lv-1],
    "atk": module.PLAYER_STATE["atk"][current_user_lv-1],
    "needExp": module.PLAYER_STATE["needExp"][current_user_lv-1]
}


def update_user_state():
    current_user_state = {
        "hp": module.PLAYER_STATE["hp"][current_user_lv-1],
        "atk": module.PLAYER_STATE["atk"][current_user_lv-1],
        "needExp": module.PLAYER_STATE["needExp"][current_user_lv-1]
    }
    return current_user_state


enemy_info = {}


def show_state():
    print("==============================================")
    print(f"{user_name}")
    print("職業: 勇者")
    print("Lv: " + str(current_user_lv))
    print("hp: " + str(leved_hp) +
          " / " + str(current_user_state["hp"]))
    print("atk: " + str(current_user_state["atk"]))
    print("次のレベルまで " + str(current_user_state["needExp"]) + "exp")
    print("==============================================")


def what_do(user):
    print("***** "+user + " " + "Lv:" +
          str(current_user_lv) + " *******************************")
    print("1. 敵と戦う")
    print("2. 強さを見る")
    print("3. 休む")
    print("4. 進む(敵が強くなるので注意してください)")
    print("5. ゲームをやめる(セーブはできません)")
    return input("何をする? : ")


def create_enemy():
    enemy = module.ENEMY_INFO["phase1"][random.randint(
        0, len(module.ENEMY_INFO["phase1"])-1)].copy()
    print("==============================================")
    time.sleep(2)
    print(enemy["name"] + "が現れた!")
    time.sleep(2)
    return enemy


def battle():
    global leved_hp, current_user_lv, current_user_state
    while leved_hp > 0 and enemy_info["hp"] > 0:
        print("==============================================")
        print(user_name + ": " + str(leved_hp) +
              " / " + str(current_user_state["hp"]))
        print("1. 攻撃")
        print("2. 調べる")
        print("3. 逃げる")
        selected_act = input("何をする？")
        if selected_act == "1":
            print(user_name + "の攻撃!")
            playsound.playsound("bgm/atack.mp3")
            dmg_to_ene = current_user_state["atk"] + random.randint(-3, 3)
            print(enemy_info["name"] + "に" + str(dmg_to_ene) + "のダメージ")
            enemy_info["hp"] = enemy_info["hp"] - dmg_to_ene
            time.sleep(1.5)
            if enemy_info["hp"] > 0:
                print(enemy_info["name"] + "の攻撃！")
                playsound.playsound("bgm/enemy1.wav")
                playsound.playsound("bgm/enemy2.wav")
                dmg_to_user = enemy_info["atk"] + random.randint(-2, 2)
                print(user_name + "に" + str(dmg_to_user) + "のダメージ")
                leved_hp = leved_hp - dmg_to_user
                time.sleep(1.5)
            else:
                continue
        elif selected_act == "2":
            time.sleep(0.5)
            print("==============================================")
            print("敵名: " + enemy_info["name"])
            print("説明: " + enemy_info["discription"])
            print("==============================================")
            continue
        elif selected_act == "3":
            time.sleep(1)
            playsound.playsound("bgm/escape.wav")
            print(user_name + "は逃げ出した。")
            time.sleep(2)
            return
    if leved_hp <= 0 and enemy_info["hp"] > 0:
        time.sleep(2)
        print(user_name + "は敗北した")
        playsound.playsound("bgm/lose.mp3")
        print("勇者よ死んでしまうとは情けない。")
        time.sleep(2)
        print("最初からやり直しですね。乙")
        time.sleep(2)
        sys.exit()
    elif leved_hp > 0 and enemy_info["hp"] <= 0:
        playsound.playsound("bgm/victory.mp3")
        print(enemy_info["name"] + "を倒した!")
        time.sleep(1)
        print(str(enemy_info["exp"]) + "の経験値を獲得!")
        current_user_state["needExp"] = current_user_state["needExp"] - \
            enemy_info["exp"]
        time.sleep(2)
        if current_user_state["needExp"] <= 0:
            playsound.playsound("bgm/LvUp.mp3")
            print("レベルアップ！")
            time.sleep(2)
            current_user_lv = current_user_lv + 1
            print(user_name + "は" + "Lv" + str(current_user_lv) + "に上がった!")
            current_user_state = update_user_state()
            time.sleep(1)
            return
        else:
            time.sleep(1)
            return


def rest():
    global current_user_state, leved_hp
    leved_hp = current_user_state["hp"]
    time.sleep(1.5)
    print(user_name + "は休憩した。")
    playsound.playsound("bgm/Bet.mp3")
    print("hpが全回復した！")
    time.sleep(1.5)


def Check_doing(doing):
    global enemy_info
    if doing == "1":
        enemy_info = create_enemy()
        battle()
    elif doing == "2":
        time.sleep(0.5)
        show_state()
    elif doing == "3":
        rest()
    elif doing == "4":
        pass
    elif doing == "5":
        sys.exit()


def game():
    while True:
        doing = what_do(user_name)
        Check_doing(doing)


print("テストRPGへようこそ！")
time.sleep(1)
print("ゲームを始めますか？")
doing = ""

start = input("1.はい　2.いいえ :  ")
if start == "2":
    print("帰れ！")
    sys.exit()


user_name = input("あなたの名前を入力してください : ")
time.sleep(1)
print("それではゲームを始めます")
time.sleep(1)
if user_name == "":
    user_name = "名無し"
game()

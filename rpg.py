import sys
import module

current_user_lv = module.PLAYER_STATE["lv"]
leved_hp = module.PLAYER_STATE["hp"][current_user_lv-1]
current_user_state = {
    "hp": module.PLAYER_STATE["hp"][current_user_lv-1],
    "atk": module.PLAYER_STATE["atk"][current_user_lv-1],
    "needExp": module.PLAYER_STATE["needExp"][current_user_lv-1]
}


def show_state():
    print("==============================================")
    print(f"{user_name}")
    print("職業: 勇者")
    print("Lv: " + str(module.PLAYER_STATE["lv"]))
    print("hp: " + str(leved_hp) +
          " / " + str(current_user_state["hp"]))
    print("atk: " + str(current_user_state["atk"]))
    print("次のレベルまで " + str(current_user_state["needExp"]) + "exp")
    print("==============================================")


def what_do(user):
    print("*****"+user + " " + "Lv:" +
          str(current_user_lv) + "*******************************")
    print("1. 敵と戦う")
    print("2. 強さを見る")
    print("3. 休む")
    print("4. 進む(敵が強くなるので注意してください)")
    print("5. ゲームをやめる(セーブはできません)")
    return input("何をする? : ")


def Check_doing(doing):
    if doing == "1":
        pass
    elif doing == "2":
        show_state()
    elif doing == "3":
        pass
    elif doing == "4":
        pass
    elif doing == "5":
        sys.exit()


def game():
    while True:
        doing = what_do(user_name)
        Check_doing(doing)


print("テストRPGへようこそ！")
print("ゲームを始めますか？")
doing = ""

start = input("1.はい　2.いいえ :  ")
if start == "2":
    print("帰れ！")
    sys.exit()

print("それではゲームを始めます")
user_name = input("あなたの名前を入力してください : ")
if user_name == "":
    user_name = "名無し"
game()

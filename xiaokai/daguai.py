import random
def gjz():
    gj = random.randint(0, 50)
    return gj
gjj = gjz()

def guard():
    player_hp = 100
    guard_hp = 80
    print("发现入侵者，兄弟们上，干掉他！\n玩家血量：100\n敌人血量：80")
    while player_hp > 0 and guard_hp > 0:
        user = input("三个怪物冲一起向了你,请选择攻击还是防守，A代表攻击，D代表防守>>>")
        if user == 'A':
            player_hp -= gjj
            print(f"玩家：{int(player_hp)}")
            guard_hp -= gjj
            print(f"敌人：{int(guard_hp)}")
        elif user == 'D':
            player_hp -= gjj * 0.5
            print(player_hp)
        if player_hp > 0 and guard_hp <= 0:
            print("胜")
        elif player_hp <= 0 and guard_hp > 0:
            print("负")
guard()

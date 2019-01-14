# 农民和士兵聚集在森林。
# 命令农民战斗，敌人滚蛋！

while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("战斗, " + friend.id + "!")
    # 寻找最近的敌人，然后让他们滚蛋
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.say("滚蛋,"+ enemy.id + "!")

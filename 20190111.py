# 在决斗中击败敌人的英雄！

while True:
    # 在一个循环中找到并攻击敌人
    # 当你完成的时候，提交到多人天梯系统中！
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.cleave(enemy)
    else:
        hero.attack(enemy)
    
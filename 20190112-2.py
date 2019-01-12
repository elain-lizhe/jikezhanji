while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # 如果他们与农民太近，就攻击他们
        hero.attack(enemy)
        pass
    # 否则的话，呆在农民旁边！使用else
    else:
        hero.moveXY(40, 37)
    
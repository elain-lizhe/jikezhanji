# 尽可能多地打败食人魔。
# 使用'cast'和'canCast' 来表示法术。


while True:
    enemy = hero.findNearestEnemy()
    if not enemy:
        pass
    elif hero.canCast("lightning-bolt", enemy):
        hero.cast("lightning-bolt", enemy)
    elif hero.canCast("chain-lightning", enemy):
        hero.cast("chain-lightning", enemy)
    elif enemy.type == "ogre":
        hero.moveXY(10, 44) 
    else:
        hero.cast("regen", hero)
    

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # hero.attack(enemy)
        hero.cleave(enemy)
    else:



item = hero.findNearestItem()
if item:
    # 移动到物品的位置。
    pos = item.pos
    x = pos.x
    y = pos.y
    hero.moveXY(x, y)
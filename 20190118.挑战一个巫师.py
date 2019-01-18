# 尽可能多地打败食人魔。
# 使用'cast'和'canCast' 来表示法术。

while True:
    if hero.canCast("lightning-bolt", hero.findNearestEnemy()):
        hero.cast("lightning-bolt", hero.findNearestEnemy())
    elif hero.canCast("chain-lightning", hero.findNearestEnemy()):
        hero.cast("chain-lightning", hero.findNearestEnemy())
    else:
        hero.cast("regen", hero.findNearestEnemy())
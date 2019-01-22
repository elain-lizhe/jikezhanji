# 尽可能多地打败食人魔。
# 使用'cast'和'canCast' 来表示法术。

for i in range(10):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

hero.cast("regen", hero)

for i in range(5):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)

for i in range(5):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)

for i in range(5):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.cast("regen", hero)

enemy = hero.findNearestEnemy()
hero.cast("chain-lightning", enemy)


for i in range(5):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.cast("regen", hero)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.cast("lightning-bolt", enemy)
        break;


hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.cast("regen", hero)

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.cast("chain-lightning", enemy)
        break;
        
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.cast("regen", hero)

for i in range(20):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
        
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.moveXY(16, 36)
hero.moveXY(17, 36)
hero.cast("regen", hero)

hero.moveXY(35, 31)
enemy = hero.findNearestEnemy()
if enemy:
    hero.cast("lightning-bolt", enemy)
    
hero.moveXY(17, 36)
hero.cast("regen", hero)
for i in range(4):
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

hero.cast("regen", hero)
hero.moveXY(12, 25)
hero.moveXY(10, 44)


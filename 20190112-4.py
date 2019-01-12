# 在这关，别碰恶魔石！往其他方向移动避开它们！
while True:
    evilstone = hero.findNearestItem()
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:     # == means "is equal to"
            # 如果恶魔石在左边，走到右边。
            hero.say("右边")
            pass
        else:
            # 如果恶魔石在右边，走到左边。
            hero.say("左边")
            pass
    else:
        # 如果没有恶魔石，那就去到中间。
        hero.say("中间")
        pass

# 移到'Laszlo'并得到他的秘密号码。
hero.moveXY(30, 13)
las = hero.findNearestFriend().getSecret()

# 向 Laszlo 的数字中加7就能得到 Erzsebet的号码
# 移到'Erzsebet'并说出她的魔法数字。
erz = las + 7
hero.moveXY(17, 26)
hero.say(erz)

# 将 Erzsebet 的数字除以 4 得到 Simoyi 的数字。
# 去'Simony'并告诉他他的电话号码。
sim = erz / 4
hero.moveXY(30, 39)
hero.say(sim)
# 将 Simonyi 的数字乘以 Laszlo 的数字得到 Agata 的数字。
aga = sim * las
hero.moveXY(43, 26)
hero.say(aga)
# 去'Agata'并告诉她她的电话号码。


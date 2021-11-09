weapons=[]

xpos=10
ypos=10

weapon_speed=2

weapons.append([xpos,ypos])
print(weapons)

weapons=[ [w[0],w[1]-weapon_speed] for w in weapons]
print(weapons)
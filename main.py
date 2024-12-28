import pygame
import math
width = 640
height = 400
renderDistance = 20
speed = 0.03
speedRun = 0.1
wallRadius = 0.1
scale = 8
surface = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()


def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
def writeTxt(texst):
	txt = font.render(str(texst), 1, pygame.Color("coral"))
	return txt

#walls = ['100,102:101,102', '101,102:101,103', '100,102:100,103', '100,103:101,103', '101,102:102,102', '102,102:102,103', '101,102:101,103', '101,103:102,103', '102,102:103,102', '103,102:103,103', '102,102:102,103', '102,103:103,103', '105,102:106,102', '106,102:106,103', '105,102:105,103', '105,103:106,103', '105,103:106,103', '106,103:106,104', '105,103:105,104', '105,104:106,104', '105,104:106,104', '106,104:106,105', '105,104:105,105', '105,105:106,105', '105,105:106,105', '106,105:106,106', '105,105:105,106', '105,106:106,106', '103,108:104,108', '104,108:104,109', '103,108:103,109', '103,109:104,109', '104,108:105,108', '105,108:105,109', '104,108:104,109', '104,109:105,109', '105,108:106,108', '106,108:106,109', '105,108:105,109', '105,109:106,109', '106,108:107,108', '107,108:107,109', '106,108:106,109', '106,109:107,109', '107,108:108,108', '108,108:108,109', '107,108:107,109', '107,109:108,109', '108,108:109,108', '109,108:109,109', '108,108:108,109', '108,109:109,109', '108,106:109,106', '109,106:109,107', '108,106:108,107', '108,107:109,107', '108,105:109,105', '109,105:109,106', '108,105:108,106', '108,106:109,106', '108,103:109,103', '109,103:109,104', '108,103:108,104', '108,104:109,104', '108,102:109,102', '109,102:109,103', '108,102:108,103', '108,103:109,103', '110,105:111,105', '111,105:111,106', '110,105:110,106', '110,106:111,106', '110,109:111,109', '111,109:111,110', '110,109:110,110', '110,110:111,110', '109,109:110,109', '110,109:110,110', '109,109:109,110', '109,110:110,110', '111,109:112,109', '112,109:112,110', '111,109:111,110', '111,110:112,110', '102,107:103,107', '103,107:103,108', '102,107:102,108', '102,108:103,108', '101,106:102,106', '102,106:102,107', '101,106:101,107', '101,107:102,107', '100,106:101,106', '101,106:101,107', '100,106:100,107', '100,107:101,107', '99,106:100,106', '100,106:100,107', '99,106:99,107', '99,107:100,107', '98,105:99,105', '99,105:99,106', '98,105:98,106', '98,106:99,106', '97,104:98,104', '98,104:98,105', '97,104:97,105', '97,105:98,105', '97,103:98,103', '98,103:98,104', '97,103:97,104', '97,104:98,104', '97,102:98,102', '98,102:98,103', '97,102:97,103', '97,103:98,103', '97,101:98,101', '98,101:98,102', '97,101:97,102', '97,102:98,102', '97,100:98,100', '98,100:98,101', '97,100:97,101', '97,101:98,101', '97,97:98,97', '98,97:98,98', '97,97:97,98', '97,98:98,98', '98,96:99,96', '99,96:99,97', '98,96:98,97', '98,97:99,97', '99,96:100,96', '100,96:100,97', '99,96:99,97', '99,97:100,97', '100,96:101,96', '101,96:101,97', '100,96:100,97', '100,97:101,97', '104,96:105,96', '105,96:105,97', '104,96:104,97', '104,97:105,97', '105,96:106,96', '106,96:106,97', '105,96:105,97', '105,97:106,97', '108,96:109,96', '109,96:109,97', '108,96:108,97', '108,97:109,97', '108,95:109,95', '109,95:109,96', '108,95:108,96', '108,96:109,96', '108,94:109,94', '109,94:109,95', '108,94:108,95', '108,95:109,95', '107,93:108,93', '108,93:108,94', '107,93:107,94', '107,94:108,94', '106,93:107,93', '107,93:107,94', '106,93:106,94', '106,94:107,94', '105,93:106,93', '106,93:106,94', '105,93:105,94', '105,94:106,94', '104,93:105,93', '105,93:105,94', '104,93:104,94', '104,94:105,94', '103,93:104,93', '104,93:104,94', '103,93:103,94', '103,94:104,94', '102,93:103,93', '103,93:103,94', '102,93:102,94', '102,94:103,94', '101,93:102,93', '102,93:102,94', '101,93:101,94', '101,94:102,94', '100,94:101,94', '101,94:101,95', '100,94:100,95', '100,95:101,95', '99,94:100,94', '100,94:100,95', '99,94:99,95', '99,95:100,95', '97,95:98,95', '98,95:98,96', '97,95:97,96', '97,96:98,96', '98,94:99,94', '99,94:99,95', '98,94:98,95', '98,95:99,95', '109,97:110,97', '110,97:110,98', '109,97:109,98', '109,98:110,98', '109,98:110,98', '110,98:110,99', '109,98:109,99', '109,99:110,99', '109,99:110,99', '110,99:110,100', '109,99:109,100', '109,100:110,100', '109,102:110,102', '110,102:110,103', '109,102:109,103', '109,103:110,103', '110,102:111,102', '111,102:111,103', '110,102:110,103', '110,103:111,103', '111,102:112,102', '112,102:112,103', '111,102:111,103', '111,103:112,103', '92,102:93,102', '93,102:93,103', '92,102:92,103', '92,103:93,103', '92,100:93,100', '93,100:93,101', '92,100:92,101', '92,101:93,101', '92,101:93,101', '93,101:93,102', '92,101:92,102', '92,102:93,102', '92,99:93,99', '93,99:93,100', '92,99:92,100', '92,100:93,100', '92,97:93,97', '93,97:93,98', '92,97:92,98', '92,98:93,98', '92,98:93,98', '93,98:93,99', '92,98:92,99', '92,99:93,99', '92,96:93,96', '93,96:93,97', '92,96:92,97', '92,97:93,97', '92,95:93,95', '93,95:93,96', '92,95:92,96', '92,96:93,96', '92,94:93,94', '93,94:93,95', '92,94:92,95', '92,95:93,95', '101,103:102,103', '102,103:102,104', '101,103:101,104', '101,104:102,104', '104,104:105,104', '105,104:105,105', '104,104:104,105', '104,105:105,105', '105,97:106,97', '106,97:106,98', '105,97:105,98', '105,98:106,98', '100,97:101,97', '101,97:101,98', '100,97:100,98', '100,98:101,98', '100,98:101,98', '101,98:101,99', '100,98:100,99', '100,99:101,99', '105,98:106,98', '106,98:106,99', '105,98:105,99', '105,99:106,99', '104,98:105,98', '105,98:105,99', '104,98:104,99', '104,99:105,99']
walls =['108,99:109,99', '109,99:109,100', '108,99:108,100', '108,100:109,100', '107,100:108,100', '108,100:108,101', '107,100:107,101', '107,101:108,101', '106,101:107,101', '107,101:107,102', '106,101:106,102', '106,102:107,102', '107,102:108,102', '108,102:108,103', '107,102:107,103', '107,103:108,103', '107,104:108,104', '108,104:108,105', '107,104:107,105', '107,105:108,105', '108,103:108,104', '107,103:107,104', '106,105:107,105', '107,105:107,106', '106,105:106,106', '106,106:107,106', '105,105:106,105', '105,105:105,106', '105,106:106,106', '103,105:104,105', '104,105:104,106', '103,105:103,106', '103,106:104,106', '104,105:105,105', '104,106:105,106', '101,105:102,105', '102,105:102,106', '101,105:101,106', '101,106:102,106', '102,105:103,105', '102,106:103,106', '100,105:101,105', '100,105:100,106', '100,106:101,106', '99,105:100,105', '99,105:99,106', '99,106:100,106', '98,105:99,105', '98,105:98,106', '98,106:99,106', '96,104:97,104', '97,104:97,105', '96,104:96,105', '96,105:97,105', '96,103:97,103', '97,103:97,104', '96,103:96,104', '97,105:98,105', '97,105:97,106', '97,106:98,106', '96,102:97,102', '97,102:97,103', '96,102:96,103', '96,100:97,100', '97,100:97,101', '96,100:96,101', '96,101:97,101', '97,101:97,102', '96,101:96,102', '96,99:97,99', '97,99:97,100', '96,99:96,100', '97,99:98,99', '98,99:98,100', '97,100:98,100', '98,99:99,99', '99,99:99,100', '98,100:99,100', '98,101:99,101', '99,101:99,102', '98,101:98,102', '98,102:99,102', '99,100:99,101', '98,100:98,101', '99,102:99,103', '98,102:98,103', '98,103:99,103', '99,103:99,104', '98,103:98,104', '98,104:99,104', '98,98:99,98', '99,98:99,99', '98,98:98,99', '98,97:99,97', '99,97:99,98', '98,97:98,98', '98,95:99,95', '99,95:99,96', '98,95:98,96', '98,96:99,96', '99,96:99,97', '98,96:98,97', '98,94:99,94', '99,94:99,95', '98,94:98,95', '98,93:99,93', '99,93:99,94', '98,93:98,94', '99,93:100,93', '100,93:100,94', '99,94:100,94', '100,94:101,94', '101,94:101,95', '100,94:100,95', '100,95:101,95', '101,95:101,96', '100,95:100,96', '100,96:101,96', '101,96:101,97', '100,96:100,97', '100,97:101,97', '101,97:102,97', '102,97:102,98', '101,97:101,98', '101,98:102,98', '102,96:103,96', '103,96:103,97', '102,96:102,97', '102,97:103,97', '103,94:104,94', '104,94:104,95', '103,94:103,95', '103,95:104,95', '106,95:107,95', '107,95:107,96', '106,95:106,96', '106,96:107,96', '107,95:108,95', '108,95:108,96', '107,96:108,96', '108,96:109,96', '109,96:109,97', '108,96:108,97', '108,97:109,97', '107,97:108,97', '108,97:108,98', '107,97:107,98', '107,98:108,98', '108,98:108,99', '107,98:107,99', '107,99:108,99', '107,99:107,100', '107,94:108,94', '108,94:108,95', '107,94:107,95', '107,93:108,93', '108,93:108,94', '107,93:107,94', '107,92:108,92', '108,92:108,93', '107,92:107,93', '106,92:107,92', '106,92:106,93', '106,93:107,93', '104,92:105,92', '105,92:105,93', '104,92:104,93', '104,93:105,93', '105,92:106,92', '105,93:106,93', '102,92:103,92', '103,92:103,93', '102,92:102,93', '102,93:103,93', '103,92:104,92', '103,93:104,93', '101,92:102,92', '101,92:101,93', '101,93:102,93', '99,92:100,92', '100,92:100,93', '99,92:99,93', '99,91:100,91', '100,91:100,92', '99,91:99,92', '101,91:102,91', '102,91:102,92', '101,91:101,92']

def CastARay(x, y, angle):
    xOffset = 0
    yOffset = 0
    Direction = 0

    if angle < -180:
        Direction = 1
        angle = angle * -1
        angle = 360 - angle
    elif angle > 180:
        Direction = -1
        angle = 360 - angle
    elif angle < 0:
        Direction = -1
        angle = angle * -1
    elif angle > 0:
        Direction = 1

    for i in range(0, renderDistance, 1):
        KnownY = math.ceil(y + yOffset)
        KnownX = math.ceil(x + xOffset)
        FloorKnownY = math.floor(y + yOffset)
        FloorKnownX = math.floor(x + xOffset)
        if angle == 90:
            if Direction == 1:
                if f"{KnownX},{FloorKnownY}:{KnownX},{KnownY}" in walls:

                    #ambient occlusion
                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{KnownX -1 },{KnownY}:{KnownX},{KnownY}" in walls:
                        ambMultiplier1 = abs(KnownY - y)
                    if f"{KnownX -1},{FloorKnownY}:{KnownX},{FloorKnownY}" in walls:
                        ambMultiplier2 = abs(FloorKnownY - y)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [KnownX - x, realAmbMult]
                else:
                    xOffset += 1
            elif Direction == -1:
                if f"{FloorKnownX},{FloorKnownY}:{FloorKnownX},{KnownY}" in walls:

                    #ambient occlusion
                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{FloorKnownX},{KnownY}:{KnownX},{KnownY}" in walls:
                        ambMultiplier1 = abs(KnownY - y)
                    if f"{FloorKnownX},{FloorKnownY}:{KnownX},{FloorKnownY}" in walls:
                        ambMultiplier2 = abs(FloorKnownY - y)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [x - FloorKnownX, realAmbMult]
                else:
                    xOffset -= 1
        elif angle == 180:
            if f"{FloorKnownX},{FloorKnownY}:{KnownX},{FloorKnownY}" in walls:

                #ambient occlusion
                ambMultiplier1 = 1
                ambMultiplier2 = 1
                if f"{KnownX},{FloorKnownY}:{KnownX},{FloorKnownY + 1}" in walls:
                    ambMultiplier1 = abs(KnownX - x)
                if f"{FloorKnownX},{FloorKnownY}:{FloorKnownX},{FloorKnownY + 1}" in walls:
                    ambMultiplier2 = abs(FloorKnownX - x)
                if ambMultiplier1 < ambMultiplier2:
                    realAmbMult = ambMultiplier1
                else: 
                    realAmbMult = ambMultiplier2

                return [y - FloorKnownY, realAmbMult]
            else:
                yOffset -= 1
        elif Direction == 1:
            MaxAngle_UpRight = math.atan((KnownX - x ) / (KnownY - y)) * 180.0 / math.pi
            MaxAngle_RightDown = 180 - math.atan((KnownX - x) / (y - FloorKnownY)) * 180.0 / math.pi
            if angle == MaxAngle_UpRight:
                        
                left = CastARay(x, y, angle - 1)
                right = CastARay(x, y, angle + 1)

                if left[0] == -1:
                    return right
                elif right[0] == -1:
                    return left

                return [(left[0] + right[0]) / 2, (left[1] + right[1]) / 2]
                
            if angle < MaxAngle_RightDown and angle > MaxAngle_UpRight:
                UsableAngle = angle
                if UsableAngle < 90: UsableAngle = 90 - UsableAngle
                elif UsableAngle > 90: UsableAngle = UsableAngle - 90

                if angle > 90:
                    RayCastHitY = y - math.tan(UsableAngle * math.pi / 180) * (KnownX - x)
                else:
                    RayCastHitY = math.tan(UsableAngle * math.pi / 180) * (KnownX - x) + y

                if f"{KnownX},{math.floor(RayCastHitY)}:{KnownX},{math.ceil(RayCastHitY)}" in walls:
                    #ambient occlusion
                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{KnownX -1 },{math.ceil(RayCastHitY)}:{KnownX},{math.ceil(RayCastHitY)}" in walls:
                        ambMultiplier1 = math.ceil(RayCastHitY) - RayCastHitY
                    if f"{KnownX -1},{math.floor(RayCastHitY)}:{KnownX},{math.floor(RayCastHitY)}" in walls:
                        ambMultiplier2 = abs(math.floor(RayCastHitY) - RayCastHitY)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [math.sqrt((KnownX - x) ** 2 + (RayCastHitY - y) ** 2), realAmbMult]
                else:
                    xOffset += 1
            elif angle > MaxAngle_RightDown:
                RayCastHitX = math.tan((180 - angle) * math.pi / 180) * (y - FloorKnownY) + x
                if f"{math.floor(RayCastHitX)},{FloorKnownY}:{math.ceil(RayCastHitX)},{FloorKnownY}" in walls:

                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{math.floor(RayCastHitX)},{FloorKnownY}:{math.floor(RayCastHitX)},{FloorKnownY + 1}" in walls:
                        ambMultiplier1 = abs(math.floor(RayCastHitX) - RayCastHitX)
                    if f"{math.ceil(RayCastHitX)},{FloorKnownY}:{math.ceil(RayCastHitX)},{FloorKnownY + 1}" in walls:
                        ambMultiplier2 = abs(math.ceil(RayCastHitX) - RayCastHitX)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [math.sqrt((y - FloorKnownY) ** 2 + (RayCastHitX - x) ** 2), realAmbMult]
                else:
                    yOffset -= 1
            else:
                RayCastHitX = math.tan(angle * math.pi / 180) * (KnownY - y) + x
                if f"{math.floor(RayCastHitX)},{KnownY}:{math.ceil(RayCastHitX)},{KnownY}" in walls:
                    #ambient occlusion
                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{math.ceil(RayCastHitX)},{KnownY - 1}:{math.ceil(RayCastHitX)},{KnownY}" in walls:
                        ambMultiplier1 = math.ceil(RayCastHitX) - RayCastHitX
                    if f"{math.floor(RayCastHitX)},{KnownY - 1}:{math.floor(RayCastHitX)},{KnownY}" in walls:
                        ambMultiplier2 = abs(math.floor(RayCastHitX) - RayCastHitX)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [math.sqrt((KnownY - y) ** 2 + (RayCastHitX - x) ** 2), realAmbMult]
                else:
                    yOffset += 1

        elif Direction == -1:
            MaxAngle_UpLeft = math.atan((x - FloorKnownX) / (KnownY - y)) * 180.0 / math.pi
            MaxAngle_LeftDown = 180 - math.atan((x - FloorKnownX) / (y - FloorKnownY)) * 180.0 / math.pi
            if angle == MaxAngle_UpLeft:
                left = CastARay(x, y, -1* angle - 1)
                right = CastARay(x, y, -1* angle + 1)



                if left[0] == -1:
                    return right
                elif right[0] == -1:
                    return left

                return [(left[0] + right[0]) / 2, (left[1] + right[1]) / 2]
            if angle < MaxAngle_LeftDown and angle > MaxAngle_UpLeft:
                UsableAngle = angle
                if UsableAngle < 90: UsableAngle = 90 - UsableAngle
                elif UsableAngle > 90: UsableAngle = UsableAngle - 90

                if angle > 90:
                    RayCastHitY = y - math.tan(UsableAngle * math.pi / 180) * (x - FloorKnownX)
                else:
                    RayCastHitY = math.tan(UsableAngle * math.pi / 180) * (x - FloorKnownX) + y

                if f"{FloorKnownX},{math.floor(RayCastHitY)}:{FloorKnownX},{math.ceil(RayCastHitY)}" in walls:

                    #ambient occlusion
                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{KnownX - 1},{math.ceil(RayCastHitY)}:{KnownX},{math.ceil(RayCastHitY)}" in walls:
                        ambMultiplier1 = math.ceil(RayCastHitY) - RayCastHitY
                    if f"{KnownX -1},{math.floor(RayCastHitY)}:{KnownX},{math.floor(RayCastHitY)}" in walls:
                        ambMultiplier2 = abs(math.floor(RayCastHitY) - RayCastHitY)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [math.sqrt((x - FloorKnownX) ** 2 + (RayCastHitY - y) ** 2), realAmbMult]
                else:
                    xOffset -= 1
            elif angle > MaxAngle_LeftDown:
                RayCastHitX = x - math.tan((180 - angle) * math.pi / 180) * (y - FloorKnownY)
                if f"{math.floor(RayCastHitX)},{FloorKnownY}:{math.ceil(RayCastHitX)},{FloorKnownY}" in walls:

                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{math.floor(RayCastHitX)},{FloorKnownY}:{math.floor(RayCastHitX)},{FloorKnownY + 1}" in walls:
                        ambMultiplier1 = abs(math.floor(RayCastHitX) - RayCastHitX)
                    if f"{math.ceil(RayCastHitX)},{FloorKnownY}:{math.ceil(RayCastHitX)},{FloorKnownY + 1}" in walls:
                        ambMultiplier2 = abs(math.ceil(RayCastHitX) - RayCastHitX)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [math.sqrt((y - FloorKnownY) ** 2 + (RayCastHitX - x) ** 2), realAmbMult]
                else:
                    yOffset -= 1
            else:
                RayCastHitX = x - math.tan(angle * math.pi / 180) * (KnownY - y)
                if f"{math.floor(RayCastHitX)},{KnownY}:{math.ceil(RayCastHitX)},{KnownY}" in walls:

                    ambMultiplier1 = 1
                    ambMultiplier2 = 1
                    if f"{math.floor(RayCastHitX)},{KnownY - 1}:{math.floor(RayCastHitX)},{KnownY}" in walls:
                        ambMultiplier1 = abs(math.floor(RayCastHitX) - RayCastHitX)
                    if f"{math.ceil(RayCastHitX)},{KnownY - 1}:{math.ceil(RayCastHitX)},{KnownY}" in walls:
                        ambMultiplier2 = abs(math.ceil(RayCastHitX) - RayCastHitX)
                    if ambMultiplier1 < ambMultiplier2:
                        realAmbMult = ambMultiplier1
                    else: 
                        realAmbMult = ambMultiplier2

                    return [math.sqrt((KnownY - y) ** 2 + (RayCastHitX - x) ** 2), realAmbMult]
                else:
                    yOffset += 1
        elif Direction == 0:
            if f"{FloorKnownX},{KnownY}:{KnownX},{KnownY}" in walls:

                ambMultiplier1 = 1
                ambMultiplier2 = 1
                if f"{FloorKnownX},{KnownY - 1}:{FloorKnownX},{KnownY}" in walls:
                    ambMultiplier1 = abs(FloorKnownX - x)
                if f"{KnownX},{KnownY - 1}:{KnownX},{KnownY}" in walls:
                    ambMultiplier2 = abs(KnownX - x)
                if ambMultiplier1 < ambMultiplier2:
                    realAmbMult = ambMultiplier1
                else: 
                    realAmbMult = ambMultiplier2

                return [KnownY - y, realAmbMult]
            else:
                yOffset += 1
    return [-1]



pygame.init()
font = pygame.font.SysFont("Arial", 18)
running = True
PlayerX, PlayerY = 100.5, 100.5
angleOffset = 0
colorMult = 1



def CalcDistMult(distance):
    #mult = 2.2/(0.05*(distance+4.1))-0.8
    #mult = 5/(0.2*(distance+3))+1.5
    mult = 0.5 / (distance * math.tan(math.radians(40)))
    return mult
def CalcColorMult(distance):
    mult = -10 * distance + 255
    if mult > 255: mult = 255
    if mult < 0.5: mult = 0.5
    return mult

while running:
    surface.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()
    movespeed = speed
    if keys[pygame.K_LSHIFT]:
        movespeed = speedRun
    movementAngle = angleOffset * -1
    nPlayerX = 0
    nPlayerY = 0
    if keys[pygame.K_w]:
        nPlayerX = movespeed * math.cos((movementAngle + 90) * math.pi / 180)
        nPlayerY =  movespeed * math.sin((movementAngle + 90) * math.pi / 180)
    if keys[pygame.K_s]:
        nPlayerX = movespeed * math.cos((movementAngle - 90) * math.pi / 180)
        nPlayerY = movespeed * math.sin((movementAngle - 90) * math.pi / 180)
    if keys[pygame.K_a]:
        nPlayerX = movespeed * math.cos((movementAngle - 180) * math.pi / 180)
        nPlayerY = movespeed * math.sin((movementAngle - 180) * math.pi / 180)
    if keys[pygame.K_d]:
        nPlayerX = movespeed * math.cos((movementAngle) * math.pi / 180)
        nPlayerY = movespeed * math.sin((movementAngle) * math.pi / 180)

    if nPlayerY > 0:
        if abs((PlayerY + nPlayerY) - math.ceil(PlayerY)) <= wallRadius:
            if f"{math.floor(PlayerX)},{math.ceil(PlayerY)}:{math.ceil(PlayerX)},{math.ceil(PlayerY)}" not in walls:
                PlayerY += nPlayerY
        else:
            PlayerY += nPlayerY
    elif nPlayerY < 0:
        if abs((PlayerY + nPlayerY) - math.floor(PlayerY)) <= wallRadius:
            if f"{math.floor(PlayerX)},{math.floor(PlayerY)}:{math.ceil(PlayerX)},{math.floor(PlayerY)}" not in walls:
                PlayerY += nPlayerY
        else:
            PlayerY += nPlayerY
    if nPlayerX > 0:
        if abs((PlayerX + nPlayerX) - math.ceil(PlayerX)) <= wallRadius:
            if f"{math.ceil(PlayerX)},{math.floor(PlayerY)}:{math.ceil(PlayerX)},{math.ceil(PlayerY)}" not in walls:
                PlayerX += nPlayerX
        else:
            PlayerX += nPlayerX
    elif nPlayerX < 0:
        if abs((PlayerX + nPlayerX) - math.floor(PlayerX)) <= wallRadius:
            if f"{math.floor(PlayerX)},{math.floor(PlayerY)}:{math.floor(PlayerX)},{math.ceil(PlayerY)}" not in walls:
                PlayerX += nPlayerX
        else:
            PlayerX += nPlayerX
    



    angleOffset += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 2
    if angleOffset >= 270: angleOffset = -90
    elif angleOffset <= -270: angleOffset = 90
                
    #debug
    if keys[pygame.K_t]:
        PlayerX = PlayerX + 0.5 * math.cos((movementAngle + 90) * math.pi / 180)
        PlayerY = PlayerY + 0.5 * math.sin((movementAngle + 90) * math.pi / 180)

    #lattia ja katto
    pygame.draw.rect(surface, (120, 120, 120), pygame.Rect(0, 0, width, height / 2))
    pygame.draw.rect(surface, (60, 60, 60), pygame.Rect(0, height / 2, width, height / 2))

    #print(PlayerX, PlayerY)

    #renderöinti
    currentX = 0
    for k in range((-40 + angleOffset) * scale, (40 + angleOffset) * scale, 1):
        i = k / scale
        rayCastReturn = CastARay(PlayerX, PlayerY, i)
        if type(rayCastReturn) != type([]):
            rayCastReturn = [rayCastReturn]
        distance = rayCastReturn[0]
        if distance != -1:
            DistanceMult = CalcDistMult(distance)
            if DistanceMult < 0: DistanceMult = 0
            rect = pygame.Rect(currentX, 50, width/(80*scale), height * DistanceMult)
            rect.centery = height / 2
            colorMultCalculated = CalcColorMult(distance)
            if (len(rayCastReturn) >= 2) and (rayCastReturn[1] == "b"):
                color = (0, 0, 255)
            elif (len(rayCastReturn) >= 2) and (rayCastReturn[1] == "g"):
                color = (0, 255, 0)
            elif (len(rayCastReturn) >= 2) and (rayCastReturn[1] == "r"):
                color = (255, 0, 0)
            else:
                ambientOcclusionMultiplier = 1
                if (len(rayCastReturn) >= 2):
                    ambientOcclusionMultiplier = -0.6*(1 - rayCastReturn[1])+1
                    if ambientOcclusionMultiplier <= 0.4: ambientOcclusionMultiplier = 0.4
                color = (int(colorMultCalculated * ambientOcclusionMultiplier), int(colorMultCalculated * ambientOcclusionMultiplier), int(colorMultCalculated * ambientOcclusionMultiplier))
            pygame.draw.rect(surface, color, rect)
        currentX += width/(80*scale)

    surface.blit(update_fps(), (10,0))
    surface.blit(writeTxt(f"angle: {angleOffset}"), (10,40))
    clock.tick(60)

    pygame.display.flip()
import pygame

width = 600
height = 600
surface = pygame.display.set_mode((width,height))
running = True
allBlocks = []
allGUIBlocks = []

def round_to_multiple(number, multiple):
    return multiple * round(number / multiple)

def ParseList():
    newList = []
    for i in range(0, len(allBlocks)):
        bX = allBlocks[i][0]
        bY = allBlocks[i][1]
        if f"{bX},{bY}:{bX + 1},{bY}" not in allBlocks:
            newList.append(f"{bX},{bY}:{bX + 1},{bY}")
        if f"{bX + 1},{bY}:{bX + 1},{bY + 1}" not in allBlocks:
            newList.append(f"{bX + 1},{bY}:{bX + 1},{bY + 1}")
        if f"{bX},{bY}:{bX},{bY + 1}" not in allBlocks:
            newList.append(f"{bX},{bY}:{bX},{bY + 1}")
        if f"{bX},{bY + 1}:{bX + 1},{bY + 1}" not in allBlocks:
            newList.append(f"{bX},{bY + 1}:{bX + 1},{bY + 1}")
    return newList

while running:
    surface.fill((0, 0, 0))
    for w in range(2, width, 30):
        for h in range(2, height, 30):
            pygame.draw.rect(surface, (70, 70, 70), pygame.Rect(w + 2, h + 2, 26, 26))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            print(ParseList())
            running=False
        if event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            allGUIBlocks.append([round_to_multiple(x, 30), round_to_multiple(y, 30)])
            blockX = int(round(x/30)*30 / 30 - 8 + 100)
            blockY = int((round(y/30)*30 / 30 - 10) * -1 + 100)
            allBlocks.append([blockX, blockY])
            print(blockX, blockY)
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                allGUIBlocks.pop()
                allBlocks.pop()
    
    for i in range(0, len(allGUIBlocks), 1):
        pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(allGUIBlocks[i][0], allGUIBlocks[i][1], 30, 30))
            
    pygame.display.flip()
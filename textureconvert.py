from PIL import Image

polku = "wall.png"
koko = 108

def texture():
    texture = []

    image = Image.open(polku)
    if (koko, koko) == image.size:
        pix = image.load()
        for x in range(0, koko):
            texture.append([])
            for y in range(0, koko):
                c = pix[x, y]
                texture[x].append((c[0], c[1], c[2]))
        
    else:
        print(f'Vääränkokoinen kuva (ei {koko}x{koko})')

    return texture
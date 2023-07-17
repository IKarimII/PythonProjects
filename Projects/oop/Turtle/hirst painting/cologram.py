import colorgram

colors = colorgram.extract('hitrstr.jpg', 30)


colour = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colour.append((r, g, b))
print(colour)
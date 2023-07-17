import pandas

data = pandas.read_csv("squirrel_data.csv")

colors = data['Primary Fur Color'].to_list()
gray = len(data[data['Primary Fur Color'] == 'Gray'])
black = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])

print(gray)
print(cinnamon)
print(black)

squirrel_colors = {
    'Fur Color':['Gray', 'Cinnamon', 'Black'],
    'count': [gray, cinnamon, black]
}

squirrel_data = pandas.DataFrame(squirrel_colors)
squirrel_data.to_csv("squirrel_colors.csv")

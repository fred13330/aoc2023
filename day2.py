
with open("data/day2_data.txt", "r", encoding="UTF-8") as file_in:
    data = file_in.read().splitlines()

possible_games = [] 
necessary_cube = []

for line in data:
    color_dict = {
        "red": [[], 12],
        "green": [[], 13],
        "blue": [[], 14,]
                 }

    number_of_game = line[:line.find(":")].split(" ")[1]
    game_choice = line[line.find(":")+1:].replace(";", ",").split(",")

    for game in game_choice:
        game = game.lstrip().split(" ")
        color_dict[game[1]][0].append(int(game[0]))
   
    validation = True  
    minimum_number_of_cubes = 1  

    for color in color_dict.keys():
        minimum_number_of_cubes *= max(color_dict[color][0])
        if max(color_dict[color][0]) > color_dict[color][1]:
            validation = False

    necessary_cube.append(minimum_number_of_cubes)

    if validation:
        possible_games.append(int(number_of_game))

print("Part 1 - La somme des jeux possible est de", sum(possible_games))
print("Part 1 - La nombre minimum de cube est de", sum(necessary_cube))
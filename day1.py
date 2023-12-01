import string

def somme(data, part):
    digits_list = []
    if part:
        data = conversion_alpha_numeric(data)
    for line in data:
        line_list = []
        for el in line:
            if el in string.digits:
                line_list.append(el)
        digits_list.append(int(line_list[0] + line_list[-1]))
    return digits_list

def conversion_alpha_numeric(liste):
    line_list = []
    for line in liste:
        for alpha, numeric in digits_dict.items():
            line = line.replace(alpha, numeric)
        line_list.append(line)
    return line_list

digits_dict = {
                "twone": "21",
                "sevenine": "79",
                "oneight": "18",
                "threeight": "38",
                "nineight": "98",
                "eighthree": "83",
                "eightwo": "82",
                "one": "1",
                "two": "2",
                "three": "3",
                "four": "4",
                "five": "5",
                "six": "6",
                "seven": "7",
                "eight": "8",
                "nine": "9",
}

with open("data/day1_data.txt", "r", encoding="UTF-8") as file_in:
    data = file_in.read().splitlines()

print("PART1 - Somme des valeurs de calibration :", sum(somme(data, part=False))) 
print("PART2 - Somme des valeurs de calibration :", sum(somme(data, part=True)))      
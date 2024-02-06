MOVES_FILE = "moves.txt"

def read_file(infile):
        try:
            with open(infile, "r") as file1:
                reader = file1.readlines()
                temp_file = []

                for x in reader:
                    temp_file.append(x)


                return temp_file
        except OSError as x:
            print(f"Error Happened, {x}")
            exit()
    
def file_splitter(inlist):
    temp_file = []

    for x in inlist:
        temp_file.append(x.split())

    return temp_file

def set_playground():
    return [["-", "-", "-", "-", "-", "-", "-", ], 
            ["-", "-", "-", "-", "-", "-", "-", ], 
            ["-", "-", "-", "-", "-", "-", "-", ], 
            ["-", "-", "-", "-", "-", "-", "-", ], 
            ["-", "-", "-", "-", "-", "-", "-", ], 
            ["-", "-", "-", "-", "-", "-", "-", ], 
            ["-", "-", "-", "-", "-", "-", "-", ], ]

def playground_print(inground):
    temp_list = inground
    temp_list.reverse()

    for row in temp_list:
        print("")
        for x in row:
            print(x, end="")

    temp_list.reverse()
    

def main():
    moves_list = file_splitter(read_file(MOVES_FILE))
    playground = set_playground()
    sign = ""
    won = 0
    moves_total = 0

    for player, move in moves_list:
        played = 0

        if player == "G1":
            sign = "O"
        else:
            sign = "X"

        for index, row in enumerate(playground):
            if row[int(move) - 1] == "-" and played != 1:
                playground[index][int(move) - 1] = sign
                played = 1
                moves_total = moves_total + 1
                print(f"\n\n{player} played.")

                try:
                    if playground[(index - 1)][int(move) - 1] == sign and playground[(index - 2)][int(move) - 1] == sign and playground[(index - 3)][int(move) - 1] == sign:
                        won = 1
                except:
                    pass
                
                try:
                    if playground[(index - 1)][int(move) - 2] == sign and playground[(index - 2)][int(move) - 3] == sign and playground[(index - 3)][int(move) - 4] == sign:
                        won = 1
                except:
                    pass
                try:
                    if playground[(index - 1)][int(move)] == sign and playground[(index - 2)][int(move) + 1] == sign and playground[(index - 3)][int(move) + 2] == sign:
                        won = 1
                except:
                    pass
                try:
                    if playground[(index)][int(move) - 2] == sign and playground[(index)][int(move) - 3] == sign and playground[(index)][int(move) - 4] == sign:
                        won = 1
                except:
                    pass
                try:
                    if playground[(index)][int(move)] == sign and playground[(index)][int(move) + 1] == sign and playground[(index)][int(move) + 2] == sign:
                        won = 1
                except:
                    pass

                if won:
                    print(f"{player} won in {moves_total}.")
                    playground_print(playground)
                    exit()

                
                playground_print(playground)


if __name__ == "__main__":
    main()
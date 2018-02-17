while True:
    def move_right (x_coord, y_coord):
        return x_coord + 1, y_coord
    def move_up (x_coord, y_coord):
        return x_coord, y_coord + 1
    def move_left(x_coord, y_coord):
        return x_coord - 1, y_coord
    def move_down (x_coord, y_coord):
        return x_coord, y_coord - 1

    def distance (source_cell):
        current_cell = 1
        current_coord = [0,0]
        move_index = 0
        jumps = 1

        while current_cell != source_cell:
            for i in range(2):
                for j in range(jumps):
                    current_coord[0], current_coord[1] = moves[move_index](current_coord[0], current_coord[1])
                    current_cell += 1

                    if current_cell == source_cell:
                        return abs(current_coord[0]) + abs(current_coord[1])
                
                move_index = (move_index + 1) % 4

            jumps += 1
            

        return abs(current_coord[0]) + abs(current_coord[1])
            

    moves = [move_right,move_up,move_left,move_down]

    source = int(input())

    print(distance (source))
    

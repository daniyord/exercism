def annotate(garden):
    result : list= []

    check_len = None

    for (y,row) in enumerate(garden):
        if check_len is not None and check_len != len(row):
            raise ValueError("The board is invalid with current input.")
        check_len = len(row)

        new_row = ""

        for (x, cell) in enumerate(row):
            if cell == "*":
                new_row += cell
            elif cell == " ":
                count = 0

                tests = [(-1, -1), (0, -1), (1,-1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

                for test in tests:
                    check_x = x + test[0]
                    check_y = y + test[1]

                    if   0 <= check_x < len(row) and 0 <= check_y < len(garden) and garden[check_y][check_x] == "*":
                        count += 1                

                new_row += str(count) if count > 0 else " "    
            else:
                raise ValueError("The board is invalid with current input.")        

        result.append(new_row)  

    return result
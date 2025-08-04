def get_sort_value(x):
    return (-x[1]["P"], x[0])


def tally(rows):
    results = {}

    for row in rows:
        parts = row.split(";")

        match parts[2]:
            case "win":
                calc_resut(results, parts[0], "W")
                calc_resut(results, parts[1], "L")
            case "draw":
                calc_resut(results, parts[0], "D")
                calc_resut(results, parts[1], "D")
            case "loss":
                calc_resut(results, parts[0], "L")
                calc_resut(results, parts[1], "W")

    final_result = ["Team                           | MP |  W |  D |  L |  P"]

    for team, result in sorted(results.items(), key=get_sort_value):
        team_part = team.ljust(31, " ")
        mp_part = str(result["MP"]).rjust(3, " ")
        w_part = str(result["W"]).rjust(3, " ")
        d_part = str(result["D"]).rjust(3, " ")
        l_part = str(result["L"]).rjust(3, " ")
        p_part = str(result["P"]).rjust(3, " ")
        final_result.append(f"{team_part}|{mp_part} |{w_part} |{d_part} |{l_part} |{p_part}")

    return final_result


def calc_resut(results, team, result):
    if not team in results:
        results[team] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}

    results[team]["MP"] += 1
    match result:
        case "W":
            results[team]["W"] += 1
            results[team]["P"] += 3
            pass
        case "D":
            results[team]["D"] += 1
            results[team]["P"] += 1
            pass
        case "L":
            results[team]["L"] += 1
            pass

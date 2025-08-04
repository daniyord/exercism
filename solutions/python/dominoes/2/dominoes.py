def can_chain(dominoes):
    if dominoes == []:
        return []

    search_helper = {}
    results = []

    for index, domino in enumerate(dominoes):
        results.append(([[(domino[0], domino[1])], [index]]))
        results.append(([[(domino[1], domino[0])], [index]]))

        if domino[0] not in search_helper:
            search_helper[domino[0]] = []
        if domino[1] not in search_helper:
            search_helper[domino[1]] = []

        search_helper[domino[0]].append(index)
        search_helper[domino[1]].append(index)

    while len(results) > 0 and len(results[0][1]) != len(dominoes):
        new_results = []
        for result in results:
            last_domino = result[0][-1]
            for next_domino_index in search_helper[last_domino[1]]:
                if next_domino_index not in result[1]:
                    next_domino = dominoes[next_domino_index]

                    if last_domino[1] == next_domino[0]:
                        new_result_left = result[0][:]
                        new_result_left.append((next_domino[0], next_domino[1]))

                        new_result_right = result[1][:]
                        new_result_right.append(next_domino_index)

                        new_results.append((new_result_left, new_result_right))
                    elif last_domino[1] == next_domino[1]:
                        new_result_left = result[0][:]
                        new_result_left.append((next_domino[1], next_domino[0]))

                        new_result_right = result[1][:]
                        new_result_right.append(next_domino_index)

                        new_results.append((new_result_left, new_result_right))

        results = new_results

    for result in results:
        if result[0][0][0] == result[0][-1][1]:
            return result[0]

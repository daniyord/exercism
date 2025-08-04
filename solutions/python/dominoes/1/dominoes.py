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
            for next_domino_index in search_helper[result[0][-1][1]]:
                if next_domino_index not in result[1]:
                    next_domino = dominoes[next_domino_index]
                    last_domino = result[0][-1]

                    if last_domino[1] == next_domino[0]:
                        result[0].append((next_domino[0], next_domino[1]))
                        result[1].append(next_domino_index)
                        new_results.append(result)
                    elif last_domino[1] == next_domino[1]:
                        result[0].append((next_domino[1], next_domino[0]))
                        result[1].append(next_domino_index)
                        new_results.append(result)

        print(new_results)
        print()
        results = new_results

    print(f"results: {results}")
    # print(f"search_helper: {search_helper}")

    for result in results:
        if result[0][0][0] == result[0][-1][1]:
            return result[0]


print(can_chain([(1, 2), (2, 3), (3, 1), (1, 1), (2, 2), (3, 3)]))

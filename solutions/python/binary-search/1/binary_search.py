def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")

    middle = len(search_list) // 2

    print(search_list, value, middle)

    if value == search_list[middle]:
        return middle

    if value < search_list[middle]:
        return find(search_list[0: middle], value)

    if value > search_list[middle]:
        return middle + 1 + find(search_list[middle+1:], value)

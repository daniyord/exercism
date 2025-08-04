def proverb(*args, qualifier):
    result = []

    if len(args) == 0:
        return []

    for i in range(0, len(args) - 1):
        result.append(f"For want of a {args[i]} the {args[i + 1]} was lost.")

    if qualifier is not None:
        result.append(f"And all for the want of a {qualifier} {args[0]}.")
    else:
        result.append(f"And all for the want of a {args[0]}.")

    return result

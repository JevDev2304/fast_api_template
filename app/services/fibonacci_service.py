def linear_fibbo_with_seeds(n: int, seed_one: int, seed_two: int):
    if n < 0:
        raise ValueError("N is less than 0")
    array_solution = [None] * (n + 2)
    for i in range(len(array_solution)):
        if i == 0:
            array_solution[i] = seed_one
        elif i == 1:
            array_solution[i] = seed_two
        else:
            array_solution[i] = array_solution[i - 1] + array_solution[i - 2]
    return sorted(array_solution, reverse=True)

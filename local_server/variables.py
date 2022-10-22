def find_new_vars_and_stats(x):
    var = open("variables.txt", "r")
    saved = var.read().split("\n")
    var_to_review = x[0]
    new_variables = []
    for h in var_to_review:
        if h["name"] in saved:
            continue
        else:
            new_variables.append(h)

    stats = open("statuses.txt", "r")
    saved_stat = stats.read().split("\n")
    stat_to_review = x[1]
    new_statues = []
    for y in stat_to_review:
        if y["name"] in saved_stat:
            continue
        else:
            new_statues.append(y)

    return [new_variables, new_statues]               

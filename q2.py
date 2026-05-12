import statistics

data = [10, 20, 30, 40, 50, 60, 70]

def list_to_matrix(lst):
    while len(lst) < 9:
        lst.append(None)

    matrix = []

    for i in range(0, 9, 3):
        matrix.append(lst[i:i+3])

    return matrix


def tuple_statistics(lst):

    t = tuple(lst)

    clean_data = []

    for i in t:
        if i is not None:
            clean_data.append(i)

    mean = statistics.mean(clean_data)
    median = statistics.median(clean_data)
    mode = statistics.mode(clean_data)

    return {
        "Tuple": t,
        "Mean": mean,
        "Median": median,
        "Mode": mode
    }


def process_data(lst):

    matrix_result = list_to_matrix(lst.copy())

    stats_result = tuple_statistics(lst.copy())

    result = {
        "Matrix": matrix_result,
        "Statistics": stats_result
    }

    return result


output = process_data(data)

print(output)
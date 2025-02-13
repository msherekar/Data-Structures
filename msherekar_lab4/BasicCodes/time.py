from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    """
    This method is to time the algorithms
    :param algorithm: name of the algorithm
    :param array: list of data
    :return: time
    """

    setup_code = f"from__main__import {algorithm}"
    if algorithm != "sorted":

        stmt = f"{algorithm}({array}"
        times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
        print(f"Algorithm: {algorithm}. Minimum execution time:{min(times)}")

    else:
         ""

Array_Length = 10000
if __name__ == "__main__":
    # generate array of random integers
    array = [randint(0, 1000) for i in range(Array_Length)]

    run_sorting_algorithm(algorithm="sorted", array=array)

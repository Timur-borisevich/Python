
import random

from datetime import datetime

from pandas import DataFrame


def generate_random_table(size):
    result = []
    for _ in range(size):
        result.append(
            [random.randint(1, 100), random.randint(1, 100)]
        )
    return result


def measure_time(fn):
    def wraper(*args, **kwargs):
        start = datetime.now()
        result = fn(*args, **kwargs)
        delta = datetime.now() - start
        print("Функция " + fn.__name__ + " исполнялась: " + str(delta.total_seconds()) + " секунд")
        return result
    return wraper


@measure_time
def using_python_for(table):
    result = []
    for row in table:
        new_row = []
        for value in row:
            new_row.append(value / 3)
        result.append(new_row)
    return result


@measure_time
def using_pandas_dataframe(df):
    df = df / 3
    return df


def experiment():
    table = generate_random_table(10000000)
    res1 = using_python_for(table)
    df = DataFrame(table)
    res2 = using_pandas_dataframe(df)


experiment()
experiment.py
experiment.py. На экране.
from multiprocessing import Pool
"""
Use Pool:

When you have many tasks that can be executed concurrently (especially short tasks).
For task parallelism, where each process executes the same function on different data.
When you want to minimize the overhead of manually creating and managing processes.
"""

def square(x):
    return x * x

if __name__ == '__main__':
    with Pool(4) as pool:
        result = pool.map(square, [1,2,3,4,5])

        print(result)

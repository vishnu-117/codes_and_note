from multiprocessing import Process, Pool
import time
"""
Use Process:

When you need full control over individual processes (e.g., custom configuration, starting/stopping processes manually).
For long-running processes where the overhead of creating and managing processes manually is not a concern.
When processes need to communicate with each other via pipes or queues.
"""

start = time.perf_counter()

def multiprocess(seconds):
    print(f'Sleeping {seconds} seconds(s)....')
    time.sleep(seconds)
    print('Done sleeping...')

processes = []

for _ in range(100):
    t = Process(target=multiprocess, args=[1])
    t.start()
    processes.append(t)

for p in processes:
    p.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} time")


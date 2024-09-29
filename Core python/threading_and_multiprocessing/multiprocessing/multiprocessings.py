from multiprocessing import Process
import time

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


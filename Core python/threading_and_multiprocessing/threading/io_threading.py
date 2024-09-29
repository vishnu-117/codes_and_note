import threading
import time

start = time.perf_counter()

def io_bound_task(seconds):
    print(f'Sleeping {seconds} seconds(s)....')
    time.sleep(seconds)
    print('Done sleeping...')

threads = []

for _ in range(10):
    t = threading.Thread(target=io_bound_task, args=[1.5])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} time")


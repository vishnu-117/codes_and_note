from concurrent.futures import ThreadPoolExecutor
import time

start = time.perf_counter()

def io_bound_task(seconds):
    print(f'Sleeping {seconds} seconds(s)....')
    time.sleep(seconds)
    return 'Done sleeping...'


with ThreadPoolExecutor(max_workers=5) as executer:
    futures = [executer.submit(io_bound_task, sec) for sec in [1,2,3,4,5]]

    for future in futures:
        print(future.result())

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} time")


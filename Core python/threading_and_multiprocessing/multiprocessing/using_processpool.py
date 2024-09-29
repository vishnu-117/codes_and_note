from concurrent.futures import ProcessPoolExecutor
import time

start = time.perf_counter()

def multiprocess(seconds):
    print(f'Sleeping {seconds} seconds(s)....')
    time.sleep(seconds)
    return 'Done sleeping...'


with ProcessPoolExecutor(max_workers=50) as executer:
    futures = [executer.submit(multiprocess, 1) for sec in range(50)]

    for future in futures:
        print(future.result())

finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} time")


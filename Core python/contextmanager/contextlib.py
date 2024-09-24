from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    except:
        f.close

with file_manager("example.py", "w") as f:
    f.write('using contextmanager...')
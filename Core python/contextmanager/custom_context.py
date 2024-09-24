class FileManager:

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print('__enter__ method called..')
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, trackback):
        print('__exit__ method called..')
        if self.file:
            self.file.close()

with FileManager('example.txt', 'w') as f:
    print('inside...')
    f.write('Custom context manager......')



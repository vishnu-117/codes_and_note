class SingletonMeta(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        import pdb;pdb.set_trace()
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwargs)
            cls._instance[cls] = instance

        return cls._instance[cls]


class DatabaseConnection(metaclass=SingletonMeta):

    def __init__(self):
        self.connection_string = "Database=ExampleDB;User=admin;Password=password;"
        print(f"Initializing database connection: {self.connection_string}")
    
    def connect(self):
        return "Database connection established."

if __name__ == '__main__':
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()

    print(f"db1 is db2: {db1 is db2}")
    print(db1.connect())
    print(db2.connect())
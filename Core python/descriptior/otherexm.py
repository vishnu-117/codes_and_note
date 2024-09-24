class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(5, 3))  # Output: 8

class Employee:
    company_name = "TechCorp"

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

Employee.change_company_name("NewTech")
print(Employee.company_name)  # Output: NewTech

from functools import wraps

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def greet(name):
    return f"Hello {name}"

print(greet('vtu'))
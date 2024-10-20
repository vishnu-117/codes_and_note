from functools import wraps

class PermissionRequired:
    def __init__(self, permission):
        self.permission = permission

    def __call__(self, func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if self.permission not in user.permissions:
                raise PermissionError(f"User does not have '{self.permission}' permission")
            return func(user, *args, **kwargs)
        return wrapper

# Example User class
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

# Example usage
@PermissionRequired('read')
def view_document(user):
    return "Viewing document"

@PermissionRequired('write')
def edit_document(user):
    return "Editing document"

# Test cases
if __name__ == "__main__":
    user1 = User("Alice", ['read'])
    user2 = User("Bob", ['read', 'write'])

    try:
        print(view_document(user1))  # Should succeed
        print(edit_document(user1))  # Should raise PermissionError
    except PermissionError as e:
        print(e)
    
    try:
        print(edit_document(user2))  # Should succeed
    except PermissionError as e:
        print(e)

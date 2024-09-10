from functools import wraps

# Permission decorator function
def requires_permission(permission):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if permission not in user.permissions:
                raise PermissionError(f"User does not have '{permission}' permission")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

# Example User class
class User:
    def __init__(self, username, permissions):
        self.username = username
        self.permissions = permissions

# Example usage
@requires_permission('read')
def view_document(user):
    return "Viewing document"

@requires_permission('write')
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

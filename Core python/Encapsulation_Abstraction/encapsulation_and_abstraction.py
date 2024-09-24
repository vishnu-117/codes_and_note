from abc import ABC, abstractmethod


class SocialMediaUser(ABC):
    def __init__(self, user_id, username, email):
        self.__user_id = user_id
        self._username = username
        self.__email = email
        self._followers = []
    
    @property
    def user_id(self):
        """Property decorator to get the private user ID."""
        return self.__user_id
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if not value:
            raise ValueError("Username cannot be empty.")
        self._username = value
    
    @property
    def email(self):
        return self.__email
    
    @abstractmethod
    def post_content(self, content):
        pass

    @abstractmethod
    def get_user_details(self):
        pass

    def follow(self, other_user):
        if other_user not in self._followers:
            self._followers.append(other_user)
            print(f"{self.username} is now following {other_user.username}.")
        else:
            print(f"{self.username} is already following {other_user.username}.")


class RegularUser(SocialMediaUser):

    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)
        self._posts = []
    
    def post_content(self, content):
        self._posts.append(content)
        print(f"{self.username} posted: {content}")
    
    def get_user_details(self):
        return f"User ID: {self.user_id}, Username: {self._username}, Email: {self.email}, Followers: {len(self._followers)}, Post count: {len(self._posts)}"


class Influencer(SocialMediaUser):
    """Class representing an influencer on the social media platform."""

    def __init__(self, user_id, username, email, sponsorships):
        super().__init__(user_id, username, email)
        self.__sponsorships = sponsorships  # Private attribute to store sponsorship deals
        self._posts = []  # Protected attribute to store posts

    @property
    def sponsorships(self):
        """Property decorator to get the private sponsorships."""
        return self.__sponsorships

    @sponsorships.setter
    def sponsorships(self, value):
        """Property decorator to set the private sponsorships."""
        if value < 0:
            raise ValueError("Sponsorship deals must be positive.")
        self.__sponsorships = value

    def post_content(self, content):
        """Method for an influencer to post content."""
        self._posts.append(content)
        print(f"{self.username} (Influencer) posted: {content} with sponsorship deals: {self.__sponsorships}")

    def get_user_details(self):
        """Implementation of abstract method to get user details."""
        return f"Influencer ID: {self.user_id}, Username: {self._username}, Email: {self.email}, Followers: {len(self._followers)}, Posts: {len(self._posts)}, Sponsorships: {self.__sponsorships}"


class Administrator(SocialMediaUser):
    """Class representing an administrator on the social media platform."""

    def __init__(self, user_id, username, email):
        super().__init__(user_id, username, email)
        self._managed_users = []  # Protected attribute to store managed users

    def post_content(self, content):
        """Method for an administrator to post platform-wide content."""
        print(f"Administrator {self.username} posted platform announcement: {content}")

    def get_user_details(self):
        """Implementation of abstract method to get administrator details."""
        return f"Administrator ID: {self.user_id}, Username: {self._username}, Email: {self.email}, Managed Users: {len(self._managed_users)}"

    def manage_user(self, user):
        """Method for an administrator to manage a user."""
        self._managed_users.append(user)
        print(f"Administrator {self.username} is now managing user: {user.username}")

if __name__ == "__main__":
    regular_user = RegularUser("U001", "john_doe", "john@example.com")
    influencer = Influencer("U002", "jane_influencer", "jane@example.com", 5)
    admin = Administrator("U003", "admin_user", "admin@example.com")

    print(regular_user.get_user_details())  # Get regular user details
    print(influencer.get_user_details())  # Get influencer details
    print(admin.get_user_details())  # Get administrator details

    regular_user.post_content("Hello, this is my first post!")  # Regular user posts content
    influencer.post_content("Check out this new product!")  # Influencer posts content
    admin.post_content("Welcome to the new social media platform!")  # Administrator posts content

    regular_user.follow(influencer)  # Regular user follows influencer
    influencer.follow(regular_user)  # Influencer follows regular user
    admin.manage_user(influencer)  # Admin manages influencer

    print(influencer.get_user_details())  # Updated influencer details

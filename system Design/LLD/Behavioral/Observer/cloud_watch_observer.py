from abc import ABC, abstractmethod
import random
import time

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Concrete Observer: EmailNotifier
class EmailNotifier(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, message: str):
        print(f"Sending email to {self.email}: {message}")

# Concrete Observer: SMSNotifier
class SMSNotifier(Observer):
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def update(self, message: str):
        print(f"Sending SMS to {self.phone_number}: {message}")

# Subject Interface
class Subject(ABC):
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Concrete Subject: CloudWatch
class CloudWatch(Subject):
    def __init__(self):
        super().__init__()

    def check_cpu_usage(self):
        # Simulate random CPU usage
        cpu_usage = random.randint(0, 100)
        print(f"Current CPU usage: {cpu_usage}%")
        
        if cpu_usage > 60:
            self.notify(f"Alert: CPU usage is high at {cpu_usage}%")

# Example Usage
if __name__ == "__main__":
    # Create CloudWatch instance
    cloud_watch = CloudWatch()
    
    # Create observers
    email_notifier = EmailNotifier("admin@example.com")
    sms_notifier = SMSNotifier("+1234567890")
    
    # Attach observers
    cloud_watch.attach(email_notifier)
    cloud_watch.attach(sms_notifier)
    
    # Simulate periodic CPU checks
    for _ in range(5):
        cloud_watch.check_cpu_usage()
        time.sleep(2)  # Wait for 2 seconds before the next check

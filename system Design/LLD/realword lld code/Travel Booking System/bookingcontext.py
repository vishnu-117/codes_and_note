class BookingContext:
    """
    Context manager to handle the setup and teardown of booking sessions.
    Ensures resources are initialized and cleaned up properly.
    """

    def __enter__(self):
        print("Starting booking session...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Ending booking session...")
        if exc_type:
            print(f"Error occurred: {exc_val}")
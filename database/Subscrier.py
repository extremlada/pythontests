class Subscriber:
    def __init__(self, name: str):
        self.subscribers = name

    def get_subscribed_data(self)-> str:
        return self.subscribers

    def update(self, data: str)-> None:
        print("the initial  entry was: ", data)
        print(f"subscriber {self.subscribers} triggered")
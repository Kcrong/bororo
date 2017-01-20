from knowledge import Brain


class Bot:
    def __init__(self, name):
        self.name = name
        self.brain = Brain(self.name)

    def __repr__(self):
        return f"<Bot {self.name}>"

    def get_response(self, talk):
        return talk


if __name__ == '__main__':
    b = Bot(input("Bot Name: "))
    while True:
        print(b.name, ": ", b.get_response(input("To Bot: ")))

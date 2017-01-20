from bot import Bot

if __name__ == '__main__':
    b = Bot(input("Bot Name: "))
    while True:
        print(b.name, ": ", b.get_response(input("To Bot: ")))

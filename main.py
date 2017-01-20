from bot import Bot

if __name__ == '__main__':
    """
    b = Bot(input("Bot Name: "))
    while True:
        print(b.name, ": ", b.get_response(input("To Bot: ")))
    """
    b = Bot("Bororo")
    print(b.get_response("사과는 과일이다."))

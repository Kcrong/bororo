from bot import Bot

if __name__ == '__main__':

    b = Bot(input("Bot Name: "))
    while True:
        print(b.name, ": ", b.get_response(input("To Bot: ")))
        b.brain.print_my_knowledge()

    """
    b = Bot("Bororo")
    print(b.get_response("사과는 과일입니다."))
    b.brain.print_my_knowledge()
    """

    """
    ------------Brain Status------------
    Thing 사과 :
    >>> 사과's name is 사과
    >>> 사과's 과일 is True
    """

    """
    print(b.get_response("사과의 색깔은 빨간색 입니다."))
    b.brain.print_my_knowledge()
    print(b.get_response("아이유 콘서트 가고싶다."))
    b.brain.print_my_knowledge()
    print(b.get_response("나는 바보다"))
    b.brain.print_my_knowledge()
    print(b.get_response("나는 천재다"))
    b.brain.print_my_knowledge()
    print(b.get_response("손건은 남자다"))
    b.brain.print_my_knowledge()
    print(b.get_response("손건은 여자다."))
    """
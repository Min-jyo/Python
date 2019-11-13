from functions import play_game
from functions.shop import play_game as play_game_shop
from functions import shop
from friends.chat import send_message

if __name__ == '__main__':
    # input()을 이용해서 값을 받는다
    #  -> 적절히 1번은 게임실행, 2번은 아이템사기 라고 출력해주기
    # 받은 값이 1인 경우, game.play_game()을 실행
    # 받은 값이 2인 경우, shop.buy_item()을 실행
    # 받은 값이 0인 경우, 프로그램을 종료
    #  0이 아닌 값을 받은 경우 다시 input()을 이용해서 실행할 명령을 받도록 한다 (무한반복, while문을 사용)
    print('= Turn on game =')

    while True:
        val = input('1: 게임실행, 2: 아이템사기, 3: 메세지 보내기, 0: 종료\n입력: ')
        if val == '1':
            play_game()
            play_game_shop()
            shop.play_game()
        elif val == '2':
            shop.buy_item()
        elif val == '3':
            send_message()
        elif val == '0':
            break
        print()

def greet():
    name = input('Enter your name:')
    return name


def read_file_name(path='rating.txt'):
    with open(path, 'r') as file_name:
        return file_name.readlines()


def player_rating(name_list, player_name):
    for i in name_list:
        name, rating = i.split()
        if player_name == name:
            return int(rating)
    return 0


def make_win_list(game_list):
    if not game_list:
        game_list ='rock,paper,scissors'
    else:
        print("Okay, let's start")
    new_list = game_list.split(',')
    n = round(len(new_list) / 2)
    l = len(new_list)
    win_dict = dict()
    for i in range(l):
        if i - n >= 0:
            start = (i - n) + 1
            end = i
            win_dict[new_list[i]] = new_list[start:end]
        else:
            start = i + n
            total = new_list[:i] + new_list[start:]
            win_dict[new_list[i]] = total
    return win_dict, new_list


def current_rating(rating):
    print(r'Your rating: {rating}')


def main():
    exit_ = True
    current_socre = 0
    name = greet()
    player_list = read_file_name()
    print(f'Hello, {name}')
    player_options = input()
    game_win_choice, game_choice = make_win_list(player_options)

    while exit_:
        import random
        system_choice = random.choice(game_choice)
        player_choice = input().lower()
        if player_choice == '!exit':
            exit_ = False
            print('Bye!')
            continue
        if player_choice == '!rating':
            rating = player_rating(name_list=player_list, player_name=name)
            print(f'Your rating: {rating + current_socre}')
            continue
        if player_choice not in game_choice:
            print('Invalid input')
            continue
        if player_choice == system_choice:
            print(f'There is a draw ({system_choice})')
            current_socre += 50

        elif system_choice not in game_win_choice[player_choice]:
            print(f'Sorry, but computer chose {system_choice}')
        else:
            print(f'Well done. Computer chose {system_choice} and failed')
            current_socre += 100


main()

#!/usr/bin/python3

import play_with_PC_lib as lib


def main():
    print(f'{lib.bcolors.HEADER}{lib.bcolors.UNDERLINE}hi looser! dare you play 2001 with me?{lib.bcolors.ENDC}')
    player_1_points = 0
    player_2_points = 0
    rounds = 1
    available_dices = [3, 4, 6, 8, 10, 12, 20, 100]
    while True:
        round_player_1_points = 0
        round_player_2_points = 0
        print(f'{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}your points: {player_1_points}{lib.bcolors.ENDC}')
        print(f"{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}computer's points: {player_2_points}{lib.bcolors.ENDC}")
        print(f"{lib.bcolors.OKGREEN}round {rounds}{lib.bcolors.ENDC}")

        # x = input('press enter to throw dices')  # comment this line if you're lazy :)

        # print('throwing your dices')
        for _ in range(2):
            kind_of_dice = 0
            while True:
                try:
                    kind_of_dice = int(input('what dice do you want to throw? \ntype 3, 4, 6, 8, 10, 12, 20, 100 \n'))
                except:
                    print('exception. number incorrect. try again')
                    continue
                if kind_of_dice == 3 or kind_of_dice == 4 or kind_of_dice == 6 or kind_of_dice == 8 or kind_of_dice == 10 or kind_of_dice == 12 or kind_of_dice == 20 or kind_of_dice == 100:
                    round_player_1_points += lib.throw(kind_of_dice)
                    break
                else:
                    print('number incorrect. try again')
                    continue
            # print(round_player_1_points)

        # print("throwing computer's dices")
        for _ in range(2):
            round_player_2_points += lib.throw(lib.kind_of_dice_computer())
            # print(round_player_2_points)

        if rounds > 1:
            if round_player_1_points == 7:
                player_1_points = player_1_points % 7
                # print('dividing player 1')
            elif round_player_1_points == 11:
                player_1_points = player_1_points * 11
                # print('multiplying player 1')
            else:
                player_1_points += round_player_1_points
                # print('summing player 1')

            if round_player_2_points == 7:
                player_2_points = player_2_points % 7
                # print('dividing player 2')
            elif round_player_2_points == 11:
                player_2_points = player_2_points * 11
                # print('multiplying player 2')
            else:
                player_2_points += round_player_2_points
                # print('summing player 2')

        else:
            player_1_points += round_player_1_points
            player_2_points += round_player_2_points

        rounds += 1

        if player_1_points >= 2001 and player_2_points >= 2001:
            print(f'{lib.bcolors.FAIL}you both won{lib.bcolors.ENDC}')
            print(f'{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}your points: {player_1_points}{lib.bcolors.ENDC}')
            print(f"{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}computer's points: {player_2_points}{lib.bcolors.ENDC}")
            print(f"{lib.bcolors.OKGREEN}round {rounds}{lib.bcolors.ENDC}")
            break
        elif player_1_points >= 2001:
            print(f'{lib.bcolors.FAIL}you won{lib.bcolors.ENDC}')
            print(f'{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}your points: {player_1_points}{lib.bcolors.ENDC}')
            print(f"{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}computer's points: {player_2_points}{lib.bcolors.ENDC}")
            print(f"{lib.bcolors.OKGREEN}round {rounds}{lib.bcolors.ENDC}")
            break
        elif player_2_points >= 2001:
            print(f'{lib.bcolors.FAIL}computer won{lib.bcolors.ENDC}')
            print(f'{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}your points: {player_1_points}{lib.bcolors.ENDC}')
            print(f"{lib.bcolors.OKBLUE}{lib.bcolors.BOLD}computer's points: {player_2_points}{lib.bcolors.ENDC}")
            print(f"{lib.bcolors.OKGREEN}round {rounds}{lib.bcolors.ENDC}")
            break
        else:
            pass

    return 0


if __name__ == '__main__':
    main()

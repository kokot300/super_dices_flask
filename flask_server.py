#!/usr/bin/python3.8

from flask import Flask, request, render_template, flash
import play_with_PC_lib as lib

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        user_points = 0
        computer_points = 0
        rounds = 1
        msg = ''
        return render_template('form.html', user_points=user_points, computer_points=computer_points, msg=msg,
                               rounds=rounds)
    elif request.method == 'POST':
        msg = request.form.get('msg')
        if msg != '':
            user_points = 0
            computer_points = 0
            rounds = 1
            msg = ''
            return render_template('form.html', user_points=user_points, computer_points=computer_points, msg=msg,
                                   rounds=rounds)
        rounds = request.form.get('rounds')
        rounds = int(rounds)
        rounds += 1
        dice1 = request.form.get('select1')
        dice2 = request.form.get('select2')
        user_points = request.form.get('user_points')
        computer_points = request.form.get('computer_points')
        user_points = int(user_points)
        computer_points = int(computer_points)
        print(dice1)
        print(dice2)
        round_points = lib.throw(int(dice1)) + lib.throw(int(dice2))
        print(user_points, computer_points)
        print(round_points)

        if round_points == 7:
            user_points = user_points // 7
        elif round_points == 11:
            user_points = user_points * 11
        else:
            user_points += round_points

        round_points = 0
        print(round_points)

        for _ in range(2):
            round_points = lib.throw(lib.kind_of_dice_computer()) + lib.throw(lib.kind_of_dice_computer())

        print(round_points)

        if round_points == 7:
            computer_points = computer_points // 7
        elif round_points == 11:
            computer_points = computer_points * 11
        else:
            computer_points += round_points

        print(user_points, computer_points)

        msg = ''
        if user_points >= 2001 and computer_points >= 2001:
            msg = 'you both won!'
        elif user_points >= 2001:
            msg = 'you won'
        elif computer_points >= 2001:
            msg = 'server won'
        return render_template('form.html', user_points=user_points, computer_points=computer_points, msg=msg,
                               rounds=rounds)
    else:
        return "oh no, you've broken my server. \nTell me how contacting kokot300@gmail.com"


if __name__ == '__main__':
    app.run()

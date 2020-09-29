import random
moves=['rock','scissor','paper']

a='True'

while a=='True':
    player_1 = input('What do you want?;rock,scissor,paper:')
    player_2 = random.choice(moves)
    if player_1=='exit':
        break

    if player_1== player_2:
        print("It's tie")
    elif player_1== 'rock':
        if player_2== 'scissor':
            print('player_1 win')
        else:
            print('player_2 win')
    elif player_1=='scissor':
        if player_2=='paper':
            print('player_1 win')
        else:
            print('player_2 win')
    elif player_1=='paper':
        if player_2=='rock':
            print('player_2 win')
        else:
            print('player_1 win')

    else:

        break

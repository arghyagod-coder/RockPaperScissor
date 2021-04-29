import random

score = 0
comps = 0

while True:
    pl1 = input('Your Chance \n\nEnter R for Rock, S for Scissor, P for Paper. Or type exit to Stop the game:\n')

    choices = ['Rock', 'Paper', 'Scissor']
    comp = random.choice(choices)

    print(f'Computer laid out {comp}')

    # if condition is true: 
    #     do this

    if comp == 'Rock' and pl1 == 'P':
        print('Ah! You win this round, Congratulations!')
        score+=1
        comps-=1


    elif comp == 'Scissor' and pl1 == 'P':
        print('You lose this round, Better luck next time!')
        score-=1
        comps+=1

    elif comp == 'Paper' and pl1 == 'P':
        print('Nice Move! You tied to the Computer')


    elif comp == 'Paper' and pl1 == 'S':
        print('Ah! You win this round, Congratulations!')
        score+=1
        comps-=1

    elif comp == 'Rock' and pl1 == 'S':
        print('You lose this round, Better luck next time!')
        score-=1
        comps+=1

    elif comp == 'Scissor' and pl1 == 'S':
        print('Nice Move! You tied to the Computer')

    elif comp == 'Scissor' and pl1 == 'R':
        print('Ah! You win this round, Congratulations!')
        score+=1
        comps-=1

    elif comp == 'Paper' and pl1 == 'R':
        print('You lose this round, Better luck next time!')
        score-=1
        comps+=1
        

    elif comp == 'Rock' and pl1 == 'R':
        print('Nice Move! You tied to the Computer')

    elif pl1=='exit':
        print(f'''Your Score: {score}
Computer Score: {comps}\n''')
        if score>comps:
            print('You win the game! Congratulations!')
        elif comps>score:
            print('You lose! But no worry, Les put a smile on that face!')
        elif comps==score:
            print('This match was tied! You did pretty well!')
        exit()

    else:
        print('Invalid Input! Enter R, S, P or exit')
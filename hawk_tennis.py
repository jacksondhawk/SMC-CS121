#   Jackson Hawk
#   CS 21, Fall 2018
#   Program: tennis.py

from random import random


points = ['Love','15','30','40','Game']

def print_intro():
    print('The purpose of this code is to simulate a tennis game or set of\
 games.')
    print('The inputs to the program are the decimal chance between 0 and 1')
    print('which a given player, A, has of winning each point that is played.')
    print('')

def get_inputs():
    while True:
        try:
            games = int(input('How many games do you want to play: '))
            if games > 0:
                break
            else:
                print('The number of games is not positive. Try again.')
        except ValueError:
            print('Not an integer. Try again.')
    while True:
        try:
            prob_a = float(input('What chance does player A have of winning \
every point between 0 and 1: '))
            if prob_a <= 1 and prob_a >= 0:
                break
            else:
                print('The number is not between 0 and 1. Try again.')
        except ValueError:
            print('Not a decimal. Try again.')            

    return games,prob_a

def play_game1(prob_a):
            
    A = 0
    B = 0
    while True:
        if random() < float(prob_a):
            A +=1
        else:
            B +=1
        if A < 3 or B < 3 and A+B < 6:
            print('Current score:',points[A],'-',points[B])


        # if at deuce then use deuce scoring

        if A >= 3 and B >= 3 and A-B == 0:


            # make a while loop for duece scoring
            while int( abs(A-B)) < int(2):
                if int(A-B) == int(0):
                    print('Current score:','Deuce')
                if int(A-B) == int(1):
                    print('Current score:','Advantage A')
                if int(B-A) == int(1):
                    print('Current score:','Advantage B')
                if random() < float(prob_a):
                    A +=1
                else:
                    B +=1 
        elif A >= 4 and A > B:
                    print('The winner is A')
                    print(' ')
                    return 'A'
        elif B >= 4:
                    print('The winner is B')
                    print(' ')
                    return 'B'

def play_game(prob_a):
            
    A = 0
    B = 0
    while True:
        if random() < float(prob_a):
            A +=1
        else:
            B +=1
        if A < 3 or B < 3 and A+B < 6:
            'Current score:',points[A],'-',points[B]


        # if at deuce then use deuce scoring

        if A >= 3 and B >= 3 and A-B == 0:


            # make a while loop for duece scoring
            while int( abs(A-B)) < int(2):
                if int(A-B) == int(0):
                    'Current score:','Deuce'
                if int(A-B) == int(1):
                    'Current score:','Advantage A'
                if int(B-A) == int(1):
                    'Current score:','Advantage B'
                if random() < float(prob_a):
                    A +=1
                else:
                    B +=1 
        elif A >= 4 and A > B:
                    #print('The winner is A')
                    #print(' ')
                    return 'A'
        elif B >= 4:
                    #print('The winner is B')
                    #print(' ')
                    return 'B'
    
def play_games(games,prob_a):
    A_Games = 0
    B_Games = 0
    while int(A_Games + B_Games) < int(games):
        if play_game(prob_a) == 'A':
            A_Games += 1
            print('Game Score: ',A_Games,':',B_Games)
            print('')
            A = 0
            B = 0
        else:
            B_Games += 1
            print('Game Score: ',A_Games,':',B_Games)
            print('')
            A = 0
            B = 0
    return A_Games,B_Games

def print_summary(A_Games,B_Games):
    print('The match ended with Player A winning ',A_Games,'game(s) and \
Player B winning ',B_Games,'game(s)')
    print('Player A won',float(A_Games / (A_Games + B_Games) * 100),'% \
of games.')
    print('Thanks for playing!')



def play_set(prob_a):
    A_Games = 0
    B_Games = 0
    while True:
        if A_Games <= 5 and B_Games <= 5:
            if play_game(prob_a) == 'A':
                A_Games += 1
                #print('Game Score: ',A_Games,':',B_Games)
                #print('')
                A = 0
                B = 0
            else:
                B_Games += 1
                #print('Game Score: ',A_Games,':',B_Games)
                #print('')
                A = 0
                B = 0
        elif A_Games + B_Games >= 10 and A_Games == B_Games:
            if play_game(prob_a) == 'A':
                A_Games += 1
                #print('Game Score: ',A_Games,':',B_Games)
                #print('')
                A = 0
                B = 0
            else:
                B_Games += 1
                #print('Game Score: ',A_Games,':',B_Games)
                #print('')
                A = 0
                B = 0
        elif A_Games == 6 and B_Games == 5:
            if play_game(prob_a) == 'A':
                A_Games += 1
                print('Set Complete: ',A_Games,':',B_Games)
                print('')
                return 'Set A'
            else:
                B_Games += 1
                #print('Game Score: ',A_Games,':',B_Games)
                #print('')
                if play_tiebreak(prob_a) == 'Set A':
                    #print('Set Complete: ','7',':','6',Bt)
                    print('')
                    return 'Set A'
                else:
                    #print('Set Complete: ','6',':','7',At)
                    print('')
                    return 'Set B'
        elif A_Games == 5 and B_Games == 6:
            if play_game(prob_a) == 'A':
                A_Games += 1
                #print('Game Score: ',A_Games,':',B_Games)
                #print('')
                if play_tiebreak(prob_a) == 'Set A':
                    #print('Set Complete: ','7',':','6')
                    print('')
                    return 'Set A'
                else:
                    #print('Set Complete: ','6',':','7')
                    print('')
                    return 'Set B'
            else:
                B_Games += 1
                print('Set Complete: ',A_Games,':',B_Games)
                print('')
                return 'Set B'
        elif A_Games == 6 and B_Games <= 4:
            print('Set Complete: ',A_Games,':',B_Games)
            print('')
            return 'Set A'
        elif A_Games <= 4 and B_Games == 6:
            print('Set Complete: ',A_Games,':',B_Games)
            print('')
            return 'Set B'


def play_tiebreak(prob_a):
    At = 0
    Bt = 0

    while True:
        if random() < float(prob_a):
            At +=1
        else:
            Bt +=1
        if At <= 6 and Bt <= 6 and At+Bt < 12:
            'Tiebreak Score: ', At,'-',Bt
        elif At == 6 and Bt == 6 and At == Bt:
            while abs(At-Bt) <= 2:
                'Tiebreak Score: ', At,'-',Bt
                if random() < float(prob_a):
                    At += 1
                else:
                    Bt += 1
                if At >= 7 and At > Bt and At - Bt >= 2:
                    'Tiebreak Score: ',At,'-',Bt
                    print('Set Complete: ','7',':','6','(',Bt,')')
                    return 'Set A'
                elif Bt >= 7 and Bt > At and Bt - At >= 2:
                    "Tiebreak Score: ",At,'-',Bt
                    print('Set Complete: ','6',':','7','(',At,')')
                    return 'Set B'
        elif At >= 7 and At > Bt and At - Bt >= 2:
            'Tiebreak Score: ',At,'-',Bt
            print('Set Complete: ','7',':','6','(',Bt,')')
            return 'Set A'
        elif Bt >= 7 and Bt > At and Bt - At >= 2:
            "Tiebreak Score: ",At,'-',Bt
            print('Set Complete: ','6',':','7','(',At,')')
            return 'Set B'
        
def play_match(prob_a):
    A_Sets = 0
    B_Sets = 0
    while A_Sets < 2 and B_Sets < 2:
        if play_set(prob_a) == 'Set A':
            A_Sets += 1
        else:
            B_Sets += 1
    print('Set Score: ',A_Sets,':',B_Sets)
    return A_Sets,B_Sets
                    
def main():
    print_intro()
    games,prob_a = get_inputs()
    A_Games,B_Games = play_games(games,prob_a)
    print_summary(A_Games,B_Games)

                
                

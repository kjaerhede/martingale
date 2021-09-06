import random

tries = 1000
bet = 1
odds = 18/37
cap = 1000000

winnings = 0
bets = 0
rounds = 0
profits = []

for i in range(1,tries+1):
    winnings = 0
    bets = 0
    rounds = 0
    current_bet = bet
    while bets+current_bet < cap:
        bets+=current_bet
        rounds+=1
        if random.random()<=odds:
            winnings+=current_bet*2-bets
            current_bet = bet
            bets = 0
        else:
            current_bet*=2
    profits.append(winnings - bets)

print(f"Using the Martingale strategy for roulette {tries} times with a betting allowance of up to {cap} \
and a minimum/base bet of {bet}, we made an average profit of {sum(profits)/len(profits)}. We were profitable \
{sum(1 for i in profits if i>0)} times, indicating a success rate of {'{0:.1%}'.format(sum(1 for i in profits if i>0)/len(profits))}")    
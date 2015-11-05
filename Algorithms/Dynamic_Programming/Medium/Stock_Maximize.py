t = input()
for ti in range(t):
    n = input()
    stocks = map(int, raw_input().split(' '))
    transactions = [0 for x in range(n)]
    stocks.reverse()
    max_so_far = 0
    for i in range(n):
        if stocks[i] > max_so_far:
            transactions[i] = 0 #sell
            max_so_far = stocks[i]
        else:
            transactions[i] = 1 #buy
    stocks.reverse()
    transactions.reverse()
    bought_stocks = 0
    profit = 0
    for i in range(n):
        if transactions[i] == 1:
            bought_stocks += 1
            profit -= stocks[i]
        else:
            profit += stocks[i] * bought_stocks
            bought_stocks = 0
    print profit
        
        

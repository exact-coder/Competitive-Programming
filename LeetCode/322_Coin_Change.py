

def coinChange(coins, amount):
        amt = [amount + 1] * (amount + 1)
        amt[0] = 0
        print(amt)

        for i in range(1, amount + 1):
                for j in range(len(coins)):
                        if i >= coins[j]:
                                amt[i] = min(amt[i], 1 + amt[i - coins[j]])

        if amt[amount] < amount + 1:
                return amt[amount]
        return -1

print(coinChange([1,2,5],11))
print(coinChange([2],3))
print(coinChange([1],0))


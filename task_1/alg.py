import time



def find_coins_greedy(amount):
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
    
    return result

def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin
    
    return result

# Example usage
coins = [10, 6, 1]
amount = 1112

# Timing the greedy algorithm
start_time = time.time()
greedy_result = find_coins_greedy(amount)
end_time = time.time()
greedy_time = end_time - start_time
print("Greedy algorithm result:", greedy_result)
print("Greedy algorithm execution time: {:.16f} seconds".format(greedy_time))

# Timing the dynamic programming algorithm
start_time = time.time()
dp_result = find_min_coins(amount)
end_time = time.time()
dp_time = end_time - start_time
print("Dynamic programming result:", dp_result)
print("Dynamic programming execution time: {:.16f} seconds".format(dp_time))
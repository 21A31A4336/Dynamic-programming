coins=[1,2,5]
amount=5
memo=[0]*(amount+1)
for i in coins:
    for a in range(i,amount+1):
        memo[a]=memo[a-i]+1
print(memo)


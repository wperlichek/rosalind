from typing import Dict

MONTHS = 35
LITTER_SIZE = 2

# top down recursive with memoization
def rabbit_pairs(curr_month: int, dp: Dict[int,int]) -> int:
    if curr_month <= 0:
        return 0
    elif curr_month == 1:
        return 1
    elif curr_month in dp:
        return dp[curr_month]
    else:
        res = rabbit_pairs(curr_month-1, dp) + LITTER_SIZE * rabbit_pairs(curr_month-2, dp)
        dp[curr_month] = res
        return dp[curr_month]


dp : Dict[int,int] = {}
pairs = rabbit_pairs(MONTHS, dp)
print(str(pairs))



# Improve with DP to avoid duplicate calculations
# What is the state?
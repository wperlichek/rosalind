MONTHS = 35
LITTER_SIZE = 2

# Crude, recursive, time complexity O(2^n)
def rabbit_pairs(curr_month: int) -> int:
    if curr_month <= 0:
        return 0
    elif curr_month == 1:
        return 1
    else:
        return rabbit_pairs(curr_month-1) + LITTER_SIZE * rabbit_pairs(curr_month-2)

pairs = rabbit_pairs(MONTHS)
print(str(pairs))


# Improve with DP to avoid duplicate calculations
# What is the state?
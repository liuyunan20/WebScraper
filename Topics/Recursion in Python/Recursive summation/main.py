def rec_sum(n):
    # write the insides here!
    if n == 1:
        sum_natural = 1
    else:
        sum_natural = rec_sum(n - 1) + n
    return sum_natural

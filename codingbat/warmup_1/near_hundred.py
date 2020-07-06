# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False

def near_hundred(n):
    if n > 89 and n <111:
      return True
    elif n > 189 and n < 211:
      return True
    else:
      return False

#alternative
def near_hundred2(n):
    return ((abs(100 -n) <= 10) or (abs(200 - n)) <= 10))



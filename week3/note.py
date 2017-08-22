import math
def sqrtt(N):
  oldguess = -1
  guess = 1
  while abs(guess-oldguess) > 1:
    oldguess = guess
    guess = (guess + N/guess) / 2
  return guess
print(sqrtt(4))
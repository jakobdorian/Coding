def towerBreakers(n, m):
    # height of all towers is 1, p2 wins
    if m == 1:
        return 2
    # number of towers is even, p2 wins
    elif n % 2 == 0:
        return 2
    # number of towers is odd, p1 wins
    else:
        return 1
    
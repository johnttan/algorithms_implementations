# Top down recursive approach causes stackoverflow(max recursion limit reached)
def bottomUpCutRod(p, n):
    # r is dict of optimal solution to each subproblem j, with j as keys of dict
    r = {}
    r[0] = 0
    # s is dict of optimal subproblem (aka cut of rod) to use at each step.
    # so for 10:10, optimal cut would be to cut 10 off; for 9:3, optimal cut would be 3, then subtract 3 from 9, and lookup remaining 6:6 cut.
    s = {}
    # find solutions for each subproblem j
    for j in range(1, n+1):
        q = False
        # look through each subproblem of subproblem j (already solved and cached in dict r)
        # find optimal value by comparing q and price[i] + remainder[j-i]
        for i in range(1, j+1):
            prevQ = q
            q = max(q, p[i] + r[j-i])
            # log cut i to cache s. this is the optimal cut i you want when you have j length left.
            if prevQ < q:
                s[j] = i
        r[j] = q
    return r, s
# Test case 1
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = 10

print(bottomUpCutRod(p, n))
# returns ({0: 0, 1: 1, 2: 5, 3: 8, 4: 10, 5: 13, 6: 17, 7: 18, 8: 22, 9: 25, 10: 30}, {1: 1, 2: 2, 3: 3, 4: 2, 5: 2, 6: 6, 7: 1, 8: 2, 9: 3, 10: 10})
# in 0.2s
# O(mn) complexity.
# similar problem to knapsack.
from knapsackproblem import solveknapsack

def loadItems(filename):
  file = open(filename)
  size, numItems = [int(x) for x in file.readline().split(' ')]
  items = []
  for i in range(numItems):
    item = [int(x) for x in file.readline().split(' ')]
    items.append(item)
  return size, items

size, items = loadItems('knapsack_big.txt')
table = solveknapsack(size, items)
print(table[len(items)-1][size])
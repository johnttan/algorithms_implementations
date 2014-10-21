import random

letterset = "abicdefghijklmnopqrstuvwxyz "

def phrasegenerator(phrase, letterset, tryagain, generated):
    length = len(phrase)
    random.seed()
    for index in tryagain:
        generated[index] = letterset[random.randrange(0, 28)]
    return generated

def score(phrase, generated):
    score = 0
    tryagain = []
    for index, letter in enumerate(phrase):
        if generated[index] == letter:
            score += 1
        else:
            tryagain.append(index)

    if score != 0:
        return score / len(phrase), tryagain
    else:
        return 0, tryagain

def run(phrase, letterset):
    maxscore = 0
    counter = 0
    bestphrase = [0]*len(phrase)
    maxscore = 0
    scores = 0
    tryagain = [x for x in range(len(phrase))]
    while scores < 1:
        latestphrase = phrasegenerator(phrase, letterset, tryagain, bestphrase)
        scores, tryagain = score(phrase, latestphrase)
        if scores > maxscore:
            maxscore = scores
            bestphrase = latestphrase
        counter += 1
        # if counter % 10 == 0:
            # print("counter: ", counter, "Maxscore: ", maxscore)
            # print("bestphrase: ", ''.join(bestphrase))
            # print("currentphrase: ", ''.join(latestphrase), "score: ", scores)
    # print(phrase, 'Found in', counter, 'iterations.')
    return counter 

def averagerun(phrase, letterset):
    total = 0
    counter = 0
    average = 0
    while True:
        total += run(phrase, letterset)
        counter += 1
        average = total / counter
        if counter % 50 == 0:
            print("Average # of iterations: ", average, "at run:", counter)
    run(phrase, letterset)

averagerun('me thinks it is like a weasel', letterset)

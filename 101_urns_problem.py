import random


# returns a list of urn dicts
def createUrns():
    urns = []
    urnsCount = 101

    for urnIndex in range(urnsCount):
        urns.append({"red": urnIndex, "green": 100 - urnIndex})

    return urns


# returns a random urn dict and its position in the list
def pickUrn(urns):
    urnIndex = random.randint(0, 100)
    return [urns[urnIndex], urnIndex]


# pick from the same urn
def runSameUrnTest():
    urns = createUrns()
    chosenUrn, _ = pickUrn(urns)

    # is the random number <= to the number of red balls in the urn?
    firstBallIsRed = random.randint(1, 100) <= chosenUrn["red"]

    # account for the missing ball
    if firstBallIsRed:
        chosenUrn["red"] -= 1
    else:
        chosenUrn["green"] -= 1

    secondBallIsRed = random.randint(1, 99) <= chosenUrn["red"]

    # both draws are the same color
    return firstBallIsRed == secondBallIsRed


# pick from a different urn
def runDiffUrnTest():
    urns = createUrns()
    chosenUrn, urnIndex = pickUrn(urns)

    firstBallIsRed = random.randint(1, 100) <= chosenUrn["red"]

    # remove previous urn from list before picking another
    del urns[urnIndex]

    newUrn = urns[random.randint(0, 99)]

    # don't reduce the random number range here. new urn, no missing balls
    secondBallIsRed = random.randint(1, 100) <= newUrn["red"]

    return firstBallIsRed == secondBallIsRed


## MAIN

print("\rcalculating...", sep="", end="\r", flush=True)

# the results of each trial for each method of choosing
sameUrnResults = []
diffUrnResults = []

# perform and record the trials
numTrials = 100000
for trial in range(numTrials):
    sameUrnResults.append(runSameUrnTest())
    diffUrnResults.append(runDiffUrnTest())

# probability that each method will result in both draws being the same color
sameUrnProb = sameUrnResults.count(True) / 100000
diffUrnProb = diffUrnResults.count(True) / 100000

print("same urn: ", sameUrnProb)
print("different urn: ", diffUrnProb)
print("# of trials: ", numTrials)

# Programming for the Puzzled -- Srini Devadas
# You Will All Conform
# Input is a vector of F's and B's, in terms of forwards and backwards caps
# Output is a set of commands (printed out) to get either all F's or all B's
# Fewest commands are the goal

caps = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']
cap2 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'F', 'F']
cap3 = ['F', 'F', 'B', 'H', 'B', 'F', 'B', 'B', 'B', 'F', 'H', 'F', 'F']


def pleaseConform(c):
    # init var

    isFlipSection = False
    start = 0

    for i in range(1, len(caps)):
        # if caps are the same
        if c[start] == c[i]:
            continue

        # else caps are different
        if isFlipSection:
            end = i - 1
            # command flip
            if start != end:
                print("flip: from", start, "to", end)
            else:
                print("flip:", start)

        # change isFlipSection, start
        if c[i] != 'H':
            start = i
            isFlipSection = not isFlipSection
        else:
            start = i + 1


pleaseConform(cap3)

#Programming for the Puzzled -- Srini Devadas
#You Will All Conform
#Input is a vector of F's and B's, in terms of forwards and backwards caps
#Output is a set of commands (printed out) to get either all F's or all B's
#Fewest commands are the goal

input = 'BWWWWWBWWWW'

def encode(input):
    # add end-char
    input = input + '.'
    result = []

    start = 0
    for i in range(1, len(input)):
        if (input[i-1] == input[i]):
            continue
        result.append(str(i - start) + input[start])
        start = i
    return ''.join(result)

def decode(input):
    result = []
    start = 0
    alphaCount = 0
    result = []
    
    for i in range(1, len(input)):
        # Numeric
        if input[i].isalpha() == False:
            continue
        alphaCount = int(input[start:i])
        start = i+1
        for n in range(alphaCount):
            result.append(input[i])
    
    return ''.join(result)

# Run
encodedStr = encode(input)
print(encodedStr)
decodedStr = decode(encodedStr)
if decodedStr != input:
    SystemError('Error: %s != %s'  (input, decodedStr))
print(decodedStr)
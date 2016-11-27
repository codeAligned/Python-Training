
def scan(input):
    """Should take input
     and return a list of tuples build with
     correct assert as first element and
     element assert list as second  """


    directionsList = ['north', 'south', 'east', 'west']
    verbsList = ['go', 'kill', 'eat']
    stopsList = ['the', 'in', 'of']
    nounsList = ['bear', 'princess']

    result = []
    for word in input.split(' '):
        if word in directionsList:
            result += [('direction', word)]
        elif word in verbsList:
            result += [('verb', word)]
        elif word in stopsList:
            result += [('stop', word)]
        elif word in nounsList:
            result += [('noun', word)]
        elif unicode(word).isnumeric():
            result += [('number', int(word))]
        else:
            result += [('error', word)]
    return result



def getGrade(score):
    if score >= 80 and score <= 100:
        return 'A'
    elif score >= 60 and score < 80:
        return 'B'
    elif score >= 40 and score < 60:
        return 'C'
    elif score >= 0 and score < 40:
        return 'D'
    else:
        'Unknown Grade'


def getMeanScore(score):
    return score


def getSum(score):
    return sum(score)
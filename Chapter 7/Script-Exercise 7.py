def check(file):
    stud = open(file, 'r')
    corr = open('Correct.txt', 'r')

    stAns = stud.read().splitlines()
    coAns = corr.read().splitlines()

    stud.close()
    corr.close()

    wrong = 0
    wrongList = []
    for i in range(0, len(coAns) - 1):
        if coAns[i] != stAns[i]:
            wrong += 1
            wrongList.append(i+1)

    if wrong < 5:
        print("Passed!")
        print("Correct:", len(coAns) - wrong)
        print("Incorrect:", wrong)
        print("Incorrect questions:", wrongList)
    else:
        print("Failed!")
        print("Correct:", len(coAns) - wrong)
        print("Incorrect:", wrong)
        print("Incorrect questions:", wrongList)

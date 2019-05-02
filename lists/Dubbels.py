def dubbels(lijst):
    oplossing = []

    for i in lijst:
        if lijst.count(i) > 1 and i not in oplossing:
            oplossing.append(i)
    return oplossing
print(dubbels([1, 1, 3, 3, 'joris', 'joris']))
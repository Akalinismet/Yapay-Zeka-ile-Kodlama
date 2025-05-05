numaralar = [8, 3, 8, 1, 2, 3, 5, 5]

benzersiz = []
for num in numaralar:
    if num not in benzersiz:
        benzersiz.append(num)

print(benzersiz)

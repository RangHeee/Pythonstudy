apart = [ [101, 102], [201, 202], [301, 302] ]

def hamsu(apart):
    for floor in apart:
        for ho in floor:
            print(ho, "호")
    print("-" * 5)

hamsu(apart)

print(apart[1][0])
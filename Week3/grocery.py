grocery = {}

while True:
    try:
        item = input().strip().upper()
        if item not in grocery:
            grocery[item] = 1
        else:
            grocery[item] += 1
    except EOFError:
        sor_dict = dict(sorted(list(grocery.items())))
        for item in sor_dict:
            print(sor_dict[item], item, sep=" ")
        break
    except KeyError:
        pass

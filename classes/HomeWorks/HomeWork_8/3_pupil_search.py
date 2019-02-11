with open('pupils_db', 'r') as db:
    rows = [row.split() for row in db.readlines()]

    data = {
        input('Enter first name: '),
        input('Enter last name: '),
        input('Enter gender (male/female): '),
        input('Enter age: ')
    }.difference({'',})

    search = ('{r[0]} {r[1]}, gender: {r[2]}, age: {r[3]}'.format(r=res) for res in rows if set(res).issuperset(data))
    print(*search, sep='\n')
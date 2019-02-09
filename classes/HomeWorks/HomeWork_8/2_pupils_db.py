with open('pupils_db', 'r') as db:
    rows = [row.split() for row in db.readlines()]
    pupil_3 = [(pupil[0], pupil[1]) for pupil in rows if int(pupil[3]) >= 3]
    average = sum((int(row[3]) for row in rows))/len(rows)
    print('Pupils:', *(' '.join(row) for row in pupil_3), '\nAverage grade: {}'.format(average), sep='\n')
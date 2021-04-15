import csv as c
def peliculas2020 (csvreader):
    encabezado=next(csvreader)
    print(encabezado)
    return filter(lambda x: x[6][-5:-4]==' ',csvreader)



with open('desafios/netflix_titles.csv', 'r') as nfx:
    csvreader = c.reader(nfx,delimiter=',')
    peliculas=peliculas2020(csvreader)
    with open ('desafios/netflix_2020.csv','w') as netflix_2020:
        csvwriter = c.writer(netflix_2020)
        for e in peliculas:
            csvwriter.writerow(e)


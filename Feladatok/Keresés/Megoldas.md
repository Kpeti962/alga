#### Azzal kezdeném a kifejtését a feladatnak, hogy 8/4 teszteset futott csak le jól, sajnos, de egyelőre inkább beadnám így, mint sehogy

#### Az n és m változónak odaadjuk a matrix sorainak és oszlopainak számát. a start és célnak mégnincsenek kezdőértékei, ezek lesznek majd a kezdőpont és a hop-port helye

    n = len(matrix)
    m = len(matrix[0])

    start = None
    cel = None

#### két egymásba rakott for ciklussal bejárjuk a mátrixot és megkeressük az "M" és a "*" helyét, amiket elmentünk a start és cél változóba.
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 'M':
                start = (x, y)
            elif matrix[x][y] == '*':
                cel = (x, y)
    
#### az ugrasok tartalmazza a lehetséges lépéseket

    ugrasok = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#### a jolepes függvény biztosítja, hogya lépéssel ne lépjünk ki a mátrixból

    def joLepes(x, y):
        return 0 <= x < n and 0 <= y < m and matrix[x][y] in ('.', '*')

### A bejaras függvényben, amihez meadtuk az aktuális lépés és a meglátogatott mező koordinátáit ezeket találjuk:

#### Ha x és y megegyezik a céllal, akkor kilépünk a függvényből.

    if (x, y) == cel:
            return 0 

#### A visited változóba elmentjük a megkapott x és y koordinátát
    
     visited.add((x, y))

#### A lehetosegek változót beállítjuk 0-ra kezdetben

     lehetosegek = 0

#### Ugrásokon iterálunk végig, ahol a jelenlegi helyzethez hozzáadjuk őket, és a jolepes fgv-t meghívva megnézzük, hogy látogattuk-e már az adott mezőket, ha nem, akkor annyival több lépéslehetőségünk van.

    for dx, dy in ugrasok:
        nx, ny = x + dx, y + dy
        if joLepes(nx, ny) and (nx, ny) not in visited:
            lehetosegek += 1

#### Beállítjuk a dontesek változót, ami 1-et ad vissza, ha 1-nél több lehetőségünk van.

    dontesek = 1 if lehetosegek > 1 else 0

#### A következő for loopban ellenőrizzük ugyanúgy, hogy létezik-e az a helye a mátrixnak, ahova lépnénk, ezután a dontesek += bejaras(nx, ny, visited) rekurzívan meghívja a függvényt, hogy elkezdje bejárni a következő helyet.

     for dx, dy in ugrasok:
        nx, ny = x + dx, y + dy
        if joLepes(nx, ny) and (nx, ny) not in visited:
            dontesek += bejaras(nx, ny, visited)

#### A végén meghatározzuk a döntséek számát, amit összehasonlítunk a k-val, ez alapján megkapjuk Ron válaszát

    dontesekSzama = bejaras(start[0], start[1], set())
    
    return "Impressed" if dontesekSzama == k else "Oops!"
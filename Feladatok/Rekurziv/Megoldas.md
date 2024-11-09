#### Először létrehozunk egy üres dictionary-t, amiben majd tároljuk az adott halmazméreteket

    memo = {};

#### Itt lecsekkoljuk, hogy a halmaz mérethez tartozó lépésszám már benne van-e a szótárban, ha igen, akkor visszaadja az értéket.

    if halmaz_meret in memo:
        return memo[halmaz_meret];

#### Beállítjuk a maximális rakás számát 0-ra.

    max_rakod_szam = 0;

#### Ezután jön egy for loop ami végigmegy az S halmaz minden elemén (az osztókon), hogy megnézze, hogyan lehet felosztani a halmazt az x osztók segítségével.
#### Ellenőrizzük, hogy az x osztója-e a jelenlegi halmaz méretének és hogy kisebb-e annál, hogy ne hozzon létre nagyobb méretű halmazokat. Ha ezek teljesülnek, akkor  fel tudjuk osztani a halmazt.
#### Kiszámoljuk, hogy hány kisebb halmaz keletkezik az osztás után
#### Meghivjuk rekurzívan a max_rakod(x) függvényt, hogy meghatározzuk az x méretű halmazból kiindulva a maximálisan végrehajtható lépések számát. Mivel az osztás után halmaz_szam darab kisebb halmaz lesz, ezért az eredményt megszorozzuk halmaz_szam-mal, a + 1 pedig hozzáad egy lépést az osztásért, amelyet most végeztünk.
#### A max_rakod_szam változót frissítjük, hogy tárolja a legnagyobb eddig elért lépésszámot az aktuális kupacmérethez.

    for x in s:
        if halmaz_meret % x == 0 and x < halmaz_meret:
            halmaz_szam = halmaz_meret // x;
            moves = halmaz_szam * max_rakod(x) + 1;
            max_rakod_szam = max(max_rakod_szam, moves);

#### Ezután elmentjük a max_rakod_szam értékéta memo-ba,hogy később el tudjuk érni, majd visszatérünk a maximálisan megcsinálható lépések számával.

    memo[halmaz_meret] = max_rakod_szam;
    return max_rakod_szam;

#### Ezután a fő függvény meghivja a max_rakod függvényt a teljes halmazméret értékével.

    return max_rakod(n);
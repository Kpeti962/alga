# Stone Division, Revisited feladatleírás

## Forrás:
#### https://www.hackerrank.com/challenges/stone-division-2/problem
---

#### Van egy kupac, amelyben 𝑛 darab kő van, és ezt kell több kisebb kupacra osztani. Emellett adott egy 𝑆 halmaz, amelyben m különböző egész szám található. Egy lépést a következőképpen definiálunk:

##### 1. Először válassz egy kőkupacot. Tegyük fel, hogy a választott kupacban 𝑦 kő van.

##### 2. Ezután keress egy olyan x-et, amely eleme S-nek, hogy 𝑥≠𝑦 és 𝑦 osztható x-szel (azaz x osztója y-nak). Ha ilyen x létezik, akkor a kupacot feloszthatod y/x egyenlő kisebb kupacra.

#### A feladatban q lekérdezés van, ahol minden lekérdezés tartalmazza n-t és S-t. Minden lekérdezéshez számold ki, hogy maximálisan hány lépést tudsz végrehajtani, és írd ki az eredményt egy új sorban.

### Bemeneti formátum
#### Az első sor egy egész számot, q-t tartalmaz, amely a lekérdezések számát jelöli. Az ezt követő 2×q sor írja le az egyes lekérdezéseket az alábbi formátumban:

##### Az első sor két szóközzel elválasztott egész számot tartalmaz, n-t (a kezdő kupac méretét az adott lekérdezésben) és m-et (a halmaz méretét az adott lekérdezésben).
##### A második sor m különböző, szóközzel elválasztott egész számot tartalmaz, amelyek az S halmaz elemeit adják meg.

### Kimeneti formátum
#### Minden lekérdezéshez számold ki, hogy maximálisan hány lépést lehet végrehajtani, és az eredményt írd ki egy új sorban.
# Equal feladatleírás

## Forrás:
#### https://www.hackerrank.com/challenges/equal/problem
---

#### Christy a HackerRanknél gyakornokoskodik. Egyik nap csokoládét kell kiosztania a kollégáinak. Elfogult a barátaival szemben, és azt tervezi, hogy nekik több csokit ad, mint a többieknek. Az egyik programmenedzser azonban ezt meghallja, és megmondja neki, hogy gondoskodjon róla, hogy mindenki ugyanannyi csokoládét kapjon.

#### Hogy nehezebb legyen, minden egyes lépésben ugyanannyi csokoládét kell adnia mindenkinek, kivéve egy kollégát. Azok, akik kapnak csokoládét, ugyanannyi darabot kapnak egy körben (1, 2 vagy 5 csokit).

#### Az a feladat, hogy a kezdeti csokoládé-elosztásból a lehető legkevesebb lépéssel elérjük, hogy minden kollégának ugyanannyi csokoládéja legyen.

## Példa:

#### Tegyük fel, hogy az arr = [1, 1, 5].

#### Ez az elosztás azt mutatja, hogy a kollégáknál kezdetben a következő csokoládé darabszámok vannak: [1, 1, 5].

#### Első lépés: Christy adhat 2 csokit az első két kollégának, így az új elosztás: [3, 3, 5].
#### Második lépés: Ismét adhat 2 csokit az első két kollégának, így az elosztás [5, 5, 5] lesz.
#### Most minden kollégának ugyanannyi csokija van, így megállhatunk. A szükséges körök száma: 2.

#### Visszatérési érték
#### A feladat szerint a megoldás 2-t ad vissza, mert ennyi körre volt szükség ahhoz, hogy minden kollégának ugyanannyi csokija legyen.
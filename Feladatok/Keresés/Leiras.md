# Count Luck feladatleírás

## Forrás:
#### https://www.hackerrank.com/challenges/count-luck/problem
---


#### Ron és Hermione mélyen bent vannak a Tiltott Rengetegben bájital hozzávalókat gyűjtve, és közben sikerült eltévedniük. Az erdőből kivezető út le van zárva, ezért egy hop-portra kell eljutniuk, ami visszaviszi őket a Roxfortba.

#### Tekintsük az erdőt egy N x M méretű rácsként. Minden mező vagy üres (jele: .), vagy egy fa blokkolja (jele: X). Ron és Hermione (egy mezőn együtt mozogva) balra, jobbra, fel és le tudnak mozogni az üres mezőkön keresztül, de egy fa mezőn nem tudnak áthaladni. A kezdő mezőjüket az M karakter jelzi, míg a hop-port helyét a * karakter. A bal felső sarok (0, 0) indexen található.

    .X.X......X
    .X*.X.XXX.X
    .XX.X.XM...
    ......XXXX.

#### A fenti példában Ron és Hermione a (2, 7) indexnél helyezkednek el, míg a hop-port a (1, 2) helyen található. Minden mezőt a mátrix konvenciói alapján indexelünk. Hermione úgy dönt, hogy ideje megtalálni a hop-portot és elhagyni a rengeteget. Elindulnak az ösvényen, és valahányszor irányt kell választaniuk, Hermione megrázza a pálcáját, ami a helyes irányba mutat. Ron arra fogad, hogy Hermione pontosan k alkalommal fogja megrázni a pálcáját. Meg tudod mondani, hogy Ron tippje helyes-e? A fenti térkép át lett rajzolva az ösvény jelölésével: M a kezdőpontot jelzi (itt nincs döntési pont), 1 egy döntési pontot jelöl, míg 0 az ösvény egy egyszerű lépése:

    .X.X.10000X
    .X*0X0XXX0X
    .XX0X0XM01.
    ...100XXXX.

#### Három helyen látható 1, ahol Hermionénak meg kellett ráznia a pálcáját. Garantált, hogy a kiindulási ponttól a hop-portig csak egyetlen út létezik.

#### Fejezd be a countLuck függvényt az alábbiak szerint, hogy egyetlen stringet adjon vissza: "Impressed", ha Ron tippje helyes, különben "Oops!".
#### Ebben a feladatban az elején megpróbáltam a logikus irányba indulni, vagyis felfelé növelni az értékeket, a tömb legmagasabb értékéhez igazítva, de ezzel nem futott le, így fordított irányba indultam ki, vagyis, hogy a legkevesebb csokival rendelkező egyén felé kezdem el csökkenteni az értékeket.


#### Itt határozom meg az arr legkisebb értékét: 
    minimum_csoki = min(arr)

#### Ezután megadom, hogy a körök, amik növelik az elemeket, nagyon nagy szám is lehet
    rounds = float('inf')


#### Különböző célértékeket állítok be, amit vizsgáljon meg a kód, kiszámolom mennyi a különbség a célérték és a valós csokik között, ha nagyobb, mint 0, akkor kezdje el vizsgálni, ha 5nél nagyobb a különbség, 5-el ossza el és azt adja hozzá, hogy hány kör kell a kívánt eredményhez, ha kevesebb, mint 5, akkor 2-vel fogja elosztani és ítovább 1-ig, ezzel megkapom, hány kör kell a csokik kiegyenlítéséhez.
     for target in range(minimum_csoki, minimum_csoki - 5, -1):
        operations = 0
        
      
        for csoki in arr:
            diff = csoki - target
                if diff > 0:
                    operations += diff // 5 + (diff % 5) // 2 + (diff% 5) % 2
        
       
        rounds = min(rounds, operations)
        
#### Minden célértéknél megvizsgáljuk, hogy a rounds értéke kevesebb-e az új kör értékével, ha kevesebb, akkor frissül az új értékkel.


    rounds = min(rounds, operations)

#### Végül visszatérek a körök értékével.

    return rounds
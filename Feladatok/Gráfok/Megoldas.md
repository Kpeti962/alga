#### Ha a könyvtár felépítési költsége (c_lib) kisebb vagy egyenlő az úthálózat javítási költségével (c_road), akkor a legolcsóbb megoldás minden városban külön könyvtárat építeni. Ilyenkor n * c_lib az összköltség, hiszen n város esetén minden városba kerül egy könyvtár, és nem építünk utat.

    if c_lib <= c_road:
        return n * c_lib;

#### Itt a városok közötti kapcsolatok egy gráfban kerülnek tárolásra. A graf nevű lista minden eleme egy várost jelöl, és minden városhoz egy lista kapcsolódik, amely azokat a városokat tartalmazza, amelyekkel közvetlen összeköttetése van (melyek elérhetők egy úttal). Az n + 1 elem azért kell, hogy az indexek a városok számozásával (1-től n-ig) összhangban legyenek.

    graf = [[] for _ in range(n + 1)]
    for u, v in cities:
        graf[u].append(v);
        graf[v].append(u);

#### Kezdetnek létrehozzuk a stack listát, amiben még csak a csomopontot rakjuk kezdésnek. A komponens kezdeti mérete nulla, ez tárolja majd az összekapcsolódó városok számát.

    stack = [csomopont]
    component_size = 0;
#### A while loopban addig megyünk, ameddig meg nem látogatunk minden összekötött várost

    while stack:
            current = stack.pop();
            if not latogatott[current]:
                latogatott[current] = True;
                component_size += 1;

#### Ezután végigmegyünk azokon a szomszédos városokon, amik közvetlen úttal kapcsolódnak egymáshoz és ha még nem mentünk arra, akkor hozzáadjuk a stack tömbhöz és visszatérünk az összefüggő városok számával.

    for szomszed in graf[current]:
        if not latogatott[szomszed]:
            stack.append(szomszed);
    return component_size;


#### Létrehozunk egy látogatott városok listát, amiben minden város állapota false, vagyis nem látogatott, a fullKoltség pedig a teljes költség tárolására van.

    latogatott = [False] * (n + 1)
    fullKoltseg = 0;

#### Ha a várost még nem látogattuk meg, azaz egy új komponens része, akkor a következőket hajtjuk végre:
##### Komponens méretének kiszámítása. Meghívjuk a keres függvényt, ami visszaadja, hogy hány várost érhetünk el az aktuális városból a loopban.
    component_size = kereses(city, latogatott);
##### Komponens költségének kiszámítása. Az első városba könyvtár kell, a többi városhoz pedig út, amin majd el tudják érni a könyvtárat.
    omponent_cost = c_lib + (component_size - 1) * c_road;
##### Teljes költség frissítése. Ezt az előbbi összeget hozzáadjuk a fullKoltseg változóhoz.
    fullKoltseg += component_cost;

#### Ezután csak visszatérünk a fullKoltseggel

    return fullKoltseg;

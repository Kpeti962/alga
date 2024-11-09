# Roads and Libraries feladatleírás

## Forrás:
#### https://www.hackerrank.com/challenges/three-month-preparation-kit-torque-and-development/problem
---
#### Határozd meg a minimális költséget, hogy a HackerLand minden állampolgára számára könyvtári hozzáférést biztosíts. Adott egy HackerLand-i városok térképe, ahol minden város számozva van 1-től n-ig. Jelenleg nincs könyvtár és a városok nem csatlakoznak egymáshoz. Kétirányú utakat lehet építeni bármely várospár között a megadott városok közül. Egy állampolgár akkor fér hozzá egy könyvtárhoz, ha:

#### Az ő városában van könyvtár.
#### Úton el tud jutni egy olyan városba, ahol van könyvtár.



## Példa:

#### Az alábbi ábra egy HackerLand térképet mutat, ahol a szaggatott vonalak a lehetséges utakat jelölik:

#### c_road = 2: egy út megépítésének költsége 2.
#### c_lib = 3: egy könyvtár megépítésének költsége 3.
#### cities = [[1, 7], [1, 3], [1, 2], [2, 3], [5, 6], [6, 8]]
#### Építs 5 utat 5 x 2 = 10 költséggel és 2 könyvtárat 6 költséggel. Az 1 > 2 > 3 > 1 ciklusban az egyik elérhető út nem szükséges.

#### Összesen q lekérdezés van, és minden lekérdezés egy térképet tartalmaz a HackerLand városairól és a c_lib valamint c_road értékeit. Minden lekérdezésre meg kell találni a minimális költséget, hogy a könyvtárak minden állampolgár számára elérhetők legyenek.







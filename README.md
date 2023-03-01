Dokumentacja
# Ultimate TicTacToe (en) **_/_** Kółko i krzyżyk na sterydach (pl)
## **Opis**
### Projekt umożliwia rozgrywkę gry w kółko i krzyżyk na sterydach:
* Gracz kontra randomowy komputer
* Gracz kontra Inteligentny komputer


## Dodatkowo:
* program pozwala wybrać kto ma zacząć rozgrywkę (gracz czy komputer)

Link do wikipedii gry -> [UltimateTicTacToe](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)
#

## **Instrukcja**
1. Program nalezy uruchamiać z pliku **game.py**, metoda _play()_ przyjmuje obiekt gry (_UltimateTicTacToe_), obiekt bota (_RandomAI_ lub _HardAI_), oraz opcjonalnie (dodatkowo) do funkcji _play()_ jako ostatni argument
można podać **symbol** gracza który ma zaczynać rozgrywkę:
* **'X'** -> zaczyna gracz
* **'O'** -> zaczyna Bot
#####  _(Domyślnie zaczyna gracz 'X' )_

2. Po uruchomieniu programu program zapyta nas na jakiego bota chcemy grać. Należy wybrać _(wpisująć do konsoli)_ jednego z dwóch podanych rodzaji bota:
* ```'Random'``` lub ```'Hard'```
-> _tryb wybranego bota wyświetli się nad planszą_
##### _wielkosci liter nie mają znaczenia_
#

## **Rozgrywka**
Gra polega na wygraniu 3 plansz w kolumnie, wierszu, lub po ukoście przez jednego gracza.

Na poczatek gracz jest proszony o podanie numeru planszy (od 0 do 8) _numery plansz są oznaczone w tabelce **Board indexing** pod planszą_.
Nastepnie gracz podaje pozycje którą chce zagrać, wpisując w terminal odpowiednio wiersz oraz kolumnę (od 0 do 2). _numery wierszów i kolumn zostały oznaczone na bokach planszy_.
Numer kolejnej planszy na której bedzie prowadzona rozgrywka zależy od wybranej poprzednio pozycji. W przypadku gdy kolejna plansza jest juz skończona gracz bądź komputer ma możliwość wybrania dowolnej planszy.

1. Wygrane plansze zostają odpowiednio oznaczone na dużej planszy oraz w tabelce **Board indexing** symbolem zwycięzcy (**X** lub **O** lub **pustym stringiem** w przypadku remisu)   pod dużą planszą.
2. Po wykonaniu ruchu gracz jest informowany o planszy na której teraz gra.
3. Po wygraniu bądź remisie program się kończy.
#

## **Klasy**
* Field() klasa odpowiadająca za symbol na pozycji na planszy.
* Board() klasa reprezentująca małą plansze. Posiada funkcje umozliwiające rozgrywke na małej planszy
* RandomAI() klasa reprezentująca randomowego bota. Posiada funkcje umozliwwiające komputerowi wylosowanie ruchu.
* HardAI()) klasa reprezentująca inteligentnego bota. Posiada funkcje umozliwwiające komputerowi wybranie najlepszej planszy oraz najlepszego ruchu na danej planszy.
* UltimateTicTacToe() klasa reprezentująca dużą plansze. Umożliwia rozgrywkę na dużej planszy.

###  **Autor:**

_Mateusz Matukiewicz_

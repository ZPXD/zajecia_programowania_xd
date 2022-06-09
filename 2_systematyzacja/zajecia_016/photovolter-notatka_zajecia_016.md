zajęcia #016

sygnatury czasowe:

00:04:13
https://www.youtube.com/watch?v=9cGHg1mlFBk&t=4m13s
„Programowanie jest  – co wam będę opowiadał! – drogą przez błędy” - Łukasz Pintal

00:13:13 - PotężnyBrokuł prezentuje

00:15:25 - omówienie kodu z app.py

00:16:15 - zalecamy pisać nazwy zmiennych małymi literami (duże litery warto rezerwować dla klas)

00:18:25 - omówienie kodu PotężnegoBrokuła

00:20:00 - omówienie liczenia słów

00:21:00 - omówienie drugiej części zadania domowego (sortowanie)

00:22:15 - przykład użycia except-ów

00:24:38 - ręcznie, ale można to zrobić prościej metodą sort()

00:26:00 - potęga metody sort() 

00:27:50 - prezentacja działania metody sort na liście list (liście zagnieżdżonej)

00:37:54 - przywoływanie w print() wielu argumentów - coś co może się przydać - skracanie kodu

00:39:30 - odwoływanie się do wartości po indeksie

00:40:30 - omówienie sort() - argumenty 'reverse' i 'key'

00:41:20 - omówienie funkcji PotężnegoBrokuła, która sortuje argumentem 'key' - tutaj: po indeksie '2' zagnieżdzonej listy

00:45:50 - sprawdzamy argument 'reverse' metody sort()

00:46:50 - upgrade kodu - poprawiamy nazwy

00:47:59 - wyjaśnienie co jest przekazywane do argumentu 'key' - 

00:48:40 - trzeba zauważyć, że funkcja 'my_func' ma argument, a w 'key' jest wywoływana BEZ wskazania argumentu

00:49:49 - warto nazywać funkcje tak, by było wiadomo o co chodzi

00:50:07 - zmieniamy nazwę funkcji 'my_func' na 'pick_3_element'

00:50:40 - rozwiewamy wątpliwości związane z działaniem funkcji 'pick_3_element'

00:55:20 - zmieniamy wartości przykładowej listy zagnieżdżonej, by działanie metody sort() po 'key' było bardziej czytelne

00:59:30 - sort() nie jest takie banalne, na jakie wygląda :)

00:59:54 - wytłumaczenie sort() w inny sposób

01:00:55 - pytanie o argument funkcji PotężnegoBrokuła o nazwie 'pick_3_element'

01:03:00 - wywołujemy 'pick_3_element' poza argumentem 'key' metody sort() - tutaj wymagane jest wpisanie argumentu bezpośrednio dla funkcji 'pick_3_element'

01:03:53 - analizujemy sposób zachowania funkcji, gdy podamy inną liczbę argumentów, niż przewiduje jej definicja

01:05:15 - a czy w takim razie, gdy podamy taką samą liczbę argumentów, jaką przewiduje definicja naszej funkcji, to czy MUSIMY wykorzystać w tej funkcji wszystkie te elementy? Odpowiedź: nie.

01:08:30 - podsumowanie liczby argumentów funkcji i konieczności korzystania z nich wszystkich

01:10:35 - podsumowanie sposobu w jaki metoda sort() sortuje po 'key' listę zagnieżdżoną

01:13:01 - pytanie o linię 11: 'sd = pick_3_element(content_list)' (Przypisek widza: odpowiedź nie pada od razu w filmie, ale chodzi o to, że metoda (sort) z linii 9. sortując ZMIENIA ORYGINALNĄ zawartość sortowanej listy - działa na dokładnie tej liście zmieniając zawartość obszaru pamięci RAM przechowującego dokładnie tę listę; inaczej zachowuje się funkcja sorted() )

01:18:40 - zaprezentowanie, że metoda sort zmienia zawartość listy

01:19:20 - sort() najczęściej używany jest bez argumentów, ale argumenty uwidaczniają jego potęgę

01:19:50 - sort() bez argumentu 'key' sortuje po indeksie '0'

01:20:50 - sort() z argumentem 'key', ale będącym int-em, a nie listą taką jak np. 'pick_3_element' - to dlatego dla 'key' stosuje się funkcje (np. lambda)

01:22:20 - prezentacja, że argument 'key' wywołujący funkcję 'pick_3_element' nie przekazuje funkcji 'pick_3_element' całej listy zagnieżdżonej ('content_list') , a jedynie jej elementy (będące w tym przypadku  również listami)

01:24:10 - czy metodę 'sort()' można zastosować na stringu, zamiast na liście?

01:26:50 - do sortowania stringu można zastosować funkcję 'sorted()' - np. sorted('bca') - ona zadziała 

01:29:00 - pokazujemy jak sort() działa na liście, której elementami są stringi.

01:31:40 - omawiamy szybko metodę append() 

01:34:20 - dzisiaj jest środa - zatem zadanie domowe: przeczytać klocek nr 008

01:44:00  - podczas nauki warto spojrzeć na to samo zagadnienie z innej perspektywy

01:47:00 - klocka nr 008 nie musimy uczyć się na pamięć, ale powinniśmy zrozumieć na tyle, żeby móc wytłumaczyć innym osobom ('nauczycielska' metoda nauki) - czyli w praktyce trzeba wracać do wcześniej przeczytanych i zrozumianych fragmentów

01:49:58 - odezwa do Orłów :)

01:50:40 - zapowiedź pierwszego wyzwania dla Orłów: Arena

01:55:30 - zakończenie

Notatka:

1. Angielski - crash course

2. Caritas Serwerowy

3. Wsparcie dla dzieci


-------------------

Listy

w metodzie sort() można podać 2 argumenty:
1. reverse
2. key
key nie może być wartością typu np. int. - jeżeli chcemy sortować listy dwuelementowe pod drugim elemencie (czyli po indeksie równym 1), to nie można podać key = 1, tylko trzeba tam dostarczyć drugi element każdej listy (można do tego wykorzystać lambda).

Innymi słowy, aby posortować taką listę: 
	content_list = [[1,3,2],[4,6,5],[7,9,8]]
po indeksie równym '1', to trzeba zrobić takie coś:
	content_list = [[1,3,2],[4,6,5],[7,9,8]]
	def pick_1_element(list_a):
		element = list_a[1]
		return element
	content_list.sort(reverse=False, key=pick_1_element# bez argumentu dla funkcji!, bo argumentem jest sama 'content_list' na której stosujemy metodę 'sort()'

a na stringach można zrobić 'sorted()' zamiast 'sort()' 
	print(content_list)

## Shuffle the string
#### Shuffle

__https://stackoverflow.com/questions/49084904/r-markdown-bullet-list-with-multiple-levels__

#### Shuffle list

```
import random
l = list(s)
random.shuffle(l)
result = ''.join(l)
```

#### Shuffle string


Shuffle string

```
import random
s="abcdef123"
''.join(random.sample(s,len(s)))
'1f2bde3ac'


```

- Python Provides the various solutions to shuffle the string:

**1. External library: python-string-utils**

- first install the python-string-utils library:

``` pip install python_string_utils ```
- use `string_utils.shuffle()` function to shuffle string
- please use the below snippet for it

Code Snippet
```
import string_utils
print string_utils.shuffle("random_string")
```
Output:
```
drorntmi_asng
```
**2. Builtins Method: random.shuffle**

Please find the code below to shuffle the string. The code will take the string and convert that string to list. Then shuffle the string contents and will print the string.
```
import random
str_var = list("shuffle_this_string")
random.shuffle(str_var)
print ''.join(str_var)
```
Output:
```
t_suesnhgslfhitrfi_
```
**3. External Library: Numpy**
```
import numpy
str_var = list("shuffle_this_string")
numpy.random.shuffle(str_var)
print ''.join(str_var)
```
Output:

```
nfehirgsu_slftt_his
```



## Co mapujemy?
### Mapowanie funkcji

__https://www.freecodecamp.org/news/python-map-function-how-to-map-a-list-in-python-3-0-with-example-code/__

Mapujemy funkcje na obiekty iterowalne:
- lista (list)
- słownik (dictionary)
- tupla (tuple))

# Design a URL shortener

One Simple Solution could be Hashing. Use a hash function to convert long string to short string. In hashing, that may be collisions.

A Better Solution is to use the integer id stored in database and convert the integer to character string that is at most 6 characters long. This problem can basically seen as a base conversion problem where we have a 10 digit input number and we want to convert it into a 6 character long string.

Below is one important observation about possible characters in URL.

A URL character can be one of the following
1) A lower case alphabet [‘a’ to ‘z’], total 26 characters
2) An upper case alphabet [‘A’ to ‘Z’], total 26 characters
3) A digit [‘0′ to ‘9’], total 10 characters

There are total 26 + 26 + 10 = 62 possible characters.

[Bijective Function](https://en.wikipedia.org/wiki/Bijection) is needed, which means This is necessary so that you can find a inverse function `g('abc') = 123` for your `f(123) = 'abc'` function. This means:

* There must be no x1, x2 (with x1 ≠ x2) that will make f(x1) = f(x2),
* and for every y you must be able to find an x so that f(x) = y.
  
## Code

```python
# ShortURL (https://github.com/delight-im/ShortURL)
# Copyright (c) delight.im (https://www.delight.im/)
# Licensed under the MIT License (https://opensource.org/licenses/MIT)

class ShortURL:
	"""
	ShortURL: Bijective conversion between natural numbers (IDs) and short strings
	ShortURL.encode() takes an ID and turns it into a short string
	ShortURL.decode() takes a short string and turns it into an ID
	Features:
	+ large alphabet (51 chars) and thus very short resulting strings
	+ proof against offensive words (removed 'a', 'e', 'i', 'o' and 'u')
	+ unambiguous (removed 'I', 'l', '1', 'O' and '0')
	Example output:
	123456789 <=> pgK8p
	"""

	_alphabet = '23456789bcdfghjkmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ-_'
	_base = len(_alphabet)

	def encode(self, number):
		string = ''
		while(number > 0):
			string = self._alphabet[number % self._base] + string
			number //= self._base
		return string

	def decode(self, string):
		number = 0
		for char in string:
			number = number * self._base + self._alphabet.index(char)
		return number
```


## Reference

[How to design a tiny URL or URL shortener?](https://www.geeksforgeeks.org/how-to-design-a-tiny-url-or-url-shortener/)

[shorturl.py](https://github.com/delight-im/ShortURL/blob/master/Python/shorturl.py)

[How to code a URL shortener?](https://stackoverflow.com/questions/742013/how-to-code-a-url-shortener)
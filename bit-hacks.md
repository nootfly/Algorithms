# Bit Hacks

## Check if an given integer is even or odd

```python
20 & 1 = 0
21 & 1 = 1
```

## X ^ X = 0

```python
12 ^ 12 = 0
```

## Add 1 to a given integer

```python
-20 = ~20 + 1
-~20 = 20 + 1
```

## Swap two numbers without using any third variable

```python
x, y = 3, 4
x = x ^ y
y = x ^ y
x = x ^ y
```

## Turn off/on k’th bit in a number

```python
# turn off: n & (~(1 << (k - 1)))
20 & ~(1 << (3 - 1)) = 16
# turn on: n | (1 << (k - 1))
16 | (1 << (3 - 1)) = 20
```

## Convert uppercase character to lowercase and Convert lowercase character to uppercase

```python
chr(ord('A') | ord(' ')) = 'a'
chr(ord('A') ^ ord(' ')) = 'a'

chr(ord('a') & ord('_')) = 'A'
chr(ord('a') ^ ord(' ')) = 'A'
```

## Find letter’s position in alphabet, and note that the case of the letter is irrelevant

```python
ord('A') & 31 = 1
ord('c') & 31 = 3
```

## Reference

[Bit Hacks – Part 1](http://www.techiedelight.com/bit-hacks-part-1-basic/)
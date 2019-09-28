## gprint
![badge](https://img.shields.io/badge/Python-3.6-brightgreen?style=flat-square) ![badge](https://img.shields.io/badge/version-1.1.0-blue?style=flat-square)

gprint -> grid print

### Example 1
```python
g1 = "abc\nde\nf"
g2 = "Here is a 2nd grid\n!!!!!\n!!!!!!"
g3 = "1\n2\n3\n4\n5"
gprint(g1, g2, g3)
```
### Output 1
```        
abc   Here is a 2nd grid   1
de    !!!!!                2
f     !!!!!!               3
                           4
                           5
```
When you use Kanji, Hiragana or Katakana, pass `True` to `enable_east_asian_width` (See a demo.py).
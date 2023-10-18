[![PyPI version](https://badge.fury.io/py/pycccedict.svg)](https://badge.fury.io/py/pycccedict)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

# CC-CEDICT in Python
To use the [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict) Chinese to English dictionary in Python.

## Installation
```bash
pip install pycccedict
```

## Example
1. Get an entry
```python
from pycccedict.cccedict import CcCedict

cccedict = CcCedict()
cccedict.get_entry('猫')
```
```json
{
    "traditional": "貓",
    "simplified": "猫",
    "pinyin": "mao1",
    "definitions": [
        "cat",
        "CL:隻|只[zhi1]",
        "(dialect) to hide oneself",
        "(coll.) modem"
    ]
}
```

## API
### get_entry
```python
>>> cccedict.get_entry('猫')
{
    "traditional": "貓",
    "simplified": "猫",
    "pinyin": "mao1",
    "definitions": [
        "cat",
        "CL:隻|只[zhi1]",
        "(dialect) to hide oneself",
        "(coll.) modem"
    ]
}
```
### get_traditional
```python
>>> cccedict.get_traditional('猫')
'貓'
```
### get_simplified
```python
>>> cccedict.get_simplified('貓')
'猫'
```
### get_pinyin
```python
>>> cccedict.get_pinyin('猫')
'mao1'
```
### get_definitions
```python
>>> cccedict.get_definitions('猫')
['cat', 'CL:隻|只[zhi1]', '(dialect) to hide oneself', '(coll.) modem']
```

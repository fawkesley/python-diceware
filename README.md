# Generate Diceware Passphrase

**NOT READY FOR PRIMETIME**

Generate a random, memorable pass-phrase, for example `kirby bang basin flux chill memo`

Inspired by the excellent [http://diceware.com](Diceware method).

**WARNING** Using a computer to generate your passphrases is **not as secure**
as rolling physical die with a paper reference of the diceware list.

Depending on your appetite for security vs convenience, you should consider
actually rolling die, or at the **very least** read 
[this section on levels of security](http://world.std.com/~reinhold/dicewarefaq.html#howlong)
on the diceware website. It's quite an interesting read.

If you are looking for a convenient way to generate passphrases, you're
confident that this code isn't dodgy (you can look) and that your computer is
not being spied on, this could be for you :)

## Example Usage

As a Python module:

```python
from diceware import generate_passphrase
print(generate_passphrase())
```

As a command-line tool:

```
> diceware
```

## Installation

```
> pip install diceware
```

## Technical stuff

This is implemented against the advice of, but in accordance with the [suggestions
on the Diceware website](http://world.std.com/~reinhold/dicewarefaq.html#computer),
namely:

- [ ] uses `os.urandom()` for entropy, which is preferable to Python's
[(less secure random module)](https://docs.python.org/2/library/random.html).
- uses the 2^13 long wordlist `diceware8k.txt` of mostly English words

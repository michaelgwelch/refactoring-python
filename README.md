# Refactoring 2nd Edition in Python

This repository contains a python version of the theater project
as described in chapter 1 of Martin Fowler's Refactoring 2nd Edition book.

As the author states (*emphasis mine*):

> Outside of the example sections, I'm not making any assumptions about the language. I expect the reader to absorb my general comments and apply them to the language they are using. *Indeed, I expect readers to take the JavaScript examples and adapt them to their language.*

## List of Commits

| Page |  Loc | Commit                     | Link(s) to file(s)    | Diff(s)                    |
| ---: | ---: | -------------------------- | --------------------- | -------------------------- |
|    2 |  441 | [Starting Point][sp-c]     | [statement.py][sp-p]  |                            |
|    7 |  547 | [Extract amountFor][eaf-c] | [statement.py][eaf-p] | [statement.py diff][eaf-d] |
|    9 |  595 | [Rename thisAmount][rta-c] | [statement.py][rta-p] | [statement.py diff][rta-d] |
|   10 |  607 | [Rename perf][rp-c]        | [statement.py][rp-p]  | [statement.py diff][rp-d]  |
|   11 |  634 | [Extract playFor][epf-c]   | [statement.py][epf-p] | [statement.py diff][epf-d] |
|   11 |  651 | [Inline play var][ipv-c]   | [statement.py][ipv-p] | [statement.py diff][ipv-d] |


Comments

1. Locations and Page numbers point to the location/page where the code for a specific refactoring has it's first line.
2. **Starting Point** The only slightly significant changes from JavaScript are
   1. Complete lack of variable declarations (other than assigning them initial values)
   2. No local variable to hold a format function. This could have been copied by creating a lambda. Instead, this program just calls the boost format_currency functionœ in multiple locations leading to an "Extract Method" refactoring later on.
   3. Python apparently has no switch statement. A dictionary of lambdas could have been used, but it seemed that for just 2 (or 3) cases if statement would suffice.œ
3. **Extract amountFor** The author tends to add the nested functions at the end of the statement method. Python doesn't seem to allow this without some "tricks". Instead I just added them to the beginning of the statement method.

[sp-c]: https://github.com/michaelgwelch/refactoring-python/tree/8e811d1636b42521608614db08f6a25d1fba4dfe
[sp-p]: https://github.com/michaelgwelch/refactoring-python/blob/8e811d1636b42521608614db08f6a25d1fba4dfe/statement.py
[eaf-c]: https://github.com/michaelgwelch/refactoring-python/tree/888660fd602b3e88404d9c4957a20b6cb572d92c
[eaf-p]: https://github.com/michaelgwelch/refactoring-python/blob/888660fd602b3e88404d9c4957a20b6cb572d92c/statement.py
[eaf-d]: https://github.com/michaelgwelch/refactoring-python/commit/888660fd602b3e88404d9c4957a20b6cb572d92c#diff-80171273663b5e689d7867585fc1d028
[rta-c]: https://github.com/michaelgwelch/refactoring-python/tree/5007c9f261fb9e1249a6bbe8cfda133c6761c0ec
[rta-p]: https://github.com/michaelgwelch/refactoring-python/blob/5007c9f261fb9e1249a6bbe8cfda133c6761c0ec/statement.py
[rta-d]: https://github.com/michaelgwelch/refactoring-python/commit/5007c9f261fb9e1249a6bbe8cfda133c6761c0ec#diff-80171273663b5e689d7867585fc1d028
[rp-c]: https://github.com/michaelgwelch/refactoring-python/tree/b3c1aea1a4c3244221302d6afa76ba77385ed27b
[rp-p]: https://github.com/michaelgwelch/refactoring-python/blob/b3c1aea1a4c3244221302d6afa76ba77385ed27b/statement.py
[rp-d]: https://github.com/michaelgwelch/refactoring-python/commit/b3c1aea1a4c3244221302d6afa76ba77385ed27b#diff-80171273663b5e689d7867585fc1d028
[epf-c]: https://github.com/michaelgwelch/refactoring-python/tree/f1fa6ed4fdbe7f37afe1105d1351400d7c9265fe
[epf-p]: https://github.com/michaelgwelch/refactoring-python/blob/f1fa6ed4fdbe7f37afe1105d1351400d7c9265fe/statement.py
[epf-d]: https://github.com/michaelgwelch/refactoring-python/commit/f1fa6ed4fdbe7f37afe1105d1351400d7c9265fe#diff-80171273663b5e689d7867585fc1d028
[ipv-c]: https://github.com/michaelgwelch/refactoring-python/tree/9d62089ccdf495287e12c95bec44a3af3c984c04
[ipv-p]: https://github.com/michaelgwelch/refactoring-python/blob/9d62089ccdf495287e12c95bec44a3af3c984c04/statement.py
[ipv-d]: https://github.com/michaelgwelch/refactoring-python/commit/9d62089ccdf495287e12c95bec44a3af3c984c04#diff-80171273663b5e689d7867585fc1d028
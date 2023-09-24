# Time Complexity Analysis for "Unscramble Computer Science Problems"
## Task0
This takes runs in __O(1)__, as the access time for items in a list.

## Task1
This task will take linear time i.e., O(n) s the access time for 2 loops

## Task2
- `O(n)`: for the for loop
- `O(n)`: for max items in a list
- ***Total time complexity*** of this code block is `O(n)`
## Task3:

PartA:

- `O(n+n)` => `O(2n)` => `O(n)`: for 2 lists
- `O(1)`: for a set.
- `O(n)`: it is obvious that for-loop is linear time.
- `O(n*log(n))`: sorting a list

***Total time complexity*** of this code block is `O(n + 1 + n*1 + nlog(n))` =>  `O(2n+nlogn)` =>  `O(nlog(n))`

PartB:

- `O(n)`: for list comprehension
- `O(1)`: for finding percentage

***Total time complexity:*** `(O(n+1))` => `O(n)`

## Task4:

- the four list comprehensions take `O(n)` complexity each. `O(4n)` => `O(n)`
- sorting takes `O(nlogn)`
- for loop takes `O(n)` time complexity 
- for loop printing sorted list

***Total time complexity:*** `O(n + n + nlogn + n)` => `O(3n + nlogn)` => `O(nlogn)`



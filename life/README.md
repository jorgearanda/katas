# Game of Life Kata

Given textual input to a `life()` function as follows:

```
....
..*.
.**.
....
```

...provide an output using Game of Life rules, as follows:

```
....
.**.
.**.
....
```

The rules are:

* A live cell (one marked with a star) with under two live neighbours (out of the eight possible cell neighbours) dies in the output, due to underpopulation
* A live cell with more than two live neighbours dies in the output, due to overpopulation
* Live cells that do not die for either of the previous reasons (so those with two or three neighbours) remain in the output
* A dead cell with exactly three live neighbours becomes a live cell
* (Variation) The grid is not infinite. Hypothetical cells beyond the border of the board are dead

Assume the input is a list of string rows. The output should also be a list of string rows.

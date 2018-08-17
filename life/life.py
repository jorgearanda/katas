def life(input):
    output = []
    for row_idx, row in enumerate(input):
        outline = ''
        for col_idx in range(len(row)):
            neighbours = _neighbours(input, row_idx, col_idx)
            if _is_live(input, row_idx, col_idx):
                if _too_sparse(neighbours) or _too_crowded(neighbours):
                    outline += '.'
                else:
                    outline += '*'
            else:
                if _right_for_life(neighbours):
                    outline += '*'
                else:
                    outline += '.'

        output.append(outline)

    return output


def _neighbours(input, row_idx, col_idx):
    count = 0
    neighbours = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    for i, j in neighbours:
        if _are_valid_coordinates(input, row_idx + i, col_idx + j) and \
                _is_live(input, row_idx + i, col_idx + j):
            count += 1

    return count


def _are_valid_coordinates(grid, row, col):
    return (row >= 0 and row < len(grid) and col >= 0 and col < len(grid[row]))


def _is_live(grid, row, col):
    return grid[row][col] == '*'


def _too_sparse(count):
    return count < 2


def _too_crowded(count):
    return count > 3


def _right_for_life(count):
    return count == 3


# First pass. I think this will benefit from a class-based approach,
# which I should implement the next time around.

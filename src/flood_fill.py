"""
733. Flood Fill

https://leetcode.com/problems/flood-fill

NOTES
  * Use breadth-first search.

This problem is very straight-forward if you use breadth-first search. Simply
add adjacent pixels that share the same color as the starting pixel to the
queue and run the algorithm.

You can also solve this problem using a depth-first search, since we want to
visit every pixel, however BFS is slightly more intuitive here and replicates
how flood fill would actually work.

There are two programming techniques to be aware of when working with matrices:
  1. Getting m (number of rows) and n (number of columns)
  2. Getting adjacent and diagonal coordinates (with boundary check)

Getting m (number of rows) and n (number of columns)
----------------------------------------------------

    m, n = len(matrix), len(matrix[0])

Getting adjacent and diagonal coordinates (with boundary check)
---------------------------------------------------------------

    # Up, Right, Down, Left
    adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Up-Right, Down-Right, Down-Left, Up-Left
    diagonal = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

    # Loop over all neighboring elements (adjacent + diagonal)
    for dx, dy in adjacent + diagonal:
        i, j = curr[0] + dx, curr[1] + dy
        if (0 <= i < m and 0 <= j < n):
            ...

This solution has O(n) time complexity and O(n) space complexity, since, in the
worst case, we will need to visit every pixel in the image.

Example:

   j →
  i
  ↓  1 1 1     2 2 2
     1 1 0  →  2 2 0
     1 0 1     2 0 1
"""

from collections import deque


class Solution:
    """
    Uses breadth-first search.
    """

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # If the starting pixel is already our target color, return `image`,
        # since no pixels will be modified.
        if image[sr][sc] == color:
            return image

        # Get m (number of rows) and n (number of columns)
        m, n = len(image), len(image[0])

        # Create queue, enqueue starting pixel.
        # NOTE: In a typical BFS, we create a set of visited elements. Since
        # modifying the color of a pixel is essentially marking it as visited,
        # the "visited" set is implicit.
        queue = deque([(sr, sc)])  # image[sr][sc]

        # Preserve the original color and update the starting pixel to the new
        # color.
        original_color = image[sr][sc]
        image[sr][sc] = color

        # Up, Right, Down, Left
        adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Run the BFS algorithm:
        #   1. Remove (deque) first element.
        #   2. For each child, if the child has not already been visited, mark
        #      it as visited and add it to the queue (enqueue).
        while queue:
            curr: tuple[int, int] = queue.popleft()  # (i, j)

            # Get adjacent pixels (taking into account the image boundary) that
            # share the same color as the starting pixel.
            for dx, dy in adjacent:
                i, j = curr[0] + dx, curr[1] + dy
                if 0 <= i < m and 0 <= j < n and image[i][j] == original_color:
                    image[i][j] = color
                    queue.append((i, j))

        return image


class SolutionDFS:
    """
    Uses depth-first search.
    """

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        # If the starting pixel is already our target color, return `image`,
        # since no pixels will be modified.
        if image[sr][sc] == color:
            return image

        # Get m (number of rows) and n (number of columns)
        m, n = len(image), len(image[0])

        # Create stack, push starting pixel.
        # NOTE: In a typical DFS, we create a set of visited elements. Since
        # modifying the color of a pixel is essentially marking it as visited,
        # the "visited" set is implicit.
        stack = deque([(sr, sc)])  # image[sr][sc]

        # Preserve the original color.
        # NOTE: When using a stack, the element is marked after it is removed.
        original_color = image[sr][sc]

        # Up, Right, Down, Left
        adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Run the DFS algorithm:
        #   1. Remove (pop) last element.
        #   2. If the element has not already been visited, mark it as visited
        #      and add (push) its children onto the stack.
        while stack:
            curr: tuple[int, int] = stack.pop()  # (i, j)

            # NOTE: When using a stack, the element is marked as visited when
            # it is removed from the stack. Continuing if the element has
            # already been visited (i.e., its color is equal to the target
            # color) ensures we do not visit a node more than once.
            if image[curr[0]][curr[1]] == color:
                continue

            image[curr[0]][curr[1]] = color

            # Get adjacent pixels (taking into account the image boundary) that
            # share the same color as the starting pixel.
            for dx, dy in adjacent:
                i, j = curr[0] + dx, curr[1] + dy
                if 0 <= i < m and 0 <= j < n and image[i][j] == original_color:
                    stack.append((i, j))

        return image

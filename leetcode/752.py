"""

Examples

Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> 1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

ERROR
- traté de buscar un algoritmo para hacerlo (backtracking, programacion dinamica)
- faltó dibujar la solucion o plantearla en mi mente
    - LUEGO, empezar a codear en base a ello

SOLUCION
- avanzar en todas las direcciones cada vez que se da un paso hacia delante
- contabilizar los pasos y devolver el contador apenas se llegue a encontrar el target
- estructura inicial
    - 1 cola fifo
    - 1 lista de deadends
    - 1 contador

Complexity: O(n^2) -> la solucion es correcta solo que se demora mucho - Time limit exceeded

"""

from typing import List


class Solution:

    def get_neighbors(self, curr: str):
        neighbors = []
        for move in [1, -1]:
            for i in range(4):
                value = curr[i]
                new_value = str((int(value) + move) % 10)
                new_start = curr[:i] + new_value + curr[i + 1:]
                neighbors.append(new_start)
        return neighbors

    def openLock(self, deadends: List[str], target: str) -> int:
        base = "0000"
        if base in deadends:
            return -1
        queue = [base]
        steps = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                curr = queue.pop(0)
                # It's the response
                if curr == target:
                    return steps
                for neighbor in self.better_get_neighbors(curr):
                    # it's not an already taken or forbidden path
                    if neighbor not in deadends:
                        # Visited
                        deadends.append(neighbor)
                        # To explore
                        queue.append(neighbor)
            steps += 1
        return -1


if __name__ == '__main__':
    s = Solution()
    r1 = s.openLock(["0201", "0101", "0102", "1212", "2002"], "0202")
    print(r1)
    r2 = s.openLock(["8888"], "0009")
    print(r2)
    r3 = s.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888")
    print(r3)

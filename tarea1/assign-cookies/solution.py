from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0  # niño actual (el menos exigente que aún no tiene galleta)
        for galleta in s:  # galletas de menor a mayor
            if i < len(g) and galleta >= g[i]:
                i += 1  # la galleta más pequeña que sirve se la damos a este niño
            # si no alcanza, la galleta se descarta y se prueba la siguiente
        return i


if __name__ == "__main__":
    sol = Solution()
    assert sol.findContentChildren([1, 2, 3], [1, 1]) == 1
    assert sol.findContentChildren([1, 2], [1, 2, 3]) == 2
    assert sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 2
    assert sol.findContentChildren([], [1]) == 0
    print("ok")

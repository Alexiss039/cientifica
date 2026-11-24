from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cinco = 0
        diez = 0
        for b in bills:
            if b == 5:
                cinco += 1
            elif b == 10:
                if cinco == 0:
                    return False
                cinco -= 1
                diez += 1
            else:  # b == 20
                # Greedy: gastar primero el billete de 10 (menos útil que los de 5)
                if diez > 0 and cinco > 0:
                    diez -= 1
                    cinco -= 1
                elif cinco >= 3:
                    cinco -= 3
                else:
                    return False
        return True


if __name__ == "__main__":
    s = Solution()
    assert s.lemonadeChange([5, 5, 5, 10, 20]) is True
    assert s.lemonadeChange([5, 5, 10, 10, 20]) is False
    assert s.lemonadeChange([10]) is False
    assert s.lemonadeChange([5, 5, 5, 5, 20, 20, 5, 5, 20, 5]) is False
    print("ok")

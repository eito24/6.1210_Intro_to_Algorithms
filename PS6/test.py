import unittest
from count_paths import count_paths


def check(test, verbose=True):
    F, staff_sol = test
    student_sol = count_paths(F)

    if staff_sol==student_sol:
        return True
    
    if verbose:
        print(
            f"Your solution output {student_sol} optimal paths but there are {staff_sol} optimal paths"
        )
    return False


tests = (
    (
        [
            ['x', 'm'],
            ['m', 'x'],
        ],
        2,
    ),
    (
        [
            ['x', 'x', 'x'],
            ['x', 'm', 'x'],
            ['m', 'm', 'x'],
        ],
        3,
    ),
    (
        [
            ['x', 'x', 'm', 'x'],
            ['x', 'x', 't', 'm'],
            ['x', 'x', 'x', 't'],
            ['x', 'x', 'x', 'x'],
        ],
        7,
    ),
    (
        [
            ['x', 'x', 't', 'x', 'm'],
            ['x', 'x', 'x', 'x', 'x'],
            ['m', 'm', 'x', 'x', 'm'],
            ['x', 'x', 't', 'm', 't'],
            ['x', 't', 'x', 'm', 'x'],
        ],
        1,
    ),
    (
        [
            ['x', 'm', 'x', 'x', 't', 'm', 'm'],
            ['x', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['x', 'm', 'x', 't', 'm', 't', 't'],
            ['m', 'x', 'x', 'x', 'x', 'x', 'm'],
            ['m', 't', 'm', 'm', 't', 'x', 'x'],
            ['m', 'x', 'm', 'x', 'x', 'x', 'm'],
            ['x', 'x', 'x', 'm', 't', 'm', 'x'],
        ],
        10,
    ),
)


class TestCases(unittest.TestCase):
    def test_01(self):
        self.assertTrue(check(tests[0]))

    def test_02(self):
        self.assertTrue(check(tests[1]))

    def test_03(self):
        self.assertTrue(check(tests[2]))

    def test_04(self):
        self.assertTrue(check(tests[3]))

    def test_05(self):
        self.assertTrue(check(tests[4]))
    

if __name__ == "__main__":
    res = unittest.main(verbosity=3, exit=False)
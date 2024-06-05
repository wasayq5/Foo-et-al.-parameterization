import unittest
from foo_param.foo import FooParameterization

class TestFooParameterization(unittest.TestCase):
    def test_volume(self):
        foo_param = FooParameterization()
        self.assertAlmostEqual(foo_param.volume(1), 4.1887902047863905)
        self.assertAlmostEqual(foo_param.volume(0), 0)
        self.assertAlmostEqual(foo_param.volume(2), 33.510321638291124)

if __name__ == '__main__':
    unittest.main()

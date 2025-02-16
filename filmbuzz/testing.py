import unittest

class TestMathOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(1 + 1, 2)
        self.assertEqual(-1 + 1, 0)
        self.assertEqual(-1 + -1, -2)

    def test_subtraction(self):
        self.assertEqual(2 - 1, 1)
        self.assertEqual(-1 - 1, -2)
        self.assertEqual(-1 - -1, 0)

    def test_multiplication(self):
        self.assertEqual(2 * 2, 4)
        self.assertEqual(-1 * 1, -1)
        self.assertEqual(-1 * -1, 1)

    def test_division(self):
        self.assertEqual(4 / 2, 2)
        self.assertEqual(-1 / 1, -1)
        self.assertEqual(-1 / -1, 1)
        with self.assertRaises(ZeroDivisionError):
            _ = 1 / 0

    def test_modulus(self):
        self.assertEqual(10 % 3, 1)
        self.assertEqual(10 % 2, 0)
        self.assertEqual(-10 % 3, 2)
        with self.assertRaises(ZeroDivisionError):
            _ = 1 % 0

    def test_exponentiation(self):
        self.assertEqual(2 ** 3, 8)
        self.assertEqual(3 ** 2, 9)
        self.assertEqual(-2 ** 2, -4)

    def test_floor_division(self):
        self.assertEqual(10 // 3, 3)
        self.assertEqual(10 // 2, 5)
        self.assertEqual(-10 // 3, -4)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def test_lower(self):
        self.assertEqual('FOO'.lower(), 'foo')

    def test_islower(self):
        self.assertTrue('foo'.islower())
        self.assertFalse('Foo'.islower())

    def test_startswith(self):
        self.assertTrue('hello world'.startswith('hello'))
        self.assertFalse('hello world'.startswith('world'))

    def test_endswith(self):
        self.assertTrue('hello world'.endswith('world'))
        self.assertFalse('hello world'.endswith('hello'))

    def test_find(self):
        self.assertEqual('hello world'.find('world'), 6)
        self.assertEqual('hello world'.find('python'), -1)

    def test_replace(self):
        self.assertEqual('hello world'.replace('world', 'python'), 'hello python')
        self.assertEqual('hello world'.replace('java', 'python'), 'hello world')

class TestListMethods(unittest.TestCase):

    def test_append(self):
        lst = []
        lst.append(1)
        self.assertEqual(lst, [1])

    def test_extend(self):
        lst = [1]
        lst.extend([2, 3])
        self.assertEqual(lst, [1, 2, 3])

    def test_insert(self):
        lst = [1, 3]
        lst.insert(1, 2)
        self.assertEqual(lst, [1, 2, 3])

    def test_remove(self):
        lst = [1, 2, 3]
        lst.remove(2)
        self.assertEqual(lst, [1, 3])
        with self.assertRaises(ValueError):
            lst.remove(4)

    def test_pop(self):
        lst = [1, 2, 3]
        self.assertEqual(lst.pop(), 3)
        self.assertEqual(lst, [1, 2])
        self.assertEqual(lst.pop(0), 1)
        self.assertEqual(lst, [2])

    def test_clear(self):
        lst = [1, 2, 3]
        lst.clear()
        self.assertEqual(lst, [])

    def test_index(self):
        lst = [1, 2, 3]
        self.assertEqual(lst.index(2), 1)
        with self.assertRaises(ValueError):
            lst.index(4)

    def test_count(self):
        lst = [1, 2, 2, 3]
        self.assertEqual(lst.count(2), 2)
        self.assertEqual(lst.count(4), 0)

    def test_sort(self):
        lst = [3, 1, 2]
        lst.sort()
        self.assertEqual(lst, [1, 2, 3])

    def test_reverse(self):
        lst = [1, 2, 3]
        lst.reverse()
        self.assertEqual(lst, [3, 2, 1])

    def test_copy(self):
        lst = [1, 2, 3]
        lst_copy = lst.copy()
        self.assertEqual(lst_copy, lst)
        self.assertIsNot(lst_copy, lst)

    def test_len(self):
        lst = [1, 2, 3]
        self.assertEqual(len(lst), 3)
        self.assertEqual(len([]), 0)

    def test_max(self):
        lst = [1, 2, 3]
        self.assertEqual(max(lst), 3)
        self.assertEqual(max([-1, -2, -3]), -1)

    def test_min(self):
        lst = [1, 2, 3]
        self.assertEqual(min(lst), 1)
        self.assertEqual(min([-1, -2, -3]), -3)

    def test_sum(self):
        lst = [1, 2, 3]
        self.assertEqual(sum(lst), 6)
        self.assertEqual(sum([]), 0)

    def test_any(self):
        lst = [0, 1, 2]
        self.assertTrue(any(lst))
        self.assertFalse(any([0, 0, 0]))

    def test_all(self):
        lst = [1, 2, 3]
        self.assertTrue(all(lst))
        self.assertFalse(all([0, 1, 2]))

    def test_sorted(self):
        lst = [3, 1, 2]
        self.assertEqual(sorted(lst), [1, 2, 3])
        self.assertEqual(sorted(lst, reverse=True), [3, 2, 1])

    def test_enumerate(self):
        lst = ['a', 'b', 'c']
        self.assertEqual(list(enumerate(lst)), [(0, 'a'), (1, 'b'), (2, 'c')])

    def test_zip(self):
        lst1 = [1, 2, 3]
        lst2 = ['a', 'b', 'c']
        self.assertEqual(list(zip(lst1, lst2)), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_map(self):
        lst = [1, 2, 3]
        self.assertEqual(list(map(lambda x: x * 2, lst)), [2, 4, 6])

    def test_filter(self):
        lst = [1, 2, 3, 4]
        self.assertEqual(list(filter(lambda x: x % 2 == 0, lst)), [2, 4])

    def test_reduce(self):
        from functools import reduce
        lst = [1, 2, 3, 4]
        self.assertEqual(reduce(lambda x, y: x + y, lst), 10)

if __name__ == '__main__':
    unittest.main()
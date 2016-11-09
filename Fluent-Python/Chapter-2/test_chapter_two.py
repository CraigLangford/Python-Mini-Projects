import unittest
from chapter_two import unicode_converter, list_comp, list_comp_map_filter
from chapter_two import cart_prod, tuple_and_array, tuple_as_record
from chapter_two import create_grades
import array
import bisect
from collections import deque


class TestChapterTwo(unittest.TestCase):
    def test_unicode_question(self):
        symbols = '$¢£¥€¤'
        self.assertEqual(unicode_converter(symbols),
                         [36, 162, 163, 165, 8364, 164])

    def test_leak(self):
        x = 'ABC'
        self.assertEqual(list_comp(x), x)

    def test_list_comp_vs_map_filter(self):
        symbols = '$¢£¥€¤'
        lc, mf = list_comp_map_filter(symbols)
        self.assertEqual(lc, mf)

    def test_cart_prod(self):
        colors = ['black', 'white']
        sizes = ['S', 'M', 'L']
        self.assertEqual(cart_prod(colors, sizes),
                         [('black', 'S'), ('black', 'M'),
                          ('black', 'L'), ('white', 'S'),
                          ('white', 'M'), ('white', 'L')])

    def test_tuple_and_array(self):
        symbols = '$¢£¥€¤'
        tuple_, array_ = tuple_and_array(symbols)
        self.assertEqual(tuple_, (36, 162, 163, 165, 8364, 164))
        self.assertEqual(array_, array.array('I',
                                             [36, 162, 163, 165, 8364, 164]))

    def test_tuple_as_record(self):
        traveler_ids = tuple_as_record()
        self.assertEqual(traveler_ids[0], ('BRA', 'CE342567'))

    def test_tuple_unpack(self):
        self.assertEqual(divmod(20, 8), (2, 4))
        t = (20, 8)
        self.assertEqual(divmod(*t), (2, 4))
        a, b, *rest = range(5)
        self.assertEqual((a, b, rest), (0, 1, [2, 3, 4]))
        a, *body, c, d = range(5)
        self.assertEqual((a, body, c, d), (0, [1, 2], 3, 4))

    def test_slicing(self):
        l = [10, 20, 30, 40, 50, 60]
        self.assertEqual(l[:2], [10, 20])
        self.assertEqual(l[4:], [50, 60])
        s = 'bicycle'
        self.assertEqual(s[::3], 'bye')
        self.assertEqual(s[::-1], 'elcycib')
        self.assertEqual(s[::-2], 'eccb')
        slice_ = slice(None, None, -1)
        self.assertEqual(s[::-1], s[slice_])

    def test_sorted(self):
        fruits = ['grape', 'raspberry', 'apple', 'banana']
        self.assertEqual(sorted(fruits), ['apple', 'banana', 'grape',
                                          'raspberry'])
        self.assertEqual(sorted(fruits, reverse=True),
                         ['raspberry', 'grape',
                          'banana', 'apple'])
        self.assertEqual(sorted(fruits, key=len),
                         ['grape', 'apple', 'banana', 'raspberry'])
        self.assertEqual(sorted(fruits, key=len, reverse=True),
                         ['raspberry', 'banana', 'grape', 'apple'])

    def test_breakpoints(self):
        grades = [33, 99, 77, 70, 89, 90, 100]
        expected = ['F', 'A', 'C', 'C', 'B', 'A', 'A']
        self.assertEqual(create_grades(grades), expected)

    def test_insort(self):
        list_ = [0, 10]
        bisect.insort(list_, 6)
        self.assertEqual(list_, [0, 6, 10])

    def test_arrays(self):
        '''
        floats = array.array('d', (random() for i in range(10**7)))
        fp = open('floats.bin', 'wb')
        floats.tofile(fp)
        fp.close()
        floats2 = array.array('d')
        fp = open('floats.bin', 'rb')
        floats2.fromfile(fp, 10**7)
        fp.close()
        '''

    def test_dequeue(self):
        dq = deque(range(5))
        self.assertEqual(list(dq), [0, 1, 2, 3, 4])
        dq.rotate(2)
        self.assertEqual(list(dq), [3, 4, 0, 1, 2])
        dq.appendleft(-3)
        self.assertEqual(list(dq), [-3, 3, 4, 0, 1, 2])

if __name__ == '__main__':
    unittest.main()

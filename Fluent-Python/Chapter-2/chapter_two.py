import array
import bisect


def unicode_converter(symbols):
    return [ord(symbol) for symbol in symbols]


def list_comp(x):
    [ord(x) for x in x]
    return x


def list_comp_map_filter(symbols):
    lc = [ord(s) for s in symbols if ord(s) > 127]
    mf = list(filter(lambda c: c > 127, map(ord, symbols)))
    return lc, mf


def cart_prod(list1, list2):
    return [(x, y) for x in list1 for y in list2]


def tuple_and_array(symbols):
    tuple_ = tuple(ord(symbol) for symbol in symbols)
    array_ = array.array('I', (ord(symbol) for symbol in symbols))
    return tuple_, array_


def tuple_as_record():
    return sorted([('USA', '31195855'), ('BRA', 'CE342567'),
                   ('ESP', 'XDA205856')])


def create_grades(num_grades, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    indexes = [bisect.bisect(breakpoints, score) for score in num_grades]
    return [grades[i] for i in indexes]

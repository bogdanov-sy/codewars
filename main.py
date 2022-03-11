from Array_diff import array_diff as ad
from filter_list import filter_list as fl
from ReplaceWithAlphabetPosition import alphabet_position as ap
from duplicate_count import duplicate_count as dc

a = [1, 2, 3, 4, 4]
b = [2, 4]
l = [0, 0, 'b', 3.5]

dc_test = 'Indivisibilities77'

text = "The sunset sets at twelve o' clock."

print(ad(a, b))
print(fl(l))
print(ap(text))
print(dc(dc_test))


class Array:
   attr0:int = 1
   attr1:int = 2
   attr2:int = 3


def mutate_array(pos:int, array: Array = Array()) -> Array:
   if pos == 0:
      array.attr0 = 2
   if pos == 1:
      array.attr1 = 4
   if pos == 2:
      array.attr2 = 6
   return array

myInstance:Array = Array()

returned_array1 = mutate_array(1)
assert returned_array1.attr1 == 4
assert myInstance.attr1 == 2
assert Array.attr1 == 2

returned_array2 = mutate_array(2,myInstance)
assert myInstance.attr2 == 6
assert returned_array2.attr2 == 6
assert Array.attr2 == 3
assert returned_array1.attr2 == 3

returned_array3 = mutate_array(0)
assert returned_array3.attr0 == 2
assert returned_array3.attr1 == 4
assert returned_array3.attr2 == 3
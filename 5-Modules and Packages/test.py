from package import maths
from package.subpackage import mul #we can also use from package.subpackage.mul import multiply (multiply is a in-built function we have imported)

print(maths.addition(89,99))
print(maths.subtraction(78,23))
print(mul.multiply(5,6))
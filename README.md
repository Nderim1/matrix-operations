

```python
# Run this cell but don't modify it.

%load_ext autoreload
%autoreload 2
from matrix import Matrix, zeroes, identity
```

    The autoreload extension is already loaded. To reload it, use:
      %reload_ext autoreload



```python
# some functionality already exists... here's a demo

m1 = Matrix([
    [1, 2],
    [3, 4]
])

m2 = Matrix([
    [2, 5],
    [6, 1]
])

print("m1 is")
print(m1)

print("m2 is")
print(m2)

print("we've also provided you with a function called zeros")
print("here's what happens when you call zeros(4,2)")
print(zeroes(4,2))

print("we've also provided you with a function called identity")
print("here's identity(3)")
print(identity(3))

print("but not everything works yet!")
print("for example, matrix addition...")
print("run the cell below to see what happens when we try...")
```

    m1 is
    1  2 
    3  4 
    
    m2 is
    2  5 
    6  1 
    
    we've also provided you with a function called zeros
    here's what happens when you call zeros(4,2)
    0.0  0.0 
    0.0  0.0 
    0.0  0.0 
    0.0  0.0 
    
    we've also provided you with a function called identity
    here's identity(3)
    1.0  0.0  0.0 
    0.0  1.0  0.0 
    0.0  0.0  1.0 
    
    but not everything works yet!
    for example, matrix addition...
    run the cell below to see what happens when we try...



```python
m1 = Matrix([
    [1, 2, 3],
    [3, 4, 4],
    [1, 2, 9]
])

m2 = Matrix([
    [2, 5, 4],
    [6, 1, 4],
    [3,4,-5]
])

m3 = m1 + m2
print("m1 + m2 is")
print(m3)
print('hello-<<<<',m2)

det = m1.determinant()
print(det)

trace = m1.trace()
print(trace)

inv = m1.inverse()
print(inv)

sm = m1+m2
print(sm)

print(-m2)
```

    m1 + m2 is
    3  7  7 
    9  5  8 
    4  6  4 
    
    hello-<<<< 2  5  4 
    6  1  4 
    3  4  -5 
    
    -12
    14
    -2.333333333333333  1.0  0.3333333333333333 
    1.9166666666666665  -0.5  -0.41666666666666663 
    -0.16666666666666666  -0.0  0.16666666666666666 
    
    3  7  7 
    9  5  8 
    4  6  4 
    
    -2  -5  -4 
    -6  -1  -4 
    -3  -4  5 
    



```python
# Try running this code. You should get an assertion error. 
# You will continue to get assertion errors until all the 
# methods in matrix.py are correctly implemented.

# You can open matrix.py by selecting File > Open... 
# and then selecting matrix.py

import test
```


```python
# open matrix.py (File > Open...) and start
# implementing matrix methods! 

# when your code passes all the tests you can submit by 
# pressing the SUBMIT button in the lower right corner 
# of this page.
```

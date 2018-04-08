

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
    
    2  5  4 
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

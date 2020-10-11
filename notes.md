# HPC in Python

- [HPC in Python](#hpc-in-python)
  - [Outline of Python Performance](#outline-of-python-performance)
  - [Where program spends time?](#where-program-spends-time)
  - [Using cProfile](#using-cprofile)
  - [Broadcasting](#broadcasting)
  - [File I/O](#file-io)
  - [Random](#random)
  - [Anatomy of `numpy.array()`](#anatomy-of-numpyarray)
  - [Speeding up complex expressions with numexpr](#speeding-up-complex-expressions-with-numexpr)

## Outline of Python Performance

* **interpreted language**: translation done by interpretor during the execution of the program
* **dynamic typing**: so difficult for the interpretor to optimize the execution, but progress in JIT compilation techniques
* **flexible data structures**: flexible so not so suited for extensive numerical computations

So, dynamic and flexible nature of Python that enhances  the productivity is the main cause for the performace problems.

## Where program spends time?

* correctness, readability and maintainability should be most focused
* Low-level optimization should be done after that.

**Time critical parts**

* Analysis through
  * timers
  * performance analysis software

```python
python3 -m timeit -n 3 -s "from mandel_main import main" "main()"
```
## Using cProfile

```bash
python3 -m cProfile -o profile.dat mandel_main.py
python3 -m pstats profile.dat

help
strip
sort 
sort time
stats 10
sort cumtime
stats 10
```

## Broadcasting

```python
    a: 8 x 3
    b:     3
a * b: 8 x 3

    a: 3 x 2
    b: 1 x 2
a * b: 3 x 2

    a: 4 x 1 x 6 x 1
    b:     5 x 1 x 3
a * b: 4 x 5 x 6 x 3

    a: 8 x 3
    b:     2  # mismatch in the last dimension

    a: 3 x 2
    b: 2 x 2  # mismatch in the first dimension

    a: 4 x 2 x 6 x 1
    b:     5 x 1 x 3  # mismatch in the third from last dimension
```

## File I/O

```python
xy = numpy.loadtxt('xy-coordinates.dat')

args = {
  'header': 'XY coordinates',
  'fmt': '%7.3f',
  'delimiter': ','
}
numpy.savetxt('output.dat', xy, **args)
```

## Random

```python
## random choice from a given array
b = np.random.choice(np.arange(4), 10)
```

## Anatomy of `numpy.array()`

* `ndarray`
  * 1-D contiguous block of memory: **raw data**
  * indexing scheme: how to locate an element
  * data type description


When one assigns a variable to a slice of another array `b = a[1:8:2, 3:12:3]`, the variable `b` has the same raw data `a`, but only different strides. Thus, changing the contents of  `b` will also change contents of `a`. 

When masking, `m = a > 0.5; b = a[m]`, `b` can't be created just by modifying the stribes, so `b` will hold a copy of the data in `a`.

**Attributes**:

* `a.flags`: information about the memory layout
* `a.strides`: bytes to step in each dimension
* `a.itemsize`: size of one array element in bytes
* `a.data`: buffer object pointing to the start of array data
* `a.__array_interface__`: python interal interface

In complex expressios, numpy stores intermediate values in temporary arrays.

```python
import numpy
a = numpy.random.random((1024, 1024, 50))
b = numpy.random.random((1024, 1024, 50))

c = 2.0 * a - 4.5 * b
```

Two temporary arrays will be created to store intermediate results. NumPy is smart enough to reuse temporary arrays when possible.

```python
c = 2.0 * a
c -= 4.5 * b
c += np.sin(a)
c += np.cos(b)

## is better than

c = (numpy.sin(a) + numpy.cos(b)) + 2.0 * a - 4.5 * b
```

```python
X = np.random.random((1000, 3))
D = np.sqrt(((X[:, np.newaxis, :] - X) ** 2).sum(axis=-1))
#            ^^^^^^^^^^^^^^^^^^^^^^^^^
#           temporary 1000x1000x3 array
```

## Speeding up complex expressions with numexpr

* using one-linear expression is not a good idea due to high memory usage
* evaluating expression with one operation at a time can lead to sub-optimal performance

> Use numexpr package

```python
x = numpy.random.random((1000000, 1))
y = numpy.random.random((1000000, 1))

import numexpr
poly = numexpr.evaluate("((.25*x + .75)*x - 1.5)*x - 2")
```

By default, numexpr tries to use multiple threads, which can also speed up the execution.

```
numexpr.set_num_threads(n)
```
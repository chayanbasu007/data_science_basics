# NumPy Learning Roadmap for Data Science

## Objective

This README is a complete NumPy checklist for a professional Data
Scientist. It includes topics already covered and topics required before
moving to Pandas.

Legend: - 🟢 Completed - 🟡 Partially Covered - 🔴 Must Learn

------------------------------------------------------------------------

# 1. NumPy Fundamentals

## Importing NumPy

🟢 Completed

``` python
import numpy as np
```

------------------------------------------------------------------------

# 2. Creating Arrays

## np.array()

🟢 Completed

``` python
arr = np.array([1,2,3,4])
```

## 1D Arrays

🟢 Completed

## 2D Arrays

🟢 Completed

## 3D Arrays

🟢 Completed

------------------------------------------------------------------------

## Additional Array Creation Methods

### np.zeros()

🔴 Learn

``` python
np.zeros((3,4))
```

### np.ones()

🔴 Learn

``` python
np.ones((2,3))
```

### np.full()

🔴 Learn

``` python
np.full((3,3),7)
```

### np.eye()

🔴 Learn

Identity matrix creation.

``` python
np.eye(3)
```

### np.arange()

🔴 Learn

``` python
np.arange(0,10,2)
```

### np.linspace()

🔴 Learn

``` python
np.linspace(0,1,5)
```

------------------------------------------------------------------------

# 3. Array Properties

🔴 Must Learn

## Shape

``` python
arr.shape
```

## Dimensions

``` python
arr.ndim
```

## Number of Elements

``` python
arr.size
```

## Data Type

``` python
arr.dtype
```

## Memory Size

``` python
arr.itemsize
```

------------------------------------------------------------------------

# 4. Array Indexing and Slicing

## Basic Indexing

🟢 Completed

``` python
arr[0]
arr[1:5]
```

## 2D Indexing

🟢 Completed

``` python
matrix[0,1]
```

## Modifying Values

🟢 Completed

``` python
arr[0] = 100
```

------------------------------------------------------------------------

# Advanced Indexing

## Boolean Indexing

🔴 Must Learn

``` python
arr[arr > 10]
```

Used heavily in Pandas:

``` python
df[df["salary"] > 50000]
```

------------------------------------------------------------------------

## Fancy Indexing

🔴 Learn

``` python
arr[[0,2,4]]
```

------------------------------------------------------------------------

# 5. Mathematical Operations

## Arithmetic Operations

🔴 Learn

-   Addition
-   Subtraction
-   Multiplication
-   Division
-   Power
-   Modulus

Example:

``` python
arr * 2
```

------------------------------------------------------------------------

# Vectorization

🔴 Must Learn

NumPy performs operations on entire arrays without explicit loops.

Example:

``` python
arr = np.array([1,2,3])
arr * 10
```

------------------------------------------------------------------------

# 6. Universal Functions (ufunc)

🔴 Learn

## Mathematical Functions

``` python
np.sqrt()
np.exp()
np.log()
np.log10()
```

## Trigonometric Functions

``` python
np.sin()
np.cos()
np.tan()
```

------------------------------------------------------------------------

# 7. Aggregation Functions

🔴 Must Learn Before Pandas

## Sum

``` python
np.sum(arr)
```

## Mean

``` python
np.mean(arr)
```

## Median

``` python
np.median(arr)
```

## Standard Deviation

``` python
np.std(arr)
```

## Variance

``` python
np.var(arr)
```

## Minimum and Maximum

``` python
np.min(arr)
np.max(arr)
```

------------------------------------------------------------------------

# 8. Random Number Generation

🟢 Completed

## Random Values

``` python
np.random.rand()
```

## Random Integers

``` python
np.random.randint()
```

## Normal Distribution

``` python
np.random.normal()
```

## Random Seed

🔴 Learn

``` python
np.random.seed(42)
```

------------------------------------------------------------------------

# 9. Shape Manipulation

🔴 Must Learn

## reshape()

``` python
arr.reshape(3,4)
```

## flatten()

``` python
arr.flatten()
```

## ravel()

``` python
arr.ravel()
```

## expand_dims()

``` python
np.expand_dims(arr,axis=0)
```

## squeeze()

``` python
np.squeeze(arr)
```

------------------------------------------------------------------------

# 10. Combining Arrays

## append()

🟢 Completed

``` python
np.append()
```

## concatenate()

🔴 Learn

``` python
np.concatenate()
```

## Vertical Stack

``` python
np.vstack()
```

## Horizontal Stack

``` python
np.hstack()
```

## Split Arrays

``` python
np.split()
```

------------------------------------------------------------------------

# 11. Broadcasting

🔴 Extremely Important

Broadcasting allows NumPy to perform operations between arrays of
different shapes.

Example:

``` python
arr = np.array([1,2,3])
arr + 10
```

Used in:

-   Feature scaling
-   Machine Learning
-   Neural Networks

------------------------------------------------------------------------

# 12. Sorting and Searching

## Sorting

🔴 Learn

``` python
np.sort(arr)
```

## Argsort

🔴 Learn

``` python
np.argsort(arr)
```

## Where

🔴 Learn

``` python
np.where(arr > 10)
```

------------------------------------------------------------------------

# 13. Missing Data Handling

🔴 Learn

## NaN Values

``` python
np.nan
```

## Check Missing Values

``` python
np.isnan(arr)
```

## Infinite Values

``` python
np.isinf(arr)
```

------------------------------------------------------------------------

# 14. Statistical Functions

🔴 Must Learn

## Percentile

``` python
np.percentile()
```

## Quantile

``` python
np.quantile()
```

## Correlation

``` python
np.corrcoef()
```

## Covariance

``` python
np.cov()
```

------------------------------------------------------------------------

# 15. Linear Algebra

## Transpose

🟢 Completed

``` python
A.T
```

## Matrix Inverse

🟢 Completed

``` python
np.linalg.inv(A)
```

## Determinant

🟢 Completed

``` python
np.linalg.det(A)
```

## Eigenvalues and Eigenvectors

🟢 Completed

``` python
np.linalg.eig(A)
```

## Rank

🟢 Completed

## Matrix Power

🟢 Completed

``` python
np.linalg.matrix_power()
```

## Diagonal Operations

🟢 Completed

``` python
np.diag()
```

------------------------------------------------------------------------

## Matrix Multiplication

🔴 Learn

``` python
np.dot(A,B)

A @ B
```

------------------------------------------------------------------------

## Solving Linear Equations

🔴 Learn

``` python
np.linalg.solve(A,b)
```

------------------------------------------------------------------------

## Norms

🔴 Learn

``` python
np.linalg.norm()
```

Used in: - Distance calculations - Regularization - Machine Learning

------------------------------------------------------------------------

## Singular Value Decomposition

🔴 Learn

``` python
np.linalg.svd()
```

Used in: - PCA - Dimensionality Reduction

------------------------------------------------------------------------

# Final Checklist Before Pandas

You should be comfortable with:

## Core NumPy

✅ Array creation\
✅ Array attributes\
✅ Indexing and slicing\
✅ Boolean indexing\
✅ Fancy indexing\
✅ Vectorization\
✅ Broadcasting\
✅ Aggregation functions\
✅ Reshaping\
✅ Combining arrays

## Data Science NumPy

✅ Statistical functions\
✅ Missing values\
✅ Correlation and covariance\
✅ Random distributions\
✅ Linear algebra basics\
✅ Matrix multiplication\
✅ Norms

------------------------------------------------------------------------

# Recommended Learning Sequence

## Phase 1: Foundation

1.  Array attributes
2.  Array creation
3.  Indexing
4.  Vectorization

## Phase 2: Data Manipulation

5.  Aggregations
6.  Boolean indexing
7.  Broadcasting
8.  Reshaping
9.  Combining arrays

## Phase 3: Data Science Concepts

10. Statistics
11. Linear Algebra
12. Random distributions
13. Missing value handling

------------------------------------------------------------------------

# After NumPy

Move to Pandas:

1.  Series
2.  DataFrames
3.  Reading CSV/Excel/SQL data
4.  Data cleaning
5.  Missing value treatment
6.  Filtering
7.  GroupBy
8.  Merge and Join
9.  Pivot Tables
10. Time Series
11. Feature Engineering

------------------------------------------------------------------------

Goal: Build strong NumPy foundations before handling real-world datasets
with Pandas.

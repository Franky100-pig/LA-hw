# Linear Algebra – Problem Set 9 — Solutions

Short practice on determinant geometry, Cramer's rule, Gram-Schmidt, QR and least squares · 9 problems

Two ideas carry this set: **the determinant measures signed area scaling**, and **Gram-Schmidt is just subtracting directions you already have**. QR is the bookkeeping of that process, and least squares is the same perpendicular-error idea in matrix form. All numerical answers below were checked with SymPy.

## Problem 1

For $A=\begin{bmatrix}2&0\\0&3\end{bmatrix}$, $\det A=6$: the unit square becomes a $2\times3$ rectangle, so area is multiplied by 6 and orientation is preserved.

For $B=\begin{bmatrix}0&1\\1&0\end{bmatrix}$, $\det B=-1$: the square is flipped across the line $y=x$, so the area factor is 1 but orientation is reversed.

For $C=\begin{bmatrix}1&2\\2&4\end{bmatrix}$, $\det C=0$: the two columns are proportional, so the square collapses onto a line and the area is 0.

## Problem 2

The coefficient matrix is $A=\begin{bmatrix}2&1\\1&3\end{bmatrix}$, with $\det A=6-1=5$.

$$x=\frac{\det\begin{bmatrix}5&1\\6&3\end{bmatrix}}{\det A}=\frac{15-6}{5}=\frac95,\qquad y=\frac{\det\begin{bmatrix}2&5\\1&6\end{bmatrix}}{\det A}=\frac{12-5}{5}=\frac75.$$

Check: $2\cdot\frac95+\frac75=5$ and $\frac95+3\cdot\frac75=6$. ✓

## Problem 3

The coefficient matrix has determinant 2. Replacing column 1 by $(3,4,5)$ gives determinant 4, so

$$x=\frac{4}{2}=2.$$

Then $y=3-x=1$ and $z=4-y=3$, so $(x,y,z)=(2,1,3)$. Check: $x+z=2+3=5$. ✓

## Problem 4

The columns are $a_1=(1,1)^T$ and $a_2=(2,0)^T$.

First, $b_1=a_1=(1,1)^T$, so

$$q_1=\frac{1}{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}.$$

Next, $q_1\cdot a_2=\sqrt2$, so the projection onto $q_1$ is $\sqrt2\,q_1=(1,1)^T$. The perpendicular remainder is

$$b_2=a_2-\sqrt2\,q_1=\begin{bmatrix}2\\0\end{bmatrix}-\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix},$$

hence

$$q_2=\frac{1}{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}.$$

Check: $q_1\cdot q_2=\frac12-\frac12=0$ and both have length 1. ✓

## Problem 5

The first vector is already clean: $b_1=(1,0,0)$.

The second loses its projection onto $b_1$:

$$b_2=(1,1,0)-(1,0,0)=(0,1,0).$$

The third loses its projections onto both earlier directions:

$$b_3=(1,1,1)-(1,0,0)-(0,1,0)=(0,0,1).$$

So Gram-Schmidt returns the standard basis $e_1,e_2,e_3$ — already orthogonal, already unit length. ✓

## Problem 6

Using Problem 4,

$$Q=\begin{bmatrix}\frac1{\sqrt2}&\frac1{\sqrt2}\\[2pt]\frac1{\sqrt2}&-\frac1{\sqrt2}\end{bmatrix},\qquad R=\begin{bmatrix}\sqrt2&\sqrt2\\0&\sqrt2\end{bmatrix}.$$

Check by columns: $\sqrt2\,q_1=a_1=(1,1)^T$ and $\sqrt2\,q_1+\sqrt2\,q_2=(1,1)^T+(1,-1)^T=(2,0)^T=a_2$. Thus $QR=A$. ✓

$R$ is upper triangular because $a_1$ only uses $q_1$, while $a_2$ uses $q_1$ and $q_2$. A column never uses a $q$ that has not been constructed yet, so the entries below the diagonal are 0.

## Problem 7

The first column gives $q_1=(1,1)^T/\sqrt2$. For the second column,

$$q_1\cdot a_2=\sqrt2,\qquad b_2=a_2-\sqrt2\,q_1=\begin{bmatrix}1\\1\end{bmatrix}-\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}0\\0\end{bmatrix}.$$

The remainder collapses to zero: the second column was already completely contained in the first direction. The columns are linearly dependent, $\det A=0$, and rank is 1, so there is no second orthogonal direction to normalize.

## Problem 8

Here $A^TA=2$ and $A^Tb=4$, so

$$\hat c=\frac{A^Tb}{A^TA}=\frac42=2.$$

The error is

$$e=b-A\hat c=\begin{bmatrix}1\\3\end{bmatrix}-\begin{bmatrix}2\\2\end{bmatrix}=\begin{bmatrix}-1\\1\end{bmatrix},$$

and its dot product with the column of $A$ is $(-1)\cdot1+1\cdot1=0$. The error is perpendicular to $\operatorname{Col}(A)$, so this is the closest possible fit. ✓

## Problem 9

(a) $p(\lambda)=\det(A-\lambda I)=(2-\lambda)^2=(\lambda-2)^2$.

(b) The only eigenvalue is $\lambda=2$, with algebraic multiplicity $\operatorname{AM}=2$. Since

$$A-2I=\begin{bmatrix}0&1\\0&0\end{bmatrix},$$

the equation $(A-2I)x=0$ gives $x_2=0$ with $x_1$ free, so the nullity is 1. Hence $\operatorname{GM}=1$.

(c) A basis for the eigenspace is $\left\{\begin{bmatrix}1\\0\end{bmatrix}\right\}$.

(d) $A$ is not diagonalizable: $\operatorname{GM}=1<2=\operatorname{AM}$, so there is only one independent eigenvector, not enough to form a basis of $\mathbb R^2$. ✓

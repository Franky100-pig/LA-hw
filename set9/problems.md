# Linear Algebra – Problem Set 9

Short practice on determinant geometry, Cramer's rule, Gram-Schmidt, QR and least squares · 9 problems

This is a short self-written set to accompany the study notes. Every problem is meant to be checkable in one or two lines: the point is to recognize the shape of each idea, not to grind through long computations.

## Problem 1

For each matrix, describe what happens to the unit square geometrically. State the area scale factor $|\det A|$ and whether orientation is preserved or reversed.

$$A=\begin{bmatrix}2&0\\0&3\end{bmatrix},\qquad B=\begin{bmatrix}0&1\\1&0\end{bmatrix},\qquad C=\begin{bmatrix}1&2\\2&4\end{bmatrix}.$$

## Problem 2

Use Cramer's rule to solve

$$2x+y=5,\qquad x+3y=6.$$

Show the two determinants you use.

## Problem 3

Use Cramer's rule to find $x$ only, then state the full solution $(x,y,z)$:

$$x+y=3,\qquad y+z=4,\qquad x+z=5.$$

## Problem 4

Apply Gram-Schmidt to the columns of

$$A=\begin{bmatrix}1&2\\1&0\end{bmatrix}.$$

Write $a_1,a_2$, then $q_1,q_2$. Check that $q_1\cdot q_2=0$ and $\|q_1\|=\|q_2\|=1$.

## Problem 5

Apply Gram-Schmidt to

$$a_1=\begin{bmatrix}1\\0\\0\end{bmatrix},\quad a_2=\begin{bmatrix}1\\1\\0\end{bmatrix},\quad a_3=\begin{bmatrix}1\\1\\1\end{bmatrix}.$$

You should get a very familiar orthogonal basis.

## Problem 6

For the same matrix as in Problem 4,

$$A=\begin{bmatrix}1&2\\1&0\end{bmatrix},$$

write the thin QR decomposition $A=QR$. Explain briefly why $R$ is upper triangular.

## Problem 7

Let

$$A=\begin{bmatrix}1&1\\1&1\end{bmatrix}.$$

Run the first steps of Gram-Schmidt on its columns. What goes wrong, and what does that say about the columns of $A$?

## Problem 8

We want one number $c$ to satisfy two measurements:

$$A=\begin{bmatrix}1\\1\end{bmatrix},\qquad b=\begin{bmatrix}1\\3\end{bmatrix}.$$

Find the least-squares value $\hat c$ and verify that the error $b-A\hat c$ is perpendicular to the column of $A$.

## Problem 9

Let

$$A=\begin{bmatrix}2&1\\0&2\end{bmatrix}.$$

(a) Find the characteristic polynomial.
(b) Find the algebraic multiplicity and geometric multiplicity of the only eigenvalue.
(c) Find a basis for the eigenspace.
(d) Is $A$ diagonalizable? Explain in one sentence.

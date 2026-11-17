# Linear Algebra – Problem Set 8

Summative Exam 3 Review · 15 problems · Eigenvalues, diagonalization, complex eigenvalues & rotation-scaling

This set is a review covering the second half of the course: change of basis, linear transformations, eigenvalues and eigenvectors, algebraic vs geometric multiplicity, diagonalization, and complex eigenvalues with rotation-scaling. Work through it in order — the later problems build on the earlier ones.

## Problem 1

Let $B=\{\mathbf b_1,\mathbf b_2\}$ and $C=\{\mathbf c_1,\mathbf c_2\}$ be ordered bases for $\mathbb{R}^2$, where
$$B=\left\{\begin{bmatrix}1\\1\end{bmatrix},\begin{bmatrix}1\\-1\end{bmatrix}\right\},\qquad C=\left\{\begin{bmatrix}2\\1\end{bmatrix},\begin{bmatrix}1\\1\end{bmatrix}\right\}.$$
(a) Find the change-of-coordinates matrix $P_{C\leftarrow B}$.
(b) Given $[\mathbf x]_B=\begin{bmatrix}3\\-2\end{bmatrix}$, find $[\mathbf x]_C$.
(c) Find the standard coordinates of $\mathbf x$.

## Problem 2

Let $T:\mathbb{R}^3\to\mathbb{R}^2$ be a linear transformation defined by $T(x,y,z)=(x+2y-z,\;2x+4y-2z)$.
(a) Find the standard matrix $A$ of $T$.
(b) Find a basis for $\ker(T)$.
(c) Determine the rank and nullity of $A$.
(d) Determine whether $T$ is one-to-one and whether it is onto. Briefly explain.

## Problem 3

Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be a linear transformation such that
$$T\left(\begin{bmatrix}1\\1\end{bmatrix}\right)=\begin{bmatrix}4\\1\end{bmatrix},\qquad T\left(\begin{bmatrix}1\\-1\end{bmatrix}\right)=\begin{bmatrix}2\\3\end{bmatrix}.$$
(a) Find the standard matrix $A$ of $T$.
(b) Find $T\left(\begin{bmatrix}3\\1\end{bmatrix}\right)$.
(c) Determine whether $T$ is invertible.

## Problem 4

Let $T:\mathbb{R}^2\to\mathbb{R}^2$ be defined by $T(x,y)=(3x+y,\;x+3y)$. Consider the ordered basis
$$B=\left\{\begin{bmatrix}1\\1\end{bmatrix},\begin{bmatrix}1\\-1\end{bmatrix}\right\}.$$
(a) Find the standard matrix $A$ of $T$.
(b) Find the matrix $[T]_B$ representing $T$ relative to $B$.
(c) Verify that $[T]_B=P_B^{-1}AP_B$, where $P_B$ is the matrix whose columns are the basis vectors of $B$.

## Problem 5

Let $A=\begin{bmatrix}3&2\\1&4\end{bmatrix}$, $\mathbf v_1=\begin{bmatrix}1\\1\end{bmatrix}$, $\mathbf v_2=\begin{bmatrix}2\\-1\end{bmatrix}$.
Determine whether each vector is an eigenvector of $A$. For each eigenvector, find its corresponding eigenvalue. Show your calculations.

## Problem 6

Let
$$A=\begin{bmatrix}3&1&0\\0&3&0\\0&0&-2\end{bmatrix}.$$
(a) Find all eigenvalues of $A$ and their algebraic multiplicities.
(b) Find a basis for each eigenspace.
(c) Find the geometric multiplicity of each eigenvalue.
(d) Determine whether $A$ is diagonalizable. Briefly explain.

## Problem 7

Let
$$A=\begin{bmatrix}2&1&0\\1&2&0\\0&0&5\end{bmatrix}.$$
(a) Find the characteristic polynomial of $A$.
(b) Find all eigenvalues of $A$.
(c) Find a basis for each eigenspace.

## Problem 8

Consider the matrices $A=\begin{bmatrix}4&1\\0&4\end{bmatrix}$, $B=\begin{bmatrix}4&0\\0&4\end{bmatrix}$.
(a) Find the characteristic polynomial of each matrix.
(b) Find the algebraic and geometric multiplicities of each eigenvalue.
(c) Are $A$ and $B$ similar? Explain your answer using their eigenspaces.

## Problem 9

Let $A=\begin{bmatrix}4&2\\1&3\end{bmatrix}$.
(a) Find all eigenvalues and a basis for each eigenspace.
(b) Find an invertible matrix $P$ and a diagonal matrix $D$ such that $A=PDP^{-1}$.
(c) Use diagonalization to find $A^4$.

## Problem 10

Let
$$A=\begin{bmatrix}1&1&0\\0&2&0\\0&0&2\end{bmatrix}.$$
(a) Find all eigenvalues of $A$ and their algebraic multiplicities.
(b) Find a basis for each eigenspace.
(c) Determine whether $A$ is diagonalizable.
(d) If $A$ is diagonalizable, construct matrices $P$ and $D$ such that $A=PDP^{-1}$.

## Problem 11

Suppose $P=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $D=\begin{bmatrix}4&0\\0&-2\end{bmatrix}$, and $A=PDP^{-1}$.
(a) Find $A$.
(b) Find $A^5$.
(c) State the eigenvalues of $A$ and give a corresponding eigenvector for each eigenvalue.

## Problem 12

Let $A=\begin{bmatrix}2&-3\\3&2\end{bmatrix}$.
(a) Find all complex eigenvalues of $A$.
(b) Find a basis for the eigenspace corresponding to the eigenvalue with positive imaginary part.
(c) Find a basis for the eigenspace corresponding to the other eigenvalue.

## Problem 13

Consider $A=\begin{bmatrix}-1&-\sqrt{3}\\\sqrt{3}&-1\end{bmatrix}$.
(a) Find the complex eigenvalues of $A$.
(b) Express $A$ in the form
$$A=r\begin{bmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{bmatrix},$$
where $r>0$ and $0\le\theta<2\pi$.
(c) Describe the geometric effect of the transformation $\mathbf x\mapsto A\mathbf x$.

## Problem 14

Let $A=\begin{bmatrix}0&-2\\2&0\end{bmatrix}$.
(a) Find all complex eigenvalues of $A$.
(b) Find a basis for each eigenspace over $\mathbb{C}$.
(c) Determine whether $A$ is diagonalizable over $\mathbb{R}$ and over $\mathbb{C}$. Briefly explain.
(d) Find $A^6$.

## Problem 15

Let
$$A=\begin{bmatrix}2&-1&0\\1&2&0\\0&0&4\end{bmatrix}.$$
(a) Find the characteristic polynomial of $A$.
(b) Find all eigenvalues of $A$ over $\mathbb{C}$.
(c) Find a basis for each eigenspace over $\mathbb{C}$.
(d) Determine whether $A$ is diagonalizable over $\mathbb{R}$ and over $\mathbb{C}$. Explain your answers.

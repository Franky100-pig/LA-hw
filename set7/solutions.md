# Linear Algebra – Problem Set 7 — Solutions

Similar Matrices & Diagonalization · Full solutions · 6 problems · Original problems in the spirit of MIT 18.06 (Strang)

Two habits carry this whole topic: **check similarity by multiplying $AP = PD$ instead of inverting $P$**, and **check a diagonalization by confirming $A\mathbf{v} = \lambda\mathbf{v}$ on each column**. Every answer below can be verified with a single multiplication.


## Problem 1

$A = \begin{bmatrix}4&1\\2&3\end{bmatrix}$, $P = \begin{bmatrix}1&1\\1&-2\end{bmatrix}$, $D = \begin{bmatrix}5&0\\0&2\end{bmatrix}$: verify $AP = PD$.

**(a)** Work column by column. The columns of $P$ are $(1,1)$ and $(1,-2)$:
$$A\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}5\\5\end{bmatrix} = 5\begin{bmatrix}1\\1\end{bmatrix}, \qquad A\begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}2\\-4\end{bmatrix} = 2\begin{bmatrix}1\\-2\end{bmatrix}.$$
So $AP = \begin{bmatrix}5&2\\5&-4\end{bmatrix}$. On the other side, $PD = \begin{bmatrix}1&1\\1&-2\end{bmatrix}\begin{bmatrix}5&0\\0&2\end{bmatrix} = \begin{bmatrix}5&2\\5&-4\end{bmatrix}$.
$AP = PD$ ✓
**(b)** Multiply $AP = PD$ on the left by $P^{-1}$: $P^{-1}AP = D$. By definition $A \sim D$.
**(c)** The diagonal entries are $5$ and $2$ — exactly the eigenvalues of $A$. They appear because the columns of $P$ are eigenvectors: multiplying column $j$ by $A$ rescales it by $\lambda_j$, and that is precisely what $PD$ does to column $j$ of $P$.


## Problem 2

Invariants of similarity: determinant, trace, eigenvalues.

**(a)** By multiplicativity and $\det(P^{-1}) = 1/\det P$:
$$\det B = \det(P^{-1}AP) = \det(P^{-1})\det A\,\det P = \frac{1}{\det P}\det A\,\det P = \det A.$$
**(b)** The trace is cyclic, $\operatorname{tr}(XY) = \operatorname{tr}(YX)$, so
$$\operatorname{tr} B = \operatorname{tr}(P^{-1}AP) = \operatorname{tr}\big((P^{-1}A)P\big) = \operatorname{tr}\big(P(P^{-1}A)\big) = \operatorname{tr}(A).$$
$\det B = \det A$ and $\operatorname{tr} B = \operatorname{tr} A$.
**(c)** $\det B = 4$ and $\operatorname{tr} B = 6$. No — the characteristic polynomial is invariant too:
$$\det(B - \lambda I) = \det\big(P^{-1}(A - \lambda I)P\big) = \det(A - \lambda I),$$
so $B$ has the *same* eigenvalues with the same algebraic multiplicities. (Its eigenvectors, however, are generally different — see Problem 6.)


## Problem 3

$I$ and $J = \begin{bmatrix}1&1\\0&1\end{bmatrix}$: same characteristic polynomial, not similar.

**(a)** For $I$, $\det(I - \lambda I) = (1-\lambda)^2$. For $J$, the matrix $J - \lambda I = \begin{bmatrix}1-\lambda & 1\\ 0 & 1-\lambda\end{bmatrix}$ is upper triangular, so its determinant is the product of the diagonal entries: $(1-\lambda)^2$.
Both have characteristic polynomial $(\lambda-1)^2$.
**(b)** The geometric multiplicity is the dimension of the eigenspace $\ker(M - I)$.
$I - I = 0$, so $\ker(0) = \mathbb{R}^2$ and the geometric multiplicity is $2$.
$J - I = \begin{bmatrix}0&1\\0&0\end{bmatrix}$ has rank $1$, so its kernel has dimension $2 - 1 = 1$: geometric multiplicity $1$.
**(c)** Similar matrices have the same geometric multiplicities (equivalently, the same diagonalizability). Here they differ ($2$ versus $1$), so $I$ and $J$ are **not similar**. Equivalently: $I$ is diagonalizable and $J$ is not, and diagonalizability is a similarity invariant.
Invariant used: geometric multiplicity of an eigenvalue (equivalently, diagonalizability).


## Problem 4

$A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$: diagonalize and compute $A^3$.

**(a)** $\det(A - \lambda I) = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda-3)(\lambda-1)$.
$\lambda = 3$: $A - 3I = \begin{bmatrix}-1&1\\1&-1\end{bmatrix} \to x = y$, so $\mathbf{v}_1 = (1,1)$.
$\lambda = 1$: $A - I = \begin{bmatrix}1&1\\1&1\end{bmatrix} \to x + y = 0$, so $\mathbf{v}_2 = (1,-1)$.
Eigenvalues $3$ and $1$; eigenvectors $(1,1)$ and $(1,-1)$.
**(b)** Put the eigenvectors in the columns and the eigenvalues on the diagonal:
$$P = \begin{bmatrix}1&1\\1&-1\end{bmatrix}, \qquad D = \begin{bmatrix}3&0\\0&1\end{bmatrix}, \qquad A = PDP^{-1}.$$
**(c)** Column by column: $A(1,1) = (3,3) = 3(1,1)$ and $A(1,-1) = (1,-1) = 1(1,-1)$. Therefore $AP = \begin{bmatrix}3&1\\3&-1\end{bmatrix} = PD$ ✓ (no inverse needed).
**(d)** Since $A = PDP^{-1}$, powers telescope: $A^3 = PD^3P^{-1}$ with $D^3 = \begin{bmatrix}27&0\\0&1\end{bmatrix}$.
$$\det P = -2, \qquad P^{-1} = -\tfrac12\begin{bmatrix}-1&-1\\-1&1\end{bmatrix} = \begin{bmatrix}\tfrac12&\tfrac12\\[2pt]\tfrac12&-\tfrac12\end{bmatrix}.$$
$$A^3 = \begin{bmatrix}1&1\\1&-1\end{bmatrix}\begin{bmatrix}27&0\\0&1\end{bmatrix}\begin{bmatrix}\tfrac12&\tfrac12\\[2pt]\tfrac12&-\tfrac12\end{bmatrix} = \begin{bmatrix}27&1\\27&-1\end{bmatrix}\begin{bmatrix}\tfrac12&\tfrac12\\[2pt]\tfrac12&-\tfrac12\end{bmatrix} = \begin{bmatrix}14&13\\13&14\end{bmatrix}.$$
Direct check: $A^2 = \begin{bmatrix}5&4\\4&5\end{bmatrix}$, so $A^3 = A^2A = \begin{bmatrix}14&13\\13&14\end{bmatrix}$ ✓.
$A^3 = \begin{bmatrix}14&13\\13&14\end{bmatrix}$.


## Problem 5

Diagonalizable over $\mathbb{R}$?

**(a)** $\begin{bmatrix}3&1\\0&3\end{bmatrix}$ — **not** diagonalizable. The eigenvalue $3$ is double, but $A - 3I = \begin{bmatrix}0&1\\0&0\end{bmatrix}$ has nullity $1$, so the geometric multiplicity ($1$) is less than the algebraic multiplicity ($2$).
**(b)** $\begin{bmatrix}2&0\\0&2\end{bmatrix}$ — diagonalizable. It is $2I$, already diagonal; the eigenvalue $2$ has geometric multiplicity $2$, so every basis qualifies.
**(c)** $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$ — **not** diagonalizable over $\mathbb{R}$. It is a rotation by $90^\circ$; its characteristic polynomial is $\lambda^2 + 1$, which has no real roots.
**(d)** $\begin{bmatrix}1&2\\2&1\end{bmatrix}$ — diagonalizable. It is symmetric, and $\det(A-\lambda I) = (1-\lambda)^2 - 4 = (\lambda-3)(\lambda+1)$ has distinct roots $3$ and $-1$.
(b) and (d) are diagonalizable; (a) fails on geometric multiplicity and (c) has no real eigenvalues.


## Problem 6

Change of basis: what $P$ does, and why eigenvalues survive.

**(a)** $P$ is a *change-of-basis matrix*: its columns are the new basis vectors written in the old coordinates. $P^{-1}$ converts a coordinate vector from the old basis to the new one, and $P^{-1}AP$ is the same linear map $A$ expressed in that new basis.
**(b)** Compute and use $P P^{-1} = I$:
$$B(P^{-1}\mathbf{v}) = (P^{-1}AP)(P^{-1}\mathbf{v}) = P^{-1}A(PP^{-1})\mathbf{v} = P^{-1}A\mathbf{v} = P^{-1}(\lambda\mathbf{v}) = \lambda(P^{-1}\mathbf{v}).$$
So $P^{-1}\mathbf{v}$ is an eigenvector of $B$ with the same eigenvalue $\lambda$.
Consequently similar matrices have the same eigenvalues, and the eigenvectors are the *same geometric vectors re-expressed in the new basis*.
**(c)** **False.** If $\mathbf{v}$ is an eigenvector of $A$, the corresponding eigenvector of $B = P^{-1}AP$ is $P^{-1}\mathbf{v}$ — generally a different coordinate vector. Only the eigenvalues (and the algebraic/geometric multiplicities) are preserved; the eigenvectors move with the basis.

Stuck, or found an error? Please open an [issue on LA-hw](https://github.com/Franky100-pig/LA-hw/issues/new) and quote the problem number.

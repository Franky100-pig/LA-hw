# Linear Algebra – Problem Set 6 — Solutions

Eigenvalues & Eigenvectors · Full solutions · 6 short problems · Original problems in the spirit of MIT 18.06 (Strang)

Every eigenvector below is checked by multiplying it out, and every spectrum is checked against $\operatorname{tr}$ and $\det$. Those two habits catch almost every mistake in this topic.


## Problem 1

$A = \begin{bmatrix}3&0\\0&-1\end{bmatrix}$; test three vectors; why $\mathbf{v} \ne \mathbf{0}$.

**(a)**
$$A\begin{bmatrix}1\\0\end{bmatrix} = \begin{bmatrix}3\\0\end{bmatrix} = 3\begin{bmatrix}1\\0\end{bmatrix}, \qquad A\begin{bmatrix}0\\1\end{bmatrix} = \begin{bmatrix}0\\-1\end{bmatrix} = (-1)\begin{bmatrix}0\\1\end{bmatrix}, \qquad A\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}3\\-1\end{bmatrix}.$$
So $(1,0)$ has eigenvalue $3$ and $(0,1)$ has eigenvalue $-1$. $(1,1)$ is not an eigenvector: $(3,-1) = c(1,1)$ would need $c = 3$ and $c = -1$ simultaneously.
Eigenvectors: $(1,0)$ with $\lambda = 3$, and $(0,1)$ with $\lambda = -1$.
**(b)** Because $A\mathbf{0} = \mathbf{0} = \lambda\mathbf{0}$ holds for *every* $\lambda$. If $\mathbf{0}$ counted, every number would be an eigenvalue of every matrix: there would be no finite list of $n$ eigenvalues, and $\det A$ = product of eigenvalues, $\operatorname{tr}A$ = sum of eigenvalues would both be meaningless. Requiring $\mathbf{v} \ne \mathbf{0}$ is what makes the spectrum a real piece of information.


## Problem 2

$B = \begin{bmatrix}2&1\\1&2\end{bmatrix}$: eigenvalues without a characteristic polynomial.

**(a)** Multiply the two symmetric directions:
$$B\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}3\\3\end{bmatrix} = 3\begin{bmatrix}1\\1\end{bmatrix}, \qquad B\begin{bmatrix}1\\-1\end{bmatrix} = \begin{bmatrix}1\\-1\end{bmatrix} = 1\cdot\begin{bmatrix}1\\-1\end{bmatrix}.$$
$\lambda = 3$ with direction $(1,1)$, and $\lambda = 1$ with direction $(1,-1)$.
**(b)** A $2\times2$ matrix has a characteristic polynomial of degree $2$, so it has exactly two eigenvalues counting multiplicity — and the two we found are distinct, so there is no room for a third. The audit confirms it: $\lambda_1 + \lambda_2 = 4 = \operatorname{tr}B = 2+2$, and $\lambda_1\lambda_2 = 3 = \det B = 4-1$.


## Problem 3

$A = \begin{bmatrix}4&1\\2&3\end{bmatrix}$: the full computation.

**(a)** Only the diagonal changes when $\lambda I$ is subtracted:
$$A - \lambda I = \begin{bmatrix}4-\lambda & 1\\ 2 & 3-\lambda\end{bmatrix}, \qquad \det(A-\lambda I) = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = (\lambda-2)(\lambda-5).$$
$\lambda = 2$ and $\lambda = 5$. Audit: $2+5 = 7 = \operatorname{tr}A$, $2\cdot 5 = 10 = \det A$ ✓.
**(b)** Each eigenvalue gets its own reduction.
$\lambda = 5$: $A - 5I = \begin{bmatrix}-1&1\\2&-2\end{bmatrix} \to \begin{bmatrix}1&-1\\0&0\end{bmatrix}$, so $x = y$ and $\mathbf{v} = t(1,1)$.
$\lambda = 2$: $A - 2I = \begin{bmatrix}2&1\\2&1\end{bmatrix} \to \begin{bmatrix}2&1\\0&0\end{bmatrix}$, so $2x+y = 0$, $y = -2x$ and $\mathbf{v} = t(1,-2)$.
**(c)** Two multiplications:
$$A\begin{bmatrix}1\\1\end{bmatrix} = \begin{bmatrix}5\\5\end{bmatrix} = 5\begin{bmatrix}1\\1\end{bmatrix}, \qquad A\begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}2\\-4\end{bmatrix} = 2\begin{bmatrix}1\\-2\end{bmatrix}.$$
Both hold, so the pairing of eigenvalues and eigenvectors is correct.


## Problem 4

$M = \begin{bmatrix}1&2\\2&4\end{bmatrix}$: the zero eigenvalue.

**(a)** Row 2 is twice row 1, so $\det M = 0$ and $M$ is singular. A singular matrix has a non-zero vector with $M\mathbf{v} = \mathbf{0}$, i.e. an eigenvector with eigenvalue $0$. The trace gives the other one: $\operatorname{tr}M = 1+4 = 5 = 0 + \lambda_2$, so $\lambda_2 = 5$.
**(b)** For $\lambda = 0$, solve $M\mathbf{v} = \mathbf{0}$: $x + 2y = 0$ gives $\mathbf{v} = t(-2,1)$. For $\lambda = 5$, $M - 5I = \begin{bmatrix}-4&2\\2&-1\end{bmatrix}$ gives $y = 2x$, so $\mathbf{v} = t(1,2)$.
Check: $M(-2,1) = (0,0)$ ✓ and $M(1,2) = (5,10) = 5(1,2)$ ✓.
Eigenvalues $0$ and $5$; eigenvectors $t(-2,1)$ and $t(1,2)$.


## Problem 5

$S = \begin{bmatrix}2&1\\0&2\end{bmatrix}$: repeated eigenvalue, one eigenvector.

**(a)** $S - \lambda I = \begin{bmatrix}2-\lambda&1\\0&2-\lambda\end{bmatrix}$ is triangular, so $\det(S-\lambda I) = (2-\lambda)^2$:
$\lambda = 2$ with algebraic multiplicity $2$.
Now $S - 2I = \begin{bmatrix}0&1\\0&0\end{bmatrix}$, and $(S-2I)\mathbf{v} = \mathbf{0}$ says $y = 0$ with $x$ free, so $\mathbf{v} = t(1,0)$: the geometric multiplicity is $1$.
**(b)** No. Diagonalising a $2\times2$ matrix needs two independent eigenvectors to serve as the columns of $P$, and here the eigenspace is only the line $\operatorname{Span}\{(1,0)\}$.
Equivalently: if $S = PDP^{-1}$ then both diagonal entries of $D$ would have to be $2$, so $D = 2I$ and $S = 2I$ — false.


## Problem 6

$A = \begin{bmatrix}4&1\\2&3\end{bmatrix}$, $P = \begin{bmatrix}1&1\\1&-2\end{bmatrix}$, $D = \begin{bmatrix}5&0\\0&2\end{bmatrix}$.

**(a)** Column $j$ of $AP$ is $A$ times column $j$ of $P$; column $j$ of $PD$ is $d_j$ times column $j$ of $P$:
$$AP = \begin{bmatrix}5 & 2\\ 5 & -4\end{bmatrix}, \qquad PD = \begin{bmatrix}5\cdot 1 & 2\cdot 1\\ 5\cdot 1 & 2(-2)\end{bmatrix} = \begin{bmatrix}5 & 2\\ 5 & -4\end{bmatrix}.$$
They agree, so $AP = PD$. The equality is exactly the statement $A\mathbf{p}_1 = 5\mathbf{p}_1$ and $A\mathbf{p}_2 = 2\mathbf{p}_2$ — the columns of $P$ are eigenvectors — which is why no inverse is needed to recognise a diagonalisation.
**(b)** $(2,-1) = (1,1) + (1,-2)$, and $A$ multiplies the first piece by $5$ and the second by $2$ each time:
$$A^k\begin{bmatrix}2\\-1\end{bmatrix} = 5^k\begin{bmatrix}1\\1\end{bmatrix} + 2^k\begin{bmatrix}1\\-2\end{bmatrix} = \begin{bmatrix}5^k + 2^k\\ 5^k - 2^{k+1}\end{bmatrix}.$$
At $k = 1$: $(5+2,\ 5-4) = (7,1)$, and indeed $A(2,-1) = (8-1,\ 4-3) = (7,1)$ ✓.

Spotted an error, or a solution that skips a step? Open an [issue on LA-hw](https://github.com/Franky100-pig/LA-hw/issues/new) and quote the problem number.

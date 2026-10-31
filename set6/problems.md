# Linear Algebra – Problem Set 6

Eigenvalues & Eigenvectors · 6 short problems · Original problems in the spirit of MIT 18.06 (Strang)

One equation, six short looks at it: $A\mathbf{v} = \lambda\mathbf{v}$. Every matrix here is $2\times2$ and every answer can be checked with a single multiplication, so the set is about the idea rather than the arithmetic. Work through it in order — Problem 3 is the only full computation, and Problem 6 reuses it.


## Problem 1

$$A = \begin{bmatrix} 3 & 0 \\ 0 & -1 \end{bmatrix}$$
(a) Compute $A(1,0)$, $A(0,1)$ and $A(1,1)$. Which of the three are eigenvectors, and with what eigenvalue?
(b) Why does the definition require $\mathbf{v} \ne \mathbf{0}$?


## Problem 2

$$B = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}$$
(a) Compute $B(1,1)$ and $B(1,-1)$. Read off two eigenvalues.
(b) Expand $\det(B - \lambda I)$ and check that it factors as $(\lambda - 3)(\lambda - 1)$. Why does that settle the list?


## Problem 3

$$A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$$
(a) Compute $\det(A - \lambda I)$ and solve for the eigenvalues.
(b) For each eigenvalue solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$ and give the eigenvectors.
(c) Check both answers with a single multiplication each.


## Problem 4

$$M = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$$
(a) Explain why $0$ is an eigenvalue. Then find the other one — try multiplying $M$ by $(1,2)$ and see what happens.
(b) Find an eigenvector for each eigenvalue.


## Problem 5

$$S = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$
(a) Find the eigenvalue and its algebraic multiplicity. Then solve $(S - 2I)\mathbf{v} = \mathbf{0}$: what is the geometric multiplicity?
(b) Can $S$ be diagonalised? One sentence of justification.


## Problem 6

Use $A = \begin{bmatrix}4&1\\2&3\end{bmatrix}$ from Problem 3, with $$P = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}, \qquad D = \begin{bmatrix} 5 & 0 \\ 0 & 2 \end{bmatrix}.$$
(a) Verify $AP = PD$. (Hint: compute column by column — no inverse needed.)
(b) Write $(2,-1)$ as a sum of the two eigenvectors, then give $A^k(2,-1)$. Check it at $k = 1$.

Stuck, or found an error? Please open an [issue on LA-hw](https://github.com/Franky100-pig/LA-hw/issues/new) and quote the problem number.

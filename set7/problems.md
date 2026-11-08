# Linear Algebra – Problem Set 7

Similar Matrices & Diagonalization · 6 problems · Original problems in the spirit of MIT 18.06 (Strang)

One sentence organizes the whole set: **similar matrices are the same linear map written in different bases**, so they differ in coordinates but not in their invariants. The set moves from verifying $AP = PD$ (1), through the invariants and their proofs (2), to the counterexample that defeats the converse — same eigenvalues do *not* imply similar (3) — then diagonalizes a matrix and uses it for $A^3$ (4), sorts diagonalizable from not (5), and finishes with the change-of-basis argument for why eigenvalues survive (6).


## Problem 1

Let $$A = \begin{bmatrix}4&1\\2&3\end{bmatrix}, \qquad P = \begin{bmatrix}1&1\\1&-2\end{bmatrix}, \qquad D = \begin{bmatrix}5&0\\0&2\end{bmatrix}.$$
(a) Compute $AP$ and $PD$ column by column, and verify $AP = PD$.
(b) Conclude $P^{-1}AP = D$, i.e. $A \sim D$. (You do not need to invert $P$.)
(c) What are the diagonal entries of $D$, and where did they come from?
Check it in the calculator: [load this matrix →](https://la-helper.app.workbuddy.host/#op=eigen&A=%5B%5B%224%22%2C%221%22%5D%2C%5B%222%22%2C%223%22%5D%5D) (eigenvalues & eigenvectors, one click)


## Problem 2

Suppose $B = P^{-1}AP$ with $P$ invertible.
(a) Prove $\det B = \det A$ using the multiplicativity of the determinant.
(b) Prove $\operatorname{tr} B = \operatorname{tr} A$. (Hint: the trace is cyclic, $\operatorname{tr}(XY) = \operatorname{tr}(YX)$.)
(c) A $3\times3$ matrix $A$ has $\det A = 4$ and $\operatorname{tr} A = 6$. If $B \sim A$, what are $\det B$ and $\operatorname{tr} B$? Can $B$ have a different set of eigenvalues?
Check it in the calculator: [load a matrix →](https://la-helper.app.workbuddy.host/#op=det&A=%5B%5B%224%22%2C%221%22%5D%2C%5B%222%22%2C%223%22%5D%5D) (determinant, one click)


## Problem 3

Let $$I = \begin{bmatrix}1&0\\0&1\end{bmatrix}, \qquad J = \begin{bmatrix}1&1\\0&1\end{bmatrix}.$$
(a) Show that both have characteristic polynomial $(\lambda-1)^2$.
(b) Find the geometric multiplicity of $\lambda = 1$ for each matrix.
(c) Conclude that $I$ and $J$ are **not** similar. Which invariant did you use?
This is the set's warning: an identical characteristic polynomial (hence identical eigenvalues) is necessary but *not* sufficient for similarity.


## Problem 4

Let $A = \begin{bmatrix}2&1\\1&2\end{bmatrix}$.
(a) Find the eigenvalues and a basis of eigenvectors.
(b) Build $P$ from the eigenvectors and write down $D$ with $A = PDP^{-1}$.
(c) Verify $AP = PD$ (column by column) rather than computing a full inverse.
(d) Use $A = PDP^{-1}$ to compute $A^3$. Check the answer against $A^2 \cdot A$ directly.
Check it in the calculator: [load this matrix →](https://la-helper.app.workbuddy.host/#op=eigen&A=%5B%5B%222%22%2C%221%22%5D%2C%5B%221%22%2C%222%22%5D%5D) (eigenvalues & eigenvectors, one click)


## Problem 5

For each matrix, say whether it is diagonalizable over $\mathbb{R}$ and give a one-line reason.
(a) $\begin{bmatrix}3&1\\0&3\end{bmatrix}$    (b) $\begin{bmatrix}2&0\\0&2\end{bmatrix}$    (c) $\begin{bmatrix}0&-1\\1&0\end{bmatrix}$    (d) $\begin{bmatrix}1&2\\2&1\end{bmatrix}$
The test: the geometric multiplicity of every eigenvalue must equal its algebraic multiplicity; a matrix with distinct real eigenvalues always passes.


## Problem 6

(a) In $B = P^{-1}AP$, what does $P$ do geometrically?
(b) Prove: if $A\mathbf{v} = \lambda\mathbf{v}$ and $B = P^{-1}AP$, then $B(P^{-1}\mathbf{v}) = \lambda(P^{-1}\mathbf{v})$. What does this say about the eigenvectors of similar matrices?
(c) True or false: similar matrices have the *same* eigenvectors. Explain.

Stuck, or found an error? Please open an [issue on LA-hw](https://github.com/Franky100-pig/LA-hw/issues/new) and quote the problem number.

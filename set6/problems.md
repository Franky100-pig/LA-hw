# Linear Algebra – Problem Set 6

Eigenvalues & Eigenvectors · Mostly 2×2, deliberately computational-light · 11 problems · Original problems in the spirit of MIT 18.06 (Strang)

Sets 1–5 built the vocabulary — determinants, elimination, independence, the three subspaces. This set asks what happens when a single vector meets a matrix and survives: $A\mathbf{v} = \lambda \mathbf{v}$. The whole payoff fits in one sentence: **on an eigenvector, multiplication by $A$ is multiplication by a number** — which is why $A^{100}\mathbf{v}$, the long-run behaviour of a repeated process, and even the shape of $A$ itself become arithmetic on $\lambda$ instead of matrix algebra. The numbers here are deliberately tiny so the effort goes into *why* rather than *how long*; almost every answer can be checked with a single multiplication, and failures are part of the syllabus: repeated roots with too few vectors (Problems 7), complex roots with no real direction (Problem 8), and $\lambda = 0$ (Problem 5). Structurally the set is one idea defended from three sides — recognise eigenvectors without grinding (Problems 2, 3), understand the eigenspace as a subspace (Problem 4), and know what survives a change of coordinates (Problems 9, 10). Verification at any point is one click away in the [LA Helper](https://la-helper.app.workbuddy.host/) calculator.


## Problem 1 — What the definition says (and why $\mathbf{v} \ne \mathbf{0}$)

$$A = \begin{bmatrix} 3 & 0 \\ 0 & -1 \end{bmatrix}$$
(a) Compute $A\mathbf{v}$ for each of $\mathbf{v} = (1,0),\ (0,1),\ (1,1),\ (2,0)$. In which cases is $A\mathbf{v}$ a scalar multiple of $\mathbf{v}$? Name the eigenvalue each time.
(b) A student argues: “$A\mathbf{0} = \mathbf{0} = \lambda\,\mathbf{0}$ for *every* number $\lambda$, so every scalar is an eigenvalue of every matrix, with eigenvector $\mathbf{0}$.” Which word of the definition rules this out, and — more usefully — what information would the word “eigenvalue” retain if we allowed it?
(c) Describe geometrically what $A$ does to the unit square with corners $(0,0),(1,0),(1,1),(0,1)$. Explain why the directions you found in (a) are exactly the ones that survive as lines through the origin.


## Problem 2 — Spotting eigenvectors without a characteristic polynomial

$$B = \begin{bmatrix} 2 & 1 \\ 1 & 2 \end{bmatrix}, \qquad C = \begin{bmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{bmatrix}$$
(a) Multiply $B(1,1)$ and $B(1,-1)$. Without computing $\det(B - \lambda I)$, read off two eigenvalues of $B$.
(b) Explain how $\operatorname{tr} B$ and $\det B$ let you conclude those are *all* the eigenvalues — say precisely what two facts you are using.
(c) Every row of $C$ adds to the same number $s$. Prove in one line that $(1,1,1)$ is an eigenvector of $C$, then verify it by multiplication.
(d) Using only $\operatorname{tr} C$, $\det C$ and the eigenvalue from (c), determine the remaining two eigenvalues of $C$ without writing $\det(C - \lambda I)$.


## Problem 3 — The full procedure, once and carefully

$$A = \begin{bmatrix} 4 & 1 \\ 2 & 3 \end{bmatrix}$$
(a) Write down $A - \lambda I$, compute $\det(A - \lambda I)$, and factor it to obtain the characteristic equation.
(b) Solve for the eigenvalues. Check them two ways: their sum against $\operatorname{tr} A$, their product against $\det A$.
(c) For each eigenvalue, substitute it into $A - \lambda I$ and solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$. Give each eigenspace as a basis times a free parameter.
(d) Verify both answers by computing $A\mathbf{v}$ and comparing it with $\lambda\mathbf{v}$. Why is this last step not optional?
(e) Both reduced matrices in (c) have rank 1. Explain what would have gone wrong if one of them had come out rank 0.


## Problem 4 — The eigenspace is a subspace; the eigenvectors are not

Keep $A = \begin{bmatrix}4 & 1 \\ 2 & 3\end{bmatrix}$ from Problem 3, where the results are $A(1,1) = 5(1,1)$ and $A(1,-2) = 2(1,-2)$. Let $E_\lambda$ denote the eigenspace for $\lambda$ *together with* the zero vector.
(a) Prove directly from $A\mathbf{v} = \lambda\mathbf{v}$ — no null spaces yet — that if $\mathbf{v}, \mathbf{w} \in E_\lambda$ then every combination $c\mathbf{v} + d\mathbf{w}$ is also in $E_\lambda$.
(b) Now identify $E_\lambda$ with $\operatorname{Nul}(A - \lambda I)$ and explain why (a) was guaranteed before you started.
(c) Compute $A\big((1,1) + (1,-2)\big) = A(2,-1)$ and decide whether the sum is an eigenvector. What does this say about the union $E_5 \cup E_2$ as a subspace?
(d) Under what precise condition is the sum of two eigenvectors again an eigenvector? State the corrected version of the tempting rule “eigenvectors are closed under addition”.


## Problem 5 — $\lambda = 0$, invertibility, and reading eigenvalues off trace and determinant

(a) Prove that $0$ is an eigenvalue of $A$ if and only if $A$ is singular. (Chain the equivalences explicitly.)
(b) $M = \begin{bmatrix}1 & 2 \\ 2 & 4\end{bmatrix}$. Without forming a characteristic polynomial, find both eigenvalues. Then find a basis for each eigenspace.
(c) $N$ is $3 \times 3$ with $\det N = 6$, $\operatorname{tr} N = 6$, and two known eigenvalues $1$ and $2$. Find the third eigenvalue, say whether $N$ is invertible, and list the eigenvalues of $N^{-1}$ and of $N^2$.
(d) Explain in general why $\det A$ being the *product* of the eigenvalues makes “$A$ is singular” and “some eigenvalue is $0$” the same statement.


## Problem 6 — Distinct eigenvalues buy independence

(a) Suppose $A\mathbf{v} = \lambda\mathbf{v}$, $A\mathbf{w} = \mu\mathbf{w}$ with $\lambda \ne \mu$. Prove that $\mathbf{v}$ and $\mathbf{w}$ are linearly independent. (Start with $c\mathbf{v} + d\mathbf{w} = \mathbf{0}$, apply $A$, then subtract $\lambda$ times the original equation.) Point out exactly where $\lambda \ne \mu$ and $\mathbf{w} \ne \mathbf{0}$ are used.
(b) Explain why (a) immediately gives: an $n \times n$ matrix with $n$ distinct eigenvalues is diagonalisable. Apply it to the matrix $A$ of Problem 3.
(c) Is the converse true — must a diagonalisable matrix have distinct eigenvalues? Give a counterexample and explain why being *already diagonal* is the extreme case.
(d) Does anything in (a) require the eigenvalues to be real? Discuss briefly.


## Problem 7 — Repeated root, missing vectors: the shear

$$S = \begin{bmatrix} 2 & 1 \\ 0 & 2 \end{bmatrix}$$
(a) Compute the characteristic polynomial of $S$ and state the algebraic multiplicity of its eigenvalue.
(b) Solve $(S - 2I)\mathbf{v} = \mathbf{0}$. How many linearly independent eigenvectors are there? Give the geometric multiplicity.
(c) Give two independent arguments that $S$ is not diagonalisable: one counting eigenvectors, and one arguing that if $S = PDP^{-1}$ then every diagonal entry of $D$ would have to be $2$, forcing $S = 2I$.
(d) Contrast with $2I = \begin{bmatrix}2 & 0 \\ 0 & 2\end{bmatrix}$: same eigenvalue, same algebraic multiplicity, but it *is* diagonalisable. Name exactly what separates them.
(e) Describe geometrically what $S$ does to the plane, and why the single eigendirection you found is the only line that stays put.


## Problem 8 — Complex eigenvalues mean rotate-and-scale

$$R = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}, \qquad H = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}, \qquad K = \begin{bmatrix} 1 & -1 \\ 1 & 1 \end{bmatrix}$$
(a) Compute the characteristic polynomial of $R$ and its eigenvalues. Explain, without any algebra, why $R$ can have *no* real eigenvector.
(b) Do the same for the reflection $H$, and find its eigenvectors. Why does swapping two numbers change complex roots into real ones? (Compare $\det R$ and $\det H$; both have trace $0$.)
(c) For $K$, compute the eigenvalues $1 \pm i$. Write them in polar form $re^{\pm i\theta}$ and predict what $K$ does to a vector geometrically. Test the prediction on $(1,0) \mapsto K(1,0)$: does the length scale by $r$ and the direction turn by $\theta$?
(d) State the general dictionary: a conjugate pair $a \pm bi$ corresponds to what combination of rotation and scaling? What real matrices are guaranteed never to produce complex eigenvalues?


## Problem 9 — Diagonalisation and the power of powers

Back to $A = \begin{bmatrix}4 & 1 \\ 2 & 3\end{bmatrix}$ (Problem 3: $\lambda = 5$ with $(1,1)$, $\lambda = 2$ with $(1,-2)$). Take $$P = \begin{bmatrix} 1 & 1 \\ 1 & -2 \end{bmatrix}, \qquad D = \begin{bmatrix} 5 & 0 \\ 0 & 2 \end{bmatrix}.$$
(a) Compute $AP$ and $PD$ column by column. Explain why checking $AP = PD$ is the *same* statement as “the columns of $P$ are eigenvectors of $A$”, and why that means you never have to invert anything to recognise a diagonalisation.
(b) Compute $P^{-1}$ and verify $A = PDP^{-1}$ explicitly.
(c) Write $(2,-1)$ as a combination of the two eigenvectors. Then give a formula for $A^k(2,-1)$ for every $k \ge 1$ with no matrix multiplication at all. Check it at $k = 1$ and $k = 2$.
(d) What does $A^k(2,-1)$ look like when divided by $5^k$ and $k \to \infty$? Explain why the largest $|\lambda|$ governs the long run, and identify that limiting direction geometrically.


## Problem 10 — Similar matrices: what survives a change of coordinates

Let $B = P^{-1}AP$ for some invertible $P$.
(a) Show that $A$ and $B$ have the same characteristic polynomial, hence the same eigenvalues with the same algebraic multiplicities. (Use $\det(XY) = \det X \det Y$.)
(b) Show that eigenvectors are *not* preserved: if $A\mathbf{v} = \lambda \mathbf{v}$, prove $B(P^{-1}\mathbf{v}) = \lambda (P^{-1}\mathbf{v})$. Verify this concretely using $A$ and $P$ from Problem 9, where $B = \begin{bmatrix}5 & 0 \\ 0 & 2\end{bmatrix}$: compute $P^{-1}(1,1)$ and $P^{-1}(1,-2)$.
(c) Show the converse of (a) fails: exhibit two matrices with identical eigenvalues (counting multiplicity) that are not similar. Use $S$ from Problem 7 and $2I$, and argue from eigenvalues alone that no invertible $P$ can connect them.
(d) List three quantities that are the same for all similar matrices, and explain why “same eigenvalues” is a statement about an invariant while “same eigenvectors” is not.


## Problem 11 — True or false, with a one-line reason

Decide each statement. A correct answer with the wrong justification is a wrong answer — give the counterexample or the proof.
(i) Every real $2 \times 2$ matrix has a real eigenvalue.
(ii) If $0$ is an eigenvalue of $A$, then $A$ is singular — and conversely.
(iii) If $\mathbf{v}$ is an eigenvector of $A$ with eigenvalue $\lambda$, then $\mathbf{v}$ is an eigenvector of $A + 3I$ with eigenvalue $\lambda + 3$.
(iv) If $\mathbf{v}$ is an eigenvector of $A$, then $\mathbf{v}$ is an eigenvector of $A^{T}$. (Test $(1,1)$ with the matrix of Problem 3, then say what $A$ and $A^{T}$ *do* share.)
(v) The sum of two eigenvectors of $A$ is always an eigenvector of $A$.
(vi) Eigenvectors belonging to distinct eigenvalues are linearly independent.
(vii) Two matrices with the same characteristic polynomial are similar.

Stuck, or found an error? Every problem here is original work — please open an [issue on LA-hw](https://github.com/Franky100-pig/LA-hw/issues/new) and quote the problem number.

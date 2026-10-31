# LA-hw

Original Linear Algebra practice sets with full worked solutions. It can be used with the LA Helper to strengthen your Linear Algebra knowledge.

All problems are self-written mimicking the form of MIT 18.06 (Gilbert Strang) — no school or course materials are included. If there are similar questions, those are just coincidences. 

Set 1 covers determinant properties, row operations, cofactor structure and Cramer's rule, with proof-style reasoning questions. 

Set 2 applies row echelon form to the determinant: tracking swaps and scalings, spotting singularity before computing, and a proof that a pivot in every row is exactly $\det A \neq 0$. 

Set 3 turns those tools onto vectors — linear independence, bases and dimension — where the unifying idea is that independence is a question about solutions: $Ac = 0$, $Ac = b$ and $Bc = v$ are the same three tools answering three different questions. It closes the loop with the equivalence $\det A \neq 0 \iff$ independent columns $\iff$ trivial null space $\iff$ invertible, and includes two applied problems (polynomials as coefficient vectors, and whether experimental data is collinear). 

Set 4 steps back from computation to concepts: what makes a set a vector space or a subspace (the three-step test), why each axiom exists, span as closure, bases as coordinate systems, and the kernel–image pair with rank-nullity — deliberately light on computation, building the vocabulary that later problem sets will combine.

Set 5 turns that vocabulary into computation. Every matrix carries three subspaces — Col(A), Row(A) and Nul(A) — and the whole point of row reduction is to describe them. One asymmetry organizes the entire set: **row operations preserve the row space and the dependence pattern of the columns, but not the column space itself.** That is why the basis for Col(A) is read off the original matrix while the basis for Row(A) is read off the reduced one, and Problem 10 is devoted to the misconception that comes from getting this backwards. The set closes with rank–nullity, which converts "shape plus one number" into answers about pivots, independence and solvability, and with the equivalence chain that ties rank, nullity, pivots and invertibility into a single fact.

Set 6 is six short problems on eigenvalues and eigenvectors — deliberately brief, one idea per problem, every matrix $2\times2$. The single sentence behind it: **on an eigenvector, multiplication by $A$ is multiplication by a number**, which is what turns $A^k\mathbf{v}$ into $\lambda^k\mathbf{v}$. The set moves in order: test a definition (Problem 1), recognise eigenvectors by symmetry instead of grinding (2), do the full computation once (3), spot a zero eigenvalue from a dependent row (4), meet the one matrix that cannot be diagonalised — the shear $\begin{bmatrix}2&1\\0&2\end{bmatrix}$ (5) — and finish by computing $A^k$ from the eigenbasis (6). Each answer is checkable with a single multiplication.

## Contents

| Set | Topics | Problems | Solutions |
|---|---|---|---|
| Set 1 | Determinants, Cofactors & Adjugate, Cramer's Rule | [`.pdf`](set1/problems.pdf) · [`.html`](set1/problems.html) | [`.pdf`](set1/solutions.pdf) · [`.docx`](set1/solutions.docx) · [`.html`](set1/solutions.html) |
| Set 2 | Row Echelon Form & the Determinant | [`.pdf`](set2/problems.pdf) · [`.html`](set2/problems.html) | [`.pdf`](set2/solutions.pdf) · [`.docx`](set2/solutions.docx) · [`.html`](set2/solutions.html) |
| Set 3 | Linear Independence, Bases & Dimension | [`.pdf`](set3/problems.pdf) · [`.html`](set3/problems.html) | [`.pdf`](set3/solutions.pdf) · [`.docx`](set3/solutions.docx) · [`.html`](set3/solutions.html) |
| Set 4 | Vector Spaces & Bases | [`.pdf`](set4/problems.pdf) · [`.html`](set4/problems.html) | [`.pdf`](set4/solutions.pdf) · [`.docx`](set4/solutions.docx) · [`.html`](set4/solutions.html) |
| Set 5 | Column, Row & Null Spaces; Rank & Nullity | [`.pdf`](set5/problems.pdf) · [`.html`](set5/problems.html) | [`.pdf`](set5/solutions.pdf) · [`.docx`](set5/solutions.docx) · [`.html`](set5/solutions.html) |
| Set 6 | Eigenvalues & Eigenvectors | [`.pdf`](set6/problems.pdf) · [`.html`](set6/problems.html) | [`.pdf`](set6/solutions.pdf) · [`.docx`](set6/solutions.docx) · [`.html`](set6/solutions.html) |

Solution formats:

- **`.docx`** — editable, native Word equations (opens in Word, Pages, WPS, Google Docs)
- **`.pdf`** — LaTeX-typeset, fixed layout
- **`.html`** — self-contained, MathJax-rendered (open in a browser)

## Questions & corrections

If a solution looks wrong, an assumption is unstated, or a problem does not make sense, please **open an issue on [LA-hw/issues](https://github.com/Franky100-pig/LA-hw/issues/new)** and quote the set and problem number (e.g. `Set 6, Problem 7(c)`). Corrections with a counterexample are especially welcome.

Two separate places, to keep reports from getting lost:

- **Problem sets** (statements, solutions, typos) → [LA-hw issues](https://github.com/Franky100-pig/LA-hw/issues)
- **The calculator** (engine errors, wrong output, UI) → [LA-Helper issues](https://github.com/Franky100-pig/LA-Helper/issues)

## 应用科普 · Applied reading

Short, plain-language notes on where the linear algebra from these sets actually shows up — vectors, matrices and inner products doing real work. No prerequisites, no proofs, and no formulas to grind through.

| Article | Concepts | Read |
|---|---|---|
| [你以为手机在偷听你，其实是线性代数在算你](应用科普/线性代数与推荐算法.md) | Vectors, cosine similarity, sparse matrices and matrix factorization inside a recommender system | [`.md`](应用科普/线性代数与推荐算法.md) |

New articles go in the [`应用科普/`](应用科普/) folder.

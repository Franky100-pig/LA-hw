# Linear Algebra – Problem Set 8 — Solutions

Summative Exam 3 Review · Full solutions · 15 problems · Eigenvalues, diagonalization, complex eigenvalues

Two ideas carry the whole set: **the change-of-basis matrix translates coordinates between bases**, and **a matrix is diagonalizable exactly when every algebraic multiplicity equals its geometric multiplicity** ($\sum \mathrm{GM}=n$). For rotation-scaling matrices $\begin{bmatrix}a&-b\\b&a\end{bmatrix}$, the eigenvalues are $a\pm bi$ and the geometry is "rotate by $\theta=\operatorname{atan2}(b,a)$, scale by $r=\sqrt{a^2+b^2}$". Every answer below was verified with SymPy.

## Problem 1

$P_B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $P_C=\begin{bmatrix}2&1\\1&1\end{bmatrix}$, $P_C^{-1}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}$.

**(a)** The change-of-basis matrix is $P_{C\leftarrow B}=P_C^{-1}P_B$:
$$P_{C\leftarrow B}=\begin{bmatrix}1&-1\\-1&2\end{bmatrix}\begin{bmatrix}1&1\\1&-1\end{bmatrix}=\begin{bmatrix}0&2\\1&-3\end{bmatrix}.$$
Column check: $\mathbf b_1=(1,1)=0\mathbf c_1+1\mathbf c_2$; $\mathbf b_2=(1,-1)=2\mathbf c_1-3\mathbf c_2$.

**(b)** $[\mathbf x]_C=P_{C\leftarrow B}[\mathbf x]_B=\begin{bmatrix}0&2\\1&-3\end{bmatrix}\begin{bmatrix}3\\-2\end{bmatrix}=\begin{bmatrix}-4\\9\end{bmatrix}$.

**(c)** $\mathbf x=P_B[\mathbf x]_B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}\begin{bmatrix}3\\-2\end{bmatrix}=\begin{bmatrix}1\\5\end{bmatrix}$. Check via $C$: $P_C[\mathbf x]_C=(1,5)$ ✓

## Problem 2

**(a)** $A=\begin{bmatrix}T(e_1)&T(e_2)&T(e_3)\end{bmatrix}=\begin{bmatrix}1&2&-1\\2&4&-2\end{bmatrix}$.

**(b)** Row 2 is twice row 1; $\operatorname{rref}(A)=\begin{bmatrix}1&2&-1\\0&0&0\end{bmatrix}$, so $x=-2y+z$ with $y,z$ free:
$$\ker T=\operatorname{span}\left\{\begin{bmatrix}-2\\1\\0\end{bmatrix},\begin{bmatrix}1\\0\\1\end{bmatrix}\right\}.$$

**(c)** $\operatorname{rank}A=1$, $\operatorname{nullity}A=2$ (rank–nullity: $1+2=3$).

**(d)** Not one-to-one (kernel is nonzero). Not onto: $\operatorname{rank}A=1<2=\dim\mathbb{R}^2$, so the image is only a line in $\mathbb{R}^2$ (spanned by $(1,2)$).

## Problem 3

**(a)** Write the two input/output pairs as $AS=Y$ with $S=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $Y=\begin{bmatrix}4&2\\1&3\end{bmatrix}$. Then $A=YS^{-1}=\begin{bmatrix}4&2\\1&3\end{bmatrix}\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}=\begin{bmatrix}3&1\\2&-1\end{bmatrix}$.

**(b)** $T(3,1)=A\begin{bmatrix}3\\1\end{bmatrix}=\begin{bmatrix}10\\5\end{bmatrix}$. (Equivalently $(3,1)=2(1,1)+(1,-1)$, so $T(3,1)=2(4,1)+(2,3)=(10,5)$.)

**(c)** $\det A=3(-1)-1(2)=-5\neq0$, so $A$ is invertible.

## Problem 4

**(a)** $A=\begin{bmatrix}3&1\\1&3\end{bmatrix}$.

**(b)** The basis vectors are eigenvectors: $A(1,1)=(4,4)=4(1,1)$ and $A(1,-1)=(2,-2)=2(1,-1)$. Hence $[T]_B=\begin{bmatrix}4&0\\0&2\end{bmatrix}$.

**(c)** $P_B=\begin{bmatrix}1&1\\1&-1\end{bmatrix}$, $P_B^{-1}=\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}$, and
$$P_B^{-1}AP_B=\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}\begin{bmatrix}4&2\\4&-2\end{bmatrix}=\begin{bmatrix}4&0\\0&2\end{bmatrix}=[T]_B\;\checkmark$$
Because $B$ consists of eigenvectors, $[T]_B$ is diagonal with the eigenvalues on the diagonal.

## Problem 5

$A(1,1)^T=\begin{bmatrix}5\\5\end{bmatrix}=5(1,1)^T$ → $\mathbf v_1$ is an eigenvector with $\lambda=5$.
$A(2,-1)^T=\begin{bmatrix}4\\-2\end{bmatrix}=2(2,-1)^T$ → $\mathbf v_2$ is an eigenvector with $\lambda=2$.
Check: $\det A=10=5\cdot2$ (product of eigenvalues) ✓ Two distinct eigenvalues ⇒ two independent eigenvectors ⇒ $A$ is diagonalizable.

## Problem 6

**(a)** Upper triangular: eigenvalues are the diagonal entries. $\lambda=3$ (AM $=2$), $\lambda=-2$ (AM $=1$). $p(\lambda)=(\lambda-3)^2(\lambda+2)$.

**(b)** $\lambda=3$: $A-3I=\begin{bmatrix}0&1&0\\0&0&0\\0&0&-5\end{bmatrix}$ gives $x_2=x_3=0$, basis $\{(1,0,0)\}$.
$\lambda=-2$: $A+2I=\begin{bmatrix}5&1&0\\0&5&0\\0&0&0\end{bmatrix}$ gives $x_1=x_2=0$, basis $\{(0,0,1)\}$.

**(c)** $\mathrm{GM}(3)=1$, $\mathrm{GM}(-2)=1$.

**(d)** Not diagonalizable: for $\lambda=3$, GM $=1<$ AM $=2$; only $1+1=2<3$ independent eigenvectors.

## Problem 7

**(a)** Block diagonal: $\det(A-\lambda I)=\big[(2-\lambda)^2-1\big](5-\lambda)=(1-\lambda)(3-\lambda)(5-\lambda)$, i.e. $p(\lambda)=(\lambda-1)(\lambda-3)(\lambda-5)$.

**(b)** Eigenvalues $\lambda=1,3,5$ (each AM $=1$).

**(c)** $\lambda=3$: basis $(1,1,0)$. $\lambda=1$: basis $(-1,1,0)$. $\lambda=5$: basis $(0,0,1)$.

## Problem 8

**(a)** Both have $p(\lambda)=(\lambda-4)^2$.

**(b)** Eigenvalue $\lambda=4$, AM $=2$ for both. For $A$: $A-4I=\begin{bmatrix}0&1\\0&0\end{bmatrix}$ → $E_4=\operatorname{span}\{(1,0)\}$, GM $=1$. For $B=4I$: $E_4=\mathbb{R}^2$, GM $=2$.

**(c)** Not similar. Similar matrices have equal geometric multiplicities (if $B=P^{-1}AP$ then $E_\lambda(B)=P^{-1}E_\lambda(A)$, same dimension). Here GM$_A=1\neq2=$ GM$_B$. Also $A$ is not diagonalizable while $B$ already is. This is the classic counterexample: same characteristic polynomial does not imply similar.

## Problem 9

**(a)** $p(\lambda)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$, so $\lambda=5,2$. $\lambda=5$: basis $(2,1)$. $\lambda=2$: basis $(-1,1)$.

**(b)** $P=\begin{bmatrix}2&-1\\1&1\end{bmatrix}$ (columns are eigenvectors), $D=\begin{bmatrix}5&0\\0&2\end{bmatrix}$, $A=PDP^{-1}$. Verified: $PDP^{-1}=\begin{bmatrix}4&2\\1&3\end{bmatrix}=A$.

**(c)** $A^4=PD^4P^{-1}$ with $D^4=\operatorname{diag}(625,16)$:
$$A^4=\begin{bmatrix}422&406\\203&219\end{bmatrix}.$$
(Direct multiplication of $A^4$ gives the same.)

## Problem 10

**(a)** Upper triangular: $\lambda=1$ (AM $=1$), $\lambda=2$ (AM $=2$); $p(\lambda)=(1-\lambda)(2-\lambda)^2$.

**(b)** $\lambda=1$: basis $(1,0,0)$. $\lambda=2$: $A-2I=\begin{bmatrix}-1&1&0\\0&0&0\\0&0&0\end{bmatrix}$ → $x_1=x_2$, $x_2,x_3$ free; basis $\{(1,1,0),(0,0,1)\}$, GM $=2$.

**(c)** Diagonalizable: GM $=$ AM for both eigenvalues, and $\sum\mathrm{GM}=1+2=3=n$.

**(d)** $P=\begin{bmatrix}1&1&0\\0&1&0\\0&0&1\end{bmatrix}$ (columns: eigenvectors for $1,2,2$), $D=\operatorname{diag}(1,2,2)$, with $A=PDP^{-1}$.

## Problem 11

**(a)** $A=PDP^{-1}=\begin{bmatrix}4&-2\\4&2\end{bmatrix}\begin{bmatrix}\tfrac12&\tfrac12\\\tfrac12&-\tfrac12\end{bmatrix}=\begin{bmatrix}1&3\\3&1\end{bmatrix}$.

**(b)** $A^5=PD^5P^{-1}$ with $D^5=\operatorname{diag}(4^5,(-2)^5)=\operatorname{diag}(1024,-32)$:
$$A^5=\begin{bmatrix}496&528\\528&496\end{bmatrix}.$$

**(c)** Eigenvalues are the diagonal entries of $D$: $\lambda=4$ with eigenvector (column 1 of $P$) $(1,1)$; $\lambda=-2$ with eigenvector $(1,-1)$. Check: $A(1,1)^T=4(1,1)^T$, $A(1,-1)^T=-2(1,-1)^T$.

## Problem 12

**(a)** $p(\lambda)=(2-\lambda)^2+9=\lambda^2-4\lambda+13$, so $\lambda=2\pm3i$. (Rotation-scaling form $a=2,b=3$.)

**(b)** For $\lambda=2+3i$: $(A-(2+3i)I)\mathbf v=0$ gives $v_2=-iv_1$; take $v_1=i$ → basis $\left\{\begin{bmatrix}i\\1\end{bmatrix}\right\}$. Check: $A(i,1)^T=(2+3i)(i,1)^T$.

**(c)** Conjugate eigenvalue $\lambda=2-3i$ has basis $\left\{\begin{bmatrix}-i\\1\end{bmatrix}\right\}$.
Geometrically $A=\sqrt{13}\,R(\theta)$ with $\theta=\operatorname{atan2}(3,2)\approx56.3^\circ$: rotate then scale by $\sqrt{13}$.

## Problem 13

**(a)** Rotation-scaling form with $a=-1,b=\sqrt3$: eigenvalues $\lambda=-1\pm\sqrt3\,i$. ($p(\lambda)=\lambda^2+2\lambda+4$.)

**(b)** $r=\sqrt{(-1)^2+(\sqrt3)^2}=2$; $\cos\theta=-1/2$, $\sin\theta=\sqrt3/2$ → $\theta=2\pi/3$. Thus
$$A=2\begin{bmatrix}\cos(2\pi/3)&-\sin(2\pi/3)\\\sin(2\pi/3)&\cos(2\pi/3)\end{bmatrix}=2\begin{bmatrix}-1/2&-\sqrt3/2\\\sqrt3/2&-1/2\end{bmatrix}\;\checkmark$$

**(c)** $\mathbf x\mapsto A\mathbf x$ rotates counterclockwise by $120^\circ$ and scales by $2$ (a similarity: angles preserved, no real invariant direction since $2\pi/3\neq0,\pi$).

## Problem 14

**(a)** Rotation-scaling with $a=0,b=2$: eigenvalues $\lambda=\pm2i$ ($p(\lambda)=\lambda^2+4$).

**(b)** $\lambda=2i$: basis $\{(i,1)\}$. $\lambda=-2i$: basis $\{(-i,1)\}$ (over $\mathbb{C}$).

**(c)** Not diagonalizable over $\mathbb{R}$ (eigenvalues are not real, no real eigenvectors; geometrically a $90^\circ$ rotation with no invariant real direction). Diagonalizable over $\mathbb{C}$: two distinct complex eigenvalues with independent eigenvectors, $P=\begin{bmatrix}i&-i\\1&1\end{bmatrix}$, $D=\operatorname{diag}(2i,-2i)$.

**(d)** $A^6=PD^6P^{-1}$; $(2i)^6=(-2i)^6=-64$, so $A^6=-64I=\begin{bmatrix}-64&0\\0&-64\end{bmatrix}$. Geometrically: scale by $2^6=64$ and rotate $6\times90^\circ=180^\circ$ → $-64I$.

## Problem 15

**(a)** Block diagonal: $\det(A-\lambda I)=\big[(2-\lambda)^2+1\big](4-\lambda)$, i.e. $p(\lambda)=(4-\lambda)(\lambda^2-4\lambda+5)$.

**(b)** Over $\mathbb{C}$: $\lambda=4$ and $\lambda=2\pm i$ (roots of $\lambda^2-4\lambda+5$).

**(c)** $\lambda=4$: basis $(0,0,1)$. $\lambda=2+i$: basis $(i,1,0)$ — check $A(i,1,0)^T=(2+i)(i,1,0)^T$. $\lambda=2-i$: basis $(-i,1,0)$.

**(d)** Not diagonalizable over $\mathbb{R}$ ($2\pm i$ are not real). Diagonalizable over $\mathbb{C}$: three distinct eigenvalues with three independent eigenvectors, $P_{\mathbb{C}}=\begin{bmatrix}0&i&-i\\0&1&1\\1&0&0\end{bmatrix}$, $D=\operatorname{diag}(4,2+i,2-i)$, $A=P_{\mathbb{C}}DP_{\mathbb{C}}^{-1}$.

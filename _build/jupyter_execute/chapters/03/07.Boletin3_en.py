#!/usr/bin/env python
# coding: utf-8

# # Bulletin III: Differential calculus of functions of a variable
# 
# ## Basic exercises
# 
# **<FONT SIZE=4>[1]</font>** Sea $f$ la función dada por $f(x)=5x^2.$
# 
# 1. Use the definition of the derivative to show that $f'(x)=10x.$
# 2. Calculate the equation of the tangent line to the graph of $f$ in $\displaystyle{x=\frac12}.$

# **<FONT SIZE=4>[2]</font>**
# Sea $f : \mathbb{R} \longrightarrow \mathbb{R}$ dada por:
# 
# $$
# f(x) =
# \begin{cases}
# 2x - 1             & \quad \text{si } x \leq -1 \\
# ( x+1)^3 + 2x & \quad \text{si } x > -1
# \end{cases}
# $$
# 
# Find out if it is differentiable at $x = -1$.

# **<FONT SIZE=4>[3]</font>**
# Let $f$ be the function given by
# 
# $$
# f(x)=
# \begin{cases}
# \displaystyle{x+x^2 \sin\left(\frac 1x\right)} & \text{  si  } x\neq 0 \\
# 0 & \text{  si  } x = 0
# \end{cases}
# $$
# 
# 1. Obtain the expression of $f'(x)$ for $x\neq 0$.
# 2. Calculate $f' (0)$ using the definition of derivative; that is, as a limit of the incremental quotient.
# 3. Check that the value obtained in section [3.2] does not coincide with the result of replacing $x$ with zero in the expression found in [3.1]. Reason why these different results occur.

# **<FONT SIZE=4>[4]</font>**
# Consider the function $f$ given by:
# 
# $$
# f(x) =
# \begin{cases}
# \displaystyle{\frac{1-e^{-x}}{x} }            & \quad \text{si } x \neq 0 \\
# 1 & \quad \text{si } x = 0
# \end{cases}
# $$
# 
# 1. Calculate $f'(x)$ at all points where it exists.
# 2. Calcula $\displaystyle{\lim _{x\rightarrow -\infty}{f(x)}}$, $\displaystyle{\lim _{x\rightarrow \infty}{f(x)}}$ y el conjunto $\textrm{Im}(f)$.
# 
# 

# **<FONT SIZE=4>[5]</font>**
# Write the Newton-Raphson method to approximate $\sqrt[3]{2}$ starting from $x_0 = 1$. Calculate the first two iterants.
# 

# **<FONT SIZE=4>[6]</font>**
# To approximate the value of the solution of the equation $x^3+2x-2=0,$ in the interval $[-2,\, 2],$ we are going to use the Newton-Raphson method.
# 
# 1. State the Newton-Raphson algorithm for this case.
# 2. Calculate the first two iterations using that algorithm. To do this, use the value $x_0=0$ as an initial approximation.
# 
# 

# **<FONT SIZE=4>[7]</font>**
# Let $f(x) = \displaystyle \arctan \left( \frac{\sin (x)}{1 + \cos (x)} \right )$. Calculate the tangent line to the graph of $f$ at $x = 0$.
# 
# 

# **<FONT SIZE=4>[8]</font>**
# Let the function $f$ be given by $f(x) = (4x+1)^{(2+ \sin (x^2))}$. Calculate its derivative at any point.
# 
# 

# **<FONT SIZE=4>[9]</font>**
# If we consider the function $f:\mathbb{R}\rightarrow \mathbb{R}$ given by
# 
# $$
# f(x)=\displaystyle{\left\{ \begin{array}{ccl}
# judisplaystyle{yufrac{yusin^2(zx)}{zx^2}} & si & hyunea 0 yuu
# \\
# \displaystyle{\frac13 }& si & x=0
# \end{array}
# \right. },
# $$
# choose the correct option:
# 
# 1. $\displaystyle\lim _{x\rightarrow 0}f(x)=\frac{1}{3} $.
# 2. Cannot calculate $\displaystyle{\lim _{x\rightarrow 0}{f(x)}}$.
# 3. $\displaystyle{\lim _{x\rightarrow 0}{f(x)}}=3$.
# 4. It is continuous in $\mathbb{R}$

# **<FONT SIZE=4>[10]</font>**
# Calculate the values ​​of $a$ and $b$ so that
# 
# $$
# \displaystyle{\lim_{x\rightarrow 0}\frac{ax^2+bx+1-e^{2x}}{\sin(x^2)}=1}
# $$
# 
# 

# **<FONT SIZE=4>[11]</font>**
# Let the function $f$ be given by $\displaystyle f(x) = \frac{1}{2} x |x|$. What is the class of $f$?
# 
# 

# **<FONT SIZE=4>[12]</font>** We consider the function $f$ given by
# 
# $$
# f(x) =
# \begin{cases}
# \sin (x) \, \qquad \text{ si } x \in (-\infty,0) \\
# \arctan (x) \,\qquad \text{ si } x \in [0,1] \\
# \pi x^3 / 4 \, \qquad \text{ si } x \in (1,+\infty)
# \end{cases}
# $$
# 1. Sketch the graphical representation of $f$.
# 2. Determine the class of $f$ in $\mathbb{R}$.
# 3. Calculate, if possible, the tangent line to $f$ at the point $x_0 = 0$.
# 4. Determine a set of real numbers in which $f$ is of class infinite.
# 
# 

# **<FONT SIZE=4>[13]</font>**
# Let $f$ be the function given by
# 
# $$
# f(x) =
# \begin{cases}
# \sqrt{x} + 1    & \quad  \text{si } x \in (0,1) \\
# \alpha x^2 + \beta x + 1   & \quad  \text{si } x \in [1,2)
# \end{cases}
# $$
# 
# 1. Determine $\alpha$ and $\beta$ so that $f$ is differentiable in $(0,2)$.
# 2. What conditions must $\alpha$ and $\beta$ satisfy so that $f$ has a relative minimum at the point $x=1$?
# 
# 

# **<FONT SIZE=4>[14]</font>**
# Calculates the relative and absolute extremes if they exist, of the function defined in the
# intervalo $\left [ -\frac{1}{2} , \frac{3}{2} \right ]$ por $f(x) = x^2 - 2|x| + 2$.
# 
# 

# **<FONT SIZE=4>[15]</font>**
# Consider the function $f:\mathbb{R} \rightarrow \mathbb{R}$ given by $\displaystyle{f(x)=\frac{|x|}{e^{x-1}}}$.
# 
# 1. Study the continuity and differentiability of the function.
# 2. Sketch the graph of $f$. To do this, it calculates their relative extremes, inflection points and asymptotes. Also determine its interval(s) of concavity and/or convexity.
# 3. Determine the absolute extremes of $f$.
# 
# 

# **<FONT SIZE=4>[16]</font>**
# Show that the equation $x^4-4\,x^3-1=0$ has a single root in the interval $[4,5]$.
# Pose the Newton-Raphson method to solve the equation from the previous section. Starting from $x_0=4$, obtain the approximation $x_1$ by hand and the approximation $x_7$ using `Python`.
# 

# **<FONT SIZE=4>[17]</font>**
# On what interval is the function $f$ given by $f(x)=x^3e^x$ increasing? Is it concave or convex in that interval? Sketch your graph.
# 

# **<FONT SIZE=4>[18]</font>**
# Find the condition that $\lambda$ must satisfy for the polynomial $x^4 + x^3 + \lambda x^2$ to be concave on some interval. Determine that interval based on $\lambda$.

# **<FONT SIZE=4>[19]</font>**
# Find a cubic polynomial without local extrema but with an inflection point and a horizontal tangent at $P=(1,\, 20)$.
# 

# **<FONT SIZE=4>[20]</font>**
# Sketch the graph of a function whose slope is always positive and increasing. Do you know of any elementary function that is an example of this situation? <br> Sketch the graph of a function whose slope is always positive and decreasing. Do you know of any elementary function that is an example of this situation?
# 

# **<FONT SIZE=4>[21]</font>**
# A rectangle whose base is on the abscissa axis has its two upper vertices in the parabola $y = 12 - x^2$. What is the largest area that this rectangle can have? Indicate its dimensions.
# 
# 

# **<FONT SIZE=4>[22]</font>**
# Knowing that $p(x)=5+(x+1)^2+3(x+1)^3$ is the third-order Taylor polynomial centered at $x_0=-1$ of a function $f,$ calculate $f(-1),$ $f^\prime (-1)$ and $f^{\prime \prime}(-1).$ Justify your answer.
# 

# **<FONT SIZE=4>[23]</font>**
# We consider the function $f$ defined by $f(x)=\ln(1+x)$.
# 
# 1. Calculate the McLaurin polynomial (i.e., the Taylor polynomial with $x_0=0$) of order two relative to $f$.
# 2. Use this polynomial to approximate the value of $\ln(1.1)$, limiting the error made.
# 

# **<FONT SIZE=4>[24]</font>**
# Construct the first-order Taylor polynomial, $p$, for the function $g(x) = \sin (x)$, centered at the point $x_0 = \pi/2$.
# 
# Now consider the function $f$ defined as follows:
# 
# $$
# f(x) =
# \begin{cases} \sin (x) \quad  & \quad \quad \text{si } x \leq \pi/2 \\
# p(x) \quad    & \quad \quad \text{si } x > \pi/2
# \end{cases}
# $$
# $p$ being the polynomial constructed in the previous section. What is the class of $f$ in $\mathbb{R}$?
# 

# **<FONT SIZE=4>[25]</font>**
# Determine the Taylor polynomial of order two of the function $f(x)= \arcsin(x)$ relative to the point $x_{0}=0$. <br> Use the previous polynomial to obtain, approximately, the angle whose sine is $\frac{1}{10}$.
# 

# **<FONT SIZE=4>[26]</font>**
# Let the function given by
# 
# $$
# \begin{array}{cccl}
# f: & \mathcal{D}om(f) \subset \mathbb{R} & \longrightarrow & \mathbb{R} \\
# &        x                    & \rightsquigarrow & f(x) = \dfrac{x^2}{e^x}
# \end{array}
# $$
# 
# 1. Calculate the domain of $f.$
# 2. Calculate the absolute extremes of $f$ in the interval $[0,10]$, previously justifying its existence.
# 3. Find the absolute extrema of $f$ in its domain.

# 

# ## Complementary exercises
# 
# **<font SIZE=4>[1 C]</font>**
# If the tangent line to the graph of the function $y = f(x)$ at the point $(4,3)$
# passes through the point $(0,2)$, calculates the value of the function $f$ and its derivative at the point whose
# abscissa is $x = 4$.
# 
# 
# 

# **<font SIZE=4>[2 C]</font>**
# Approximate the solution of $x^3 - x - 1 = 0$ in $[1.3,\, 1.4]$ using the Newton-Raphson method, starting from $x_0 = 1$ and performing three iterations.
# 
# 

# **<font SIZE=4>[3 C]</font>**
# Find the numbers $a$ and $b$ such that $\,\,\displaystyle{\lim _{x\rightarrow 0}{\frac{\sqrt{ax+b}-2}{x}}=1}. $
# 
# 

# **<font SIZE=4>[4 C]</font>**
# Calculate the limit:
# 
# $$
# \displaystyle{\lim_{x\rightarrow 0} \dfrac{(1+x)^{\frac{1}{x}} - e}{x}.}
# $$
# 
# 

# **<font SIZE=4>[5 C]</font>**
# We consider the function $f: \mathbb{R} \longrightarrow \mathbb{R}$ given by:
# 
# $$
# f(x)=
# \begin{cases}
# \displaystyle{\dfrac{1-\cos (x)}{x^2}} & \text{  si  } x\neq 0 \\
# \lambda  & \text{  si  } x = 0
# \end{cases}
# $$
# 
# 1. Calculate the value of $\lambda$ for which $f$ is differentiable at $x=0$.
# 2. Calculate $f^{\prime \prime}(0)$ for the value of $\lambda$ found in the previous section.
# 
# 

# **<font SIZE=4>[6 C]</font>**
# Let $f:\mathbb{R}\to \mathbb{R}$ defined as $f(x) =
# \begin{cases}
# \displaystyle 1 - \frac{x^2}{2} & \text{ si } x < 0 \\
# \cos (x) & \text{ si } x \geq 0
# \end{cases}
# $. <br> How many times is $f$ differentiable at $x_{0}=0$?
# 
# 

# **<font SIZE=4>[7 C]</font>**
# Check that the function $F$, given by $F(x) = \dfrac{1}{4} x^2 - \ln x$, has a relative minimum, $x_{\min}$, in the interval $ (1.3)$.
# Use the dichotomy algorithm, starting from $a = 1$ and $b = 3$, to approximate $x_{\min}$ with an error less than $\frac{1}{7}$.
# 
# 

# **<font SIZE=4>[8 C]</font>**
# We consider the equation \, $x e^{-x} = e^{-3}$.
# 
# 1. Check that you have exactly two solutions in $\mathbb{R}$.
# 2. Establish the Newton-Raphson method starting from a point in the interval $[2,5]$. Calculate $x_2$ from $x_0 = 2$.
# 
# 

# **<font SIZE=4>[9 C]</font>**
# We wish to construct an arc that describes the curve given by $f(x) = \sqrt{1-x^2}$. To facilitate construction, it is proposed to approximate said function by a second-order Taylor polynomial centered on $a = 0$. Calculate said polynomial and approximate $f(1)$.
# 
# 

# **<font SIZE=4>[10 C]</font>**
# During coughing, the diameter of the trachea decreases. The velocity $v$ of the air in the trachea during cough is related to the radius, $r,$ by the equation:
# 
# $$
# v = Ar^2 (r_0-r) \quad , \qquad A > 0
# $$
# where $r_0$ is the radius in the relaxed state.
# 
# 1. Find the radius of the trachea when the speed is maximum, as well as this speed.
# 2. Justifies the existence of a minimum. calculate it
# 
# 

# **<font SIZE=4>[11 C]</font>**
# Find the radius and height of a cylindrical soda can.
# $33$ cm$^3$ that minimizes the amount of material used for its construction (assume that the thickness of the material used is uniform throughout the can and negligible).
# 
# 

# **<font SIZE=4>[12 C]</font>**
# Let the real function $f$ be given by:
# 
# $$
# f(x) =
# \begin{cases} \frac{\sin( x)}{x} - 1 \quad and \quad \quad \text{si } x < 0 \\ & \\
# x^3 e^{-x^2} \quad           & \quad \quad \text{si } x \geq 0 \, .
# \end{cases}
# $$
# 
# 1. Study the differentiability of $f$ in $\mathbb{R}$.
# 2. Calculate the second-order Taylor polynomial of the function $f$ in the neighborhood of $x_0 = 1$.
# 3. Reasonably determine the absolute extremes of $f$ in $[0,+\infty)$.
# 

# **<font SIZE=4>[13 C]</font>**
# Let the function $f$ be given by:
# 
# $$
# f(x) =
# \begin{cases} \dfrac{\sin (x)}{x} \, & \quad \quad \text{si } x < 0 \\
# 2 - \cos(x) \,        & \quad \quad \text{si } x \geq 0 \, .
# \end{cases}
# $$
# 
# 1. Study the continuity of $f$ in $\mathbb{R}$.
# 2. Determine, if $f'(0)$ exists. If so, reason whether $f$ is of class one in $\mathbb{R}$.
# 3. Calculate the second degree Taylor polynomial of $f$ in $x = -\pi$.
# 

# **<font SIZE=4>[14 C]</font>**
# We call $f(x) = \sqrt{x+1}$.
# 
# 1. Find the fourth-order Taylor polynomial of $f$ at $x = 0$.
# 2. Approximate $\sqrt{1.02}$ with the Taylor polynomial of the second degree and limit the error made.

# **<font SIZE=4>[15 C]</font>**
# Obtain the McLaurin polynomial (Taylor, with $x_{0}=0$) of order less than or equal to $n$ relative to $f(x) = (1-x)^{\alpha}$, with $\ alpha \in \mathbb{R}$.
# 
# 

# **<font SIZE=4>[16 C]</font>**
# Construct the Taylor polynomial of degree less than or equal to $3$ for the function $f(x)=x^2 - 2x + 1$ in a neighborhood of the point $x_{0} = 1$.
# 

# **<font SIZE=4>[17 C]</font>**
# Determine the absolute extrema of the function $f(x)=|16-x^2|$ in the interval $[-5,8]$.
# 

# **<font SIZE=4>[18 C]</font>**
# We want to approximate a root of the equation $x^3 -x^2 + 2 = 0$.
# 
# 1. Justify the existence of roots of the function $f$ given by $f(x)=x^3 -x^2 + 2$ in the interval $[-2,3]$.
# 2. Starting from $x_0=2$, calculate, using Newton's algorithm, $x_1$. Use two correct decimal places in your calculations.

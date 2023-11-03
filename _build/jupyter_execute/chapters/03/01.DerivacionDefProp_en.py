#!/usr/bin/env python
# coding: utf-8

# # Definition of derivative and basic properties
# 
# ## Definition of derivative
# 
# Let's introduce this new concept through an example. For this we copy
# Galileo's famous experiment on the Tower of Pisa and we ask ourselves:
# 
# Suppose we drop a ball from the top of a building.
# $300$ m. What will be the speed of the ball after 5 seconds?
# 
# Galileo concluded that the space traveled is directly proportional
# squared of the elapsed time, according to the formula
# 
# $$
# s(t)=4.9 t^2,
# $$
# 
# formula that is very close to reality... as long as we neglect friction
# exerted by the air.
# 
# So how do we find the speed at $t=5$ seconds? We can make a
# average speed:
# 
# $$
# \begin{array}{rcl}
# \test{Average speed} &=& \dfrac{\text{distance traveled}}
# {\text{elapsed time}}, \\
# && \\
# v(5)\approx \dfrac{s(5.1)-s(5)}{0.1} &=& \dfrac{4.9(5.1)^2-4.9\, 5^2}{0.1}
# =49.49\; m/s,
# \end{array}
# $$
# 
# or, better yet,
# 
# $$
# v(5)\approx \frac{s(5.01)-s(5)}{0.01}=\frac{4.9(5.01)^2-4.9(5)^2}{0.01}
# =49.049\; m/s.
# $$
# 
# Really, what we are doing is approximating the slope of the tangent line
# to the function $s$ at the point $t=5$.
# Let us remember, first of all, that the **slope** of a line is the tangent of the
# angle it forms with the $OX$ axis, as shown in the following figure:
# 
# <img src="../../images/cap_deriv_pendiente_recta.png" width="400"/>
# 
# 

# If now we want to calculate the slope of the tangent line to a function $f$
# at a point $x_0$, what we will do is calculate the slopes of the lines
# secants to $f$ by two nearby points, $x_0$ and $x$, and make $x$
# approach $x_0$ (i.e., take the *limit when $x\to x_0$*). The
# Graphic illustration of this process is shown in the following figure
# (with which, by the way, you can play at the following link: https://www.desmos.com/calculator/piskepauzm):
# 
# <img src="../../images/cap_deriv_definicion_derivada.png" width="400"/>
# 
# ````{prf:definition} 
# :label: def_derivada
# :nonumber: 
# 
# Sea $f:(a,b)\rightarrow\mathbb{R}$, $x_0\in(a,b)$. Definimos la **derivada de $f$ en $x_0$**
# como el límite, si existe,
# 
# $$
# f'(x_0):=\lim_{x\to x_0}\dfrac{f(x)-f(x_0)}{x-x_0}=\lim_{h\to 0}\dfrac{f(x_0+h)-f(x_0)}{h}.
# $$
# 
# ````
# ````{prf:remark} 
# :label: remark_derivada
# :nonumber: 
# 
# 1. Aquí ya vemos la utilidad de no incluir el punto $x_0$ (en este caso, 
# el punto $h=0$) en la definición de límite. En la expresión 
# $\displaystyle\lim_{h\to 0}\frac{f(x_0+h)-f(x_0)}{h}$ no podemos hacer nada si 
# $h=0$, ya que tendríamos una división entre $0$. Pero, afortunadamente, 
# justo el punto $h=0$ no se incluye en la definición de límite (recordemos eso 
# de $0<|h-0|<\delta$...).
# 
# 2. El cociente $\frac{f(x)-f(x_0)}{x-x_0}$ mide la variación de la función 
# respecto a la variación de la variable. Por ese motivo a $f'(x_0)$ se le denomina, 
# en ocasiones, coeficiente de variación de $f$, o razón de cambio de la función 
# $f$, en el punto $x_0$. 
# 
#     Es decir, la derivada de una función en un punto indica la variación instantánea 
#     de la función en ese punto. Por ejemplo, la aceleración, que es la variación de 
#     velocidad, se escribe matemáticamente como $\frac{dv}{dx}$, es decir, 
#     la derivada de la velocidad respecto al tiempo. 
# 
#     Que la derivada sea la variación instantánea de una variable dependiente, 
#     $y$, respecto a otra variable independiente, $x$, será fundamental cuando
#     veamos los modelos matemáticos en ecuaciones diferenciales.
# 
# 3. Ahora ya podemos calcular la ecuación de la recta tangente utilizando la
# fórmula punto-pendiente,
# 
#     $$
#     y-y_{0}=m\left(x-x_{0}\right) \Longrightarrow y=y_{0}+m\left(x-x_{0}\right).
#     $$ 
# 
#     En este caso, $\left(x_{0},y_{0}\right)=\left(x_{0},f\left(x_{0}\right)\right)$, 
#     $m=f'\left(x_{0}\right)$. Y la recta tangente,
# 
#     $$
#     y=f\left(x_{0}\right)+f'\left(x_{0}\right)\left(x-x_{0}\right).
#     $$
# 
# ````
# 
# 

# ## Lateral derivatives
# 
# Now, since we are defining the derivative as a limit, we can talk about derivative
# on the left and derivative on the right.
# 
# ````{prf:definition} Derivadas laterales
# :label: def_derivadas_laterales
# :nonumber: 
# 
# Sea $f:(a,b)\rightarrow\mathbb{R}$, $x_0\in(a,b)$. Definimos
# 
# * **derivada por la izquierda** de $f$ en $x_0$ como
# 
#     $$
#     f'(x_0^{-}):=\lim_{h\to 0^{-}}\frac{f(x_0+h)-f(x_0)}{h},
#     $$
# 
# * **derivada por la derecha** de $f$ en $x_0$ como
# 
# $$
# f'(x_0^{+}):=\lim_{h\to 0^{+}}\frac{f(x_0+h)-f(x_0)}{h}.
# $$
# 
# ````
# ````{prf:property} 
# :label: prop_derivadas_laterales
# :nonumber: 
# 
# Sea $f:(a,b)\rightarrow\mathbb{R}$, $x_0\in(a,b)$. $f$ es derivable en $x_0$ si y sólo si es
# derivable por la izquierda y por la derecha en $x_0$ y ambas derivadas coinciden.
# ````
# 
# The most typical **example** of a non-differentiable function is the
# absolute value function, which is not differentiable at $0$. Let's see it, calculating its
# partial derivatives. Let us remember that
# 
# $$
# |x|=\left\{\begin{array}{ll}
# -x &\quad \mbox{si }x<0, \\
# x &\quad\mbox{si }x\geq 0.
# \end{array}\right.
# $$
# 
# So,
# 
# \begin{eqnarray*}
# &&f'\left(0^{-}\right)=\lim_{h\to 0^{-}}\frac{|h|-|0|}{h}=\lim_{h\to 0^{-}}\frac{-h}{h}=-1, \\
# &&f'\left(0^{+}\right)=\lim_{h\to 0^{+}}\frac{|h|-|0|}{h}=\lim_{h\to 0^{+}}\frac{h}{h}=1.
# \end{eqnarray*}
# 
# Then $f'\left(0^{-}\right)\not=f'\left(0^{+}\right)$, so the absolute value function is not
# derivable in $0$.
# 
# Graphically, we can realize what is happening if we remember the graph of the
# absolute value function:
# 
# <img src="../../images/cap_deriv_valor_absoluto.png" width="400"/>
# 
# The point $x=0$ is an angular point for
# this curve, that is, a point at which the slope of the curve varies abruptly.
# It goes from being $-1$ to the left of $0$ to being $1$ to its right. When this occurs
# sudden variation the function cannot be differentiable at $0$.
# 
# Here you can see **another complete example**:
# * https://existelimite.blogspot.com/2013/02/derivabilidad-de-una-funcion-definida.html.

# ## Derivation properties
# 
# Let us now look at some important properties of the derived function.
# 
# ````{prf:property}  
# :label: prop_derivable_continua
# :nonumber: 
# 
# Sea $f(a,b)\rightarrow\mathbb{R}$, $x_0\in\mathbb{R}$. Si $f$ es derivable en $x_0$, entonces $f$ es
# continua en $x_0$.
# ````
# 
# This property can be summarized as
# 
# $$
# \mathrm{derivable}\,\Rightarrow\, \mathrm{continua}.
# $$
# 
# It is advisable to know how to read it correctly. According to the logical relationship
# 
# $$
# \left[\textrm{a}\Rightarrow\textrm{b}\right]\Leftrightarrow\left[\textrm{no b}\Rightarrow\textrm{no a}\right],
# $$
# 
# This property is the same as
# 
# $$
# f \mbox{ not continuous in } x_0\Rightarrow f \mbox{ not differentiable in }x_0.
# $$
# 
# This is the most common form of application. If you ask us if certain
# function is differentiable at some point, the first thing we must do is check if it is
# keep going. If indeed it is, we must check whether the definition of
# derived, but if it is not continuous we will have already finished, because in that case it cannot be
# derivable.
# 
# ````{prf:property}  Derivadas elementales
# :label: prop_derivadas_elementales
# :nonumber: 
# 
# 1. $\displaystyle \dfrac{d}{dx} \left(x^{n}\right) = nx^{n-1}$,
# 2. $\displaystyle \dfrac{d}{dx} \left(\ln x\right) = \dfrac{1}{x}$, 
#    
#    $\displaystyle  \dfrac{d}{dx} \left(\log_{a}x\right) = \dfrac{1}{x}\log_{a} e$,
# 3. $\displaystyle \dfrac{d}{dx} \left(e^x\right) = e^x$,
#    
#     $\displaystyle \dfrac{d}{dx} \left(a^x\right) = a^x\ln a$,
# 4. $\displaystyle \dfrac{d}{dx} \left(\sin x\right) = \cos x$,
#    
#    $\displaystyle \dfrac{d}{dx} \left(\cos x\right) = -\sin x$,
# 5. $\displaystyle  \dfrac{d}{dx} \left(\tan x\right) = \dfrac{1}{\cos^2 x}$,
# 6. $\displaystyle \dfrac{d}{dx} \left(\arcsin x\right) = \dfrac{1}{\sqrt{1-x^2}}$, 
#    
#     $\displaystyle \dfrac{d}{dx} \left(\arccos x\right) = \dfrac{-1}{\sqrt{1-x^2}}$,
# 7.  $\displaystyle \dfrac{d}{dx} \left(\arctan x\right) = \dfrac{1}{1+x^2}$.
# 
# ````
# 
# ````{prf:property} Propiedades aritméticas de la derivada 
# :label: prop_aritmetica_derivada
# :nonumber: 
# 
# Sean $f,g:(a,b)\rightarrow\mathbb{R}$, dos funciones derivables en un punto $x_0\in(a,b)$. Entonces
# 
# 1. para cualquier $\lambda\in\mathbb{R}$, la función $\lambda f$ es derivable en $x_0$ y 
# 
#     $$
#     \left(\lambda f\right)'(x_0)=\lambda f'(x_0),
#     $$
# 
# 2. $f\pm g$ es derivable en $x_0$ y 
# 
#     $$
#     \left(f\pm g\right)'(x_0)=f'(x_0)\pm g'(x_0),
#     $$
# 
# 3. $fg$ es derivable en $x_0$ y 
# 
#     $$
#     \left(fg\right)'(x_0)=f'(x_0)g(x_0)+f(x_0)g'(x_0),
#     $$
# 
# 4. si $g(x_0)\not= 0$, entonces $\dfrac{f}{g}$ es derivable en $x_0$ y 
# 
#     $$
#     \left(\frac{f}{g}\right)'(x_0)=\frac{f'(x_0)g(x_0)-f(x_0)g'(x_0)}{g(x_0)^2}.
#     $$
# 
# ````
# 
# ````{prf:property} Regla de la cadena 
# :label: prop_regla_cadena
# :nonumber: 
# 
# Consideramos las funciones $f:(a,b)\rightarrow\mathbb{R}$, derivable en $x_0\in(a,b)$, y
# $g:f(a,b)\to\mathbb{R}$, derivable en $f(x_0)$. Entonces la función composición $g\circ f$ es
# derivable en $x_0$ y además
# 
# $$
# \left(g\circ f\right)'(x_0)=g'\left(f(x_0)\right)f'(x_0).
# $$
# 
# ````
# 
# Let's look at some examples of the application of these rules:
# 
# 1. Derivar $\ln\left(\cos x\right)$.
# 
# The result is
# 
# $$
# \left(\ln\left(\cos x\right)\right)'=\frac{1}{\cos x}\left(\cos x\right)'=\frac{-\sin x}{\cos x}.
# $$
# 
# Let's think about what we have done:
# 
# We are composing the function $f(x)=\cos x$ with
# $g(x)=\ln x$. This is easy to check, since
# 
# $$
# \left(g\circ f\right)(x)=g\left(f(x)\right)=g\left(\cos x\right)=\ln\left(\cos x\right).
# $$
# 
# So according to the chain rule, $\left(g\circ f\right)'(x)=g'\left(f(x)\right)f'(x)$.
# 
# Now, $f'(x)=-\sin x$ and $g'(x)=\frac{1}{x}$, so $g'(\cos x)=\frac{1}{ \cos x}$, which
# allows us to obtain the announced result.
# 
# 2. Let's look at a slightly more complicated application example.
# 
# \begin{eqnarray*}
# \left(\textrm{atan}\left(\frac{\sin x}{1+\cos x}\right)\right)'&=&\frac{1}{1+\frac{\sin^2 x}{\left(1+\cos
# x\right)^2}} \frac{\left(\cos x\right)\left(1+\cos x\right)+\sin^2 x}{\left(1+\cos x\right)^2}=\\
# &=&\frac{\cos x\cos^2x\sin^2x}{\left(1+\cos x\right)^2+\sin^2 x}
# =\frac{1+\cos x}{1+\cos^2 x+2\cos x+\sin^2 x}= \\
# &=&\frac{1+\cos x}{2+2\cos x}=\frac{1}{2},
# \end{eqnarray*}
# 
# where we have used twice that $\sin^2 x+\cos^2 x=1$.
# 
# 

# ## Derivation in **Sympy**
# 
# To symbolically calculate the first derivative of a function using Sympy, the *diff* function is used. For example

# In[1]:


import sympy as sp
x=sp.symbols('x')
f_exp=sp.exp(x)*sp.cos(x)
d1f_exp=sp.diff(f_exp,x)
print('Para la función: ',f_exp)
print('La derivada primera es: ',d1f_exp)


# ## Derivation of some special cases.
# 
# ### Derivation of the inverse function.
# 
# For example, $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$. Suppose that $f$ is derivable at $x_0$ and that $f(x_0)\not=0$.
# Then $f^{-1}$, if it exists, is differentiable and
# 
# $$
# \left(f^{-1}\right)'\left(f(x_0)\right)=\frac{1}{f'(x_0)},
# $$
# 
# Or what is the same,
# 
# $$
# \left(f^{-1}\right)'\left(y_0\right)=\frac{1}{f'\left(f^{-1}(y_0)\right)}.
# $$
# 
# Let's highlight that we are relating the derivative of the inverse function with $1$ split
# by the derivative of the inverse function. This is quite surprising, because at these
# heights we must already know that $f^{-1}\not=\frac{1}{f}$.
# 
# Let's look at an **example**. If we consider the function $y=f(x)=\cos x$, the function
# inverse is the arc-cosine, $f^{-1}(y)=\arccos y$. Deriving directly,
# 
# $$
# \left(f^{-1}\right)'(y)=\left(\arccos\, y\right)'=-\frac{1}{\sqrt{1-y^2}}.
# $$
# 
# Let's see if this expression matches the one we obtain by applying the formula
# that we explained at the beginning. In this case
# 
# $$
# \left(f^{-1}\right)'\left(f(x)\right)=\frac{1}{f'(x)}=-\frac{1}{\sin x}=-\frac{1}{\sqrt{1-\cos^2
# x}}=-\frac{1}{\sqrt{1-y^2}},
# $$
# 
# where, in the last equality, we have used the initial definition of the function: $y= f(x)=\cos x$.
# 
# ### Implicit derivation
# 
# An implicit equation is an equation of the form
# 
# $$
# F(x,y)=0,
# $$
# 
# that is, an equation where $x$ and $y$ appear mixed and where it is not possible
# (usually) separate the $y$ to arrive at an explicit equation,
# 
# $$
# y=f(x).
# $$
# 
# An example of an implicit equation would be
# 
# $$
# \cos(xy)+xy^2=0.
# $$
# 
# If from an implicit equation we want to know the value of the derivative of $y$
# with respect to $x$, $y'=\frac{dy}{dx},$ we will differentiate term by term, using the
# usual rules of derivation, but taking into account that in the terms where
# $y$, or something that depends on $y$, appears when differentiating using the chain rule
# we will obtain the corresponding expression multiplied by $y'$. This does not happen if the
# term depends on $x$, since when we differentiate with respect to $x$ the derivative would appear
# of $x$ with respect to the same $x$, $\frac{dx}{dx}$, which is $1$. Let's see some example
# simple:
# 
# * $\displaystyle \left(x^3\right)'=3x^2\frac{dx}{dx}=3x^2$,
# * $\displaystyle \left(y^3\right)'=3y^2\frac{dy}{dx}=3y^2y'$,
# * $\displaystyle \left(cos(2y)\right)=-\sin(2y)2\frac{dy}{dx}=-2\sin(2y)y'$.
# 
# Then, in a more complicated derivative (using the derivation rule of
# product),
# 
# \begin{eqnarray*}
# \cos(xy)+xy^2=0&\stackrel{\mathrm{derivando}}{\Rightarrow}
# &-\sin(xy)\left(y+xy'\right)+y^2+2xyy'=0 \\
# x\Rightarrow y'\Big(2xy-x\sin(xy)\Big)=y\sin(xy)\Rightarrow
# y'=\frac{y\sin(xy)}{2xy-x\sin(xy)}.
# \end{eqnarray*}
# 
# As we can see, the final result is the value of $y'$ as a function of $x$ and $y$.
# It is generally not possible to obtain the value of $y'$ solely as a function of $x$.
# 
# You can look at the following links, if you want to understand this better:
# * https://es.wikipedia.org/wiki/Funci%C3%B3n_impl%C3%ADcita
# * https://www.fisicalab.com/apartado/derivacion-implicita
# * https://es.snapxam.com/calculators/calculadora-derivacion-implicita (Calculator to derive implicit functions! If there is everything on the internet...)
# * https://es.khanacademy.org/math/ap-calculus-ab/ab-differentiation-2-new/ab-3-2/a/implicit-differentiation-review
# 
# ### Logarithmic derivation
# 
# Suppose we have an expression of the type
# 
# $$
# y=f(x)^{g(x)}
# $$
# and we want to derive it. Since we have a function that depends on $x$ both in the base and
# In the exponent we cannot do it directly. Then we apply logarithms and of the
# previous expression results
# 
# $$
# \ln y=\ln\left(f(x)^{g(x)}\right)\Rightarrow\ln y=g(x)\ln\left(f(x)\right),
# $$
# and now we do an implicit derivation to obtain
# 
# \begin{eqnarray*}
# &&\frac{1}{y}y'=g'(x)\ln\left(f(x)\right)+g(x)\frac{1}{f(x)}f'(x)\Rightarrow
# y'=y\left(g'(x)\ln\left(f(x)\right)+\frac{g(x)f'(x)}{f(x)}\right) \\
# &&\Rightarrow y'=f(x)^{g(x)}\left(g'(x)\ln\left(f(x)\right)+\frac{g(x)f'(x)}{f(x)}\right).
# \end{eqnarray*}
# 
# Let's look at it on an **example**:
# 
# \begin{eqnarray*}
# y=\left(x^3-5\right)^{\sin x}&\stackrel{\mathrm{(logaritmos)}}{\Rightarrow}&\ln
# y=\sin(x)\ln\left(x^3-5\right) \\
# &\stackrel{\mathrm{(derivamos)}}{\Rightarrow}&\frac{1}{y}y'=\cos(x)\ln\left(x^3-5\right)+\frac{
# \sin(x)3x^2}{x^3-5} \\
# x\Rightarrow y'=y\left(\cos(x)\ln\left(x^3-5\right)+\frac{\sin(x)3x^2}{x^3-5}\right) \\
# x\Rightarrow y'=\left(x^3-5\right)^{\sin(x)}\left(\cos(x)\ln\left(x^3-5\right)+\frac{\sin(x)3x^2}{x^3-5}\right).
# \end{eqnarray*}
# 
# Here you have more information and other examples:
# * https://lasmatematicas.eu/derivacion-logaritmica/
# * https://es.snapxam.com/calculators/calculadora-diferenciacion-logaritmica

# ## Hospital regulations
# 
# <img src="../../images/cap3_lHopital_meme.jpg" width="400"/>
# 
# (Image taken from the Twitter account @MathMatize, specifically from https://twitter.com/MathMatize/status/1678166772359348225)
# 
# We still have one point left that we must resolve:
# When we apply the arithmetic properties of limits we can find an *unpleasant* surprise if any of the parties involved have a limit of $+\infty$ or $-\infty$.
# For example, if we remember that $\displaystyle\lim _{x\to x_{0}} \left(f(x)+g(x)\right) = \lim _{x\to x_{0}} f(x ) + \lim _{x\to x_{0}} g(x)$, if we now assume that $\displaystyle\lim _{x\to x_{0}} f(x) = 4$, and $\displaystyle\ lim_{x\to x_{0}} g(x) = + \infty$, how do we add $4$ and $+\infty$?
# 
# There are some rules that help us do these operations with limits where + or -$\infty$ appears or, also, at $0$ (sometimes this is called **infinity arithmetic**). You can look at the table here: http://asignaturas.topografia.upm.es/matematicas/primero/Apuntes/Funciones/Operaciones%20con%20limites%20infinitos.pdf, we summarize it below:
# 
# ````{prf:property} Operaciones con límites infinitos
# :label: prop_aritmetica_infinito
# :nonumber: 
# 
# * Suma:
#   * $\lambda + \infty = +\infty$, $\forall \lambda\in\mathbb{R}$,
#   * $\lambda - \infty = -\infty$, $\forall \lambda\in\mathbb{R}$,
#   * $+\infty+\infty = +\infty$,
#   * $-\infty-\infty=-\infty$.
# * Multiplicación:
#   * $\lambda*\pm\infty=\pm\infty$, $\forall \lambda >0$,
# 
#       $\lambda*\pm\infty=\mp\infty$, $\forall \lambda <0$,
#   * $(+\infty)(+\infty) = (-\infty)(-\infty) = +\infty$, 
#     
#       $(+\infty)(-\infty) = (-\infty)(+\infty) = -\infty$. 
# * División:
#   * $\displaystyle\frac{\lambda}{\pm\infty} = 0$, $\forall \lambda\in\mathbb{R}$, $\lambda\neq 0$,
#   * $\displaystyle\frac{\lambda}{0^{+}} = +\infty$, $\displaystyle\frac{\lambda}{0^{-}} = -\infty$, $\forall \lambda > 0$,
#     
#     $\displaystyle\frac{\lambda}{0^{+}} = -\infty$, $\displaystyle\frac{\lambda}{0^{-}} = +\infty$, $\forall \lambda < 0$,
#   * $\displaystyle\frac{+\infty}{0^{+}}=+\infty$ (en otros casos, se aplica la regla de los signos),
#   * $\displaystyle\frac{0}{\pm\infty}=0$.
#   
#   [**Nota**: Diremos que $\displaystyle\lim_{x\to x_0} f(x) = 0^{+}$ si la función se acerca a $0$ por valores positivos, es decir, desde la derecha.]
# * Potencias:
#   * $\displaystyle 0^{+\infty} = 0$,
#   
#     $\displaystyle 0^{-\infty} = +\infty$,
#   * $\displaystyle\left(+\infty\right)^{+\infty} = +\infty$,
#   * $\displaystyle \left(+\infty\right)^{-\infty} = 0$,
#   * $\displaystyle \left(-\infty\right)^{+\infty} = \not\exists\,$.
# ````
# 
# In any case, we remember again that **we are not operating with real numbers and symbols**.
# By saying, for example, that $5 + \infty = +\infty$ what we really mean is that if we add a function that, at a given point, has a limit of $5$ with another function that, at the same point, has as a limit $+\infty$, the result will have a limit $+\infty$.
# 
# However, there are some operations with infinite limits that do not always give the same result. They are called **indeterminations**. Namely:
# 
# ````{prf:property} Indeterminaciones
# :label: prop_indeterminaciones
# :nonumber: 
# 
# * $\displaystyle \frac{0}{0} = $ INDETERMINADO,
# * $\displaystyle \frac{\pm\infty}{\pm\infty} = $ INDETERMINADO,
# * $\displaystyle 0\left(\pm\infty\right) = $ INDETERMINADO,
# * $+\infty - \infty  = $ INDETERMINADO,
# *  $\displaystyle 1^{\pm\infty} = $ INDETERMINADO,
# * $\displaystyle 0^{0}  = $ INDETERMINADO,
# * $\displaystyle \left(\pm\infty\right)^{0}  = $ INDETERMINADO.
# ````
# 
# **Be careful!** When we say *INDETERMINATE* we do not mean that the limit does not exist, but rather that the result may vary depending on the case.
# For example, there are times when dividing a function that converges to $+\infty$ by another function that also converges to $+\infty$ the limit of the quotient will be $5$,
# but in other cases the quotient converges to $0$, l to $+\infty$, or to...
# 
# Since we cannot give a result *a priori* we will have to study case by case. How do you do that? It doesn't always work, but in many cases we can use the **L'Hôpital Rule**.
# 
# ````{prf:theorem} Regla de l Hôpital 
# :label: th_lhopital
# :nonumber: 
# 
# Sea $x_{0}\in\mathbb{R}$ y $f$ y $g$ funciones derivables en $\left(x_{0}-r, x_{0}\right)\cup\left(x_{0}, x_{0}+r\right)$. 
# 
# Si $\displaystyle \lim_{x\to x_{0}} f(x) = \displaystyle\lim_{x\to x_{0}} g(x) = 0$ y $\exists\displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}$ entonces 
# $\exists\displaystyle\lim_{x\to x_{0}} \dfrac{f(x)}{g(x)}$ y 
# 
# $$
# \displaystyle\lim_{x\to x_{0}} \dfrac{f(x)}{g(x)} = \displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}.
# $$
# 
# ````
# 
# ````{prf:remark}  
# :label: rm_lhopital
# :nonumber:
# 
# * El recíproco no es cierto: $\exists\displaystyle\lim_{x\to x_{0}} \dfrac{f(x)}{g(x)} \not\Rightarrow \exists\displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}$.
# * El enunciado del teorema también es válido si $\displaystyle \lim_{x\to x_{0}} f(x) = \pm\infty$ y  $\displaystyle\lim_{x\to x_{0}} g(x) = \pm \infty$ y/o $x_{0}=\pm\infty$.
# * Si en la expresión $\displaystyle\lim_{x\to x_{0}} \dfrac{f'(x)}{g'(x)}$ se vuelve a producir una indeterminación del tipo $\frac{0}{0}$ o $\frac{\infty}{\infty}$ 
#   (y se cumplen el resto de hipótesis), se puede volver a aplicar l'Hôpital.
# * Las indeterminaciones $0\,\infty$, $+\infty-\infty$, $0^{0}$, $\infty^{0}$ o $1^{\infty}$ se pueden convertir en indeterminaciones resolubles con l'Hôpital.
# 
# ````
# 
# **Historical curiosity:** Today known as *L'Hôpital Rule* owes its name to Guillaume de l'Hôpital, Marquis of Saint Mesme, who was an amateur mathematician of the 17th century,
# and who published the famous theorem in a book in 1696.
# However, the result was really the result of the work of Johann Bernoulli (little brother of the more famous Jacob Bernoulli, one of the greatest mathematicians in history),
# who worked for said marquis and who saw how he stole his idea. You can see more juicy details of this mathematical sauce here (short and in Spanish, let's see if you dare):
# https://emis.univie.ac.at//journals/DM/v1/art7.pdf.

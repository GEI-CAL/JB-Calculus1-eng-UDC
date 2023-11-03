#!/usr/bin/env python
# coding: utf-8

# # Convexity and concavity
# 
# ## Definitions
# 
# Mathematically, the idea of ​​a convex function is simple: it is a function in which the secant lines are above the graph of the function.
# Said colloquially: it is a glass in which water would not spill.
# 
# <img src="../../images/cap3-convexidad.png" width="400"/>
# 
# If we remember that the line secant to $f$ through $a$ and $b$ has equation $r(x) =\frac{f(b)-f(a)}{b-a}(x-a) + f(a) $, we obtain the following formal definition:
# 
# ````{prf:definition}  Convexidad
# :label: def_convexidad
# :nonumber: 
# 
# Se dice que $f$ es convexa en $[a,b]$ si
#             
# $$
# f(z) \leq f(x) + \frac{f(y)-f(x)}{y-x}(z-x) \, , \qquad \forall x < z < y, \quad x,y,z \in [a,b].
# $$
# 
# ````
# 
# Similarly, we will say that $f$ is concave if the graph lies below the secant line or, equivalently, if its inverse is a convex function.
# 
# ````{prf:definition}  Concavidad
# :label: def_concavidad
# :nonumber: 
# 
# Se dice que $f$ es cóncava en $[a,b]$ si $-f$ es convexa en ese intervalo.
#             
# ````
# 
# The latest definition linked to concavity/convexity is the following:
# 
# ````{prf:definition}  Punto de inflexión
# :label: def_punto_inflexion
# :nonumber: 
# 
# Se dice que $f$ tiene un punto de inflexión en $x_{0}$ si en ese punto la función pasa de cóncava a convexa o viceversa.
# 
# ````
# 
# <img src="../../images/cap_deriv_puntos_inflexion.png" width="400"/>
# 
# ## Convexity and concavity for sufficiently differentiable functions
# 
# And now a reflection, which will lead us to an important property: if a function is convex (look at the graph at the beginning of this section), its derivative, if it exists, will be negative at the beginning, then it will be worth $0$ at the relative minimum to pass to be positive then. That is, the derivative of a convex function is increasing. And, therefore, the derivative of this (that is, the second derivative of $f$, whenever it exists) will be positive. Of course, the opposite happens for a concave function.
# 
# All this is summarized in the following
# 
# ````{prf:property}  
# :label: prop_concavidad_convexidad
# :nonumber: 
# 
# * Sea $f:[a,b] \longrightarrow \mathbb{R}$ continua en $[a,b]$ y
# derivable en $(a,b)$. Entonces $f$ es convexa en $[a,b]$ si y sólo 
# si $f'$ es creciente en $(a,b)$. Esto equivale a que $f'' \geq 0$, 
# si $f$ tiene derivada segunda.
# 
# * Análogamente, $f$ es cóncava en $[a,b]$ si y sólo si $f'$ es decreciente
# en $(a,b)$ (es decir, si y sólo si $f'' \leq 0$, en caso de  existir derivada segunda).
# 
# ````
# 
# We illustrate this property in the following figure:
# 
# <img src="../../images/cap_deriv_prop_convexidad.png" width="400"/>
# 
# ## More information
# 
# * On this web page you can see more explanations and some examples (both solved and proposed): https://www.funciones.xyz/concavidad-y-convexidad-de-una-funcion-curvatura/
# * In the wiki they start easy, but move towards more abstract concepts. Still, you can take a look at it: https://es.wikipedia.org/wiki/Funci%C3%B3n_convexa

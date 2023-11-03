#!/usr/bin/env python
# coding: utf-8

# (sec_taylor)=
# # Theorem of Taylor
# 
# We will use Taylor’s theorem to approximate a complex function (in the sense that it is difficult to calculate its exact value at that point) at a point using a polynomial of degree n (which is easily evaluable). For this, we will need the starting function to be differentiable $n+1$ times.
# 

# ## Practical example
# 
# Suppose we want to approximate the value of the natural logarithm of 1.3, $\ln(1.3)$. A first approximation would be to take
# 
# $$
# \ln(1.3)\approx\ln(1)=0.
# $$
# Can we improve this approximation? The answer is yes. All we need to do is calculate the tangent line to the logarithm function at the point $x=1$ (we choose this point because it is easy to know the tangent line there and, moreover, it is close to $1.3$) and *walk along the tangent line* to the desired point (in this case 1.3). Let's see it in the following graph:
# 

# In[1]:


import numpy as np
import sympy as sp
import matplotlib as mp
import matplotlib.pyplot as plt
mp.__version__

get_ipython().run_line_magic('matplotlib', 'inline')

# we deffine the function
x = sp.symbols('x', real=True) 
f_expr = sp.log(x)
f = sp.Lambda(x,f_expr)

print('The value of ln(1.3) is: ', f(1.3),'\n')

# tangent line at 1
f_der=  sp.diff(f(x),x)
f1 = sp.Lambda(x,f_der)
rt = f1(1)*(x-1) + f(1)

print('The tangent line to f(x) =',f(x),' at x=1 is: P1(x) =', rt,'\n')

# point of interest
x0 = 1.3

# We create function graphs
x1 = np.linspace(0.4, 2.5, 200)
y1 = np.log(x1)
y2 = f1(1)*(x1-1) + f(1)

fig, axs = plt.subplots(1, 2, figsize=(20,10))

ax1 = axs[0]
ax1.plot(x1, y1, c='b', lw='3',  label='$f(x)=\ln(x)$')
ax1.plot(x1, y2, c='k', ls='--', lw='3', label='$P_1(x)=x-1$')
ax1.axvline(x=1.3, c='red', ls='-.', lw='2')
ax1.set_ylabel('Y', fontsize=10)
ax1.set_xlabel('X', fontsize=10)
ax1.grid()
ax1.legend(prop={'size': 18})


ax2 = axs[1]
ax2.plot(x1, y1, c='b', lw='3', label='$f(x)=\ln(x)$')
ax2.plot(x1, y2, c='k', ls='--', lw='3', label='$P_1(x)=x-1$')
ax2.axvline(x=1.3, c='red', ls='-.', lw='2')
ax2.set_ylabel('Y', fontsize=10)
ax2.set_xlabel('X', fontsize=10)
plt.xlim(0.8,1.4)
plt.ylim(-0.3,0.5)
ax2.set_xticks(np.arange(0.8,1.5,0.1))
ax2.set_yticks(np.arange(-0.3,0.6,0.1))
ax2.grid()
ax2.legend(prop={'size': 18})


# The idea is simple. We know that the line that is tangent to the natural logarithm function at the point $x_0=1$ *resembles* the $\ln$ function near that point. Moreover, it is easy to compute. Therefore, all we need to do is evaluate the tangent line at $1.3$ to get a good approximation of $\ln(1.3)$!
# 
# Let's calculate that tangent line. We need the function and its derivative evaluated at the point $x_0$, that is,
# 
# $$
# \begin{array}{lr}
#  f(x)=\ln(x) &\Rightarrow& f(x_0)=f(1)=\ln(1)=0, \\
#  f'(x)=\frac{1}{x} &\Rightarrow& f'(x_0)=f'(1)=\frac{1}{1}=1. 
# \end{array}
# $$
# Then the equation of the tangent line is
# 
# $$
# y=f(x_0)+f'(x_0)\left(x-x_0\right) \Rightarrow y=0+1(x-1)=x-1.
# $$
# Therefore, the value of the tangent line at $x=1.3$ (which we take as an approximation of $\ln(1.3)$) is
# 
# $$
# \ln(1.3)\approx 1.3-1=0.3.
# $$
# Is this a correct approximation? As we have calculated earlier in python 
# 
# $$
# \ln(1.3)=0.262364264467491...
# $$ 
# so indeed, $0.3$ is a reasonable approximation of this value.
# 
# And now, can we improve it? The answer is again yes: by using Taylor's theorem.

# ## Statement of the theorem
# 
# First, we define the Taylor polynomial:
# 
# ````{prf:definition} Polynomial of Taylor 
# :label: def_Taylor
# :nonumber: 
# 
# Let $f:[a,b]\to \mathbb{R}$ be a function of class $n+1$ in $(a,b)$, for some $n\in\mathbb{N}$.  Let $x_0\in(a,b)$. We call the **Taylor polynomial** of order $n$ centered at $x_0$ for the function $f$, $P_{n,f,x_0}$, the polynomial that evaluated at $x$ takes the value
# 
# $$
# P_{n,f,x_0}(x):=f(x_0)+\frac{f'(x_0)}{1!}\left(x-x_0\right)+
#                     \frac{f''(x_0)}{2!}\left(x-x_0\right)^{2}+\dots+
#                     \frac{f^{(n)}(x_0)}{n!}\left(x-x_0\right)^{n}.
# $$
# ````
# 
# The Taylor Theorem can be stated as follows:
# 
# ````{prf:theorem} Theorem of Taylor 
# :label: th_Taylor
# :nonumber: 
# 
# Let $f:[a,b]\to \mathbb{R}$ be a function of class $n+1$ in $(a,b)$, for some $n\in\mathbb{N}$. Let $x_0\in(a,b)$. Let $P_{n,f,x_0}$ be its Taylor polynomial of order $n$ centered at $x_0$. Then, for any $x\in(a,b)$ there exists a $\xi\in(x,x_0)$ (or $\xi\in(x_0,x)$) such that
# 
# $$
#  f(x)=P_{n,f,x_0}(x)+\frac{f^{(n+1)}(\xi)}{(n+1)!}\left(x-x_0\right)^{n+1}.
# $$
# ````
# 
# ````{prf:remark}  
# :label: rem_Taylor
# :nonumber: 
# 
# * We are generalizing the mean value theorem for differential calculus (Lagrange's theorem). Indeed, this can be understood as Taylor with $n=0$, $x_0=a$ and $x=b$, as it states 
# 
#    $$
#    \exists c\in(a,b) \text{ such that } f(b)=f(a)+f'(c)(b-a).
#    $$
# * The Taylor polynomial of order 1 relative to the function $f$ and the point $x_0$ defines a local linear approximation of $f$ in a neighborhood of $x_0$.
# * If $x_0=0$, the polynomial is called **MacLaurin**.
# * Let's highlight that $\xi$ **is not known**. The only thing we know is that $\xi \in (x,x_0)$ or $\xi \in (x_0,x)$.
# * $P_{n,f,x_0}$ is the only polynomial of degree less than or equal to $n$ such that at the point $x_0$ it and its derivatives up to order $n$ coincide with $f$ and its derivatives up to the same order.
# $ P_{n,f,x_0}(x)$ is a good approximation of $f(x)$ when $x$ is close to $x_0$. Moreover, this approximation is better the larger $n$ is (the fact that $x$ is far from $x_0$ can be compensated by increasing $n$).
# ````  
# 

# ### Bounding the error
# 
# A direct consequence of Taylor's Theorem is that
# 
# $$
# f(x)-P_{n,f,x_0}(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}\left(x-x_0\right)^{n+1},
# $$
# and therefore,
# 
# $$
# \left|f(x)-P_{n,f,x_0}(x)\right|=\frac{\left|f^{(n+1)}(\xi)\right|}{(n+1)!}\left|x-x_0\right|^{n+1}.
# $$
# That is, the absolute difference between $f(x)$ and $P_{n,f,x_0}(x)$ is the term that depends on $\xi$ (unknown) in absolute value, often represented as 
# 
# $$
# R_{n,f,x_0}(x):=\frac{f^{(n+1)}(\xi)}{(n+1)!}\left(x-x_0\right)^{n+1}.
# $$
# Obviously, not knowing $\xi$ we also cannot know exactly how much $R_{n,f,x_0}(x)$ will be. What we can do is bound it (that is, indicate that it is less than or equal to a certain number). To do this, just realize that, as $\xi$ is between $x$ and $x_0$ (or between $x_0$ and $x$), it holds
# 
# $$
# \left|f^{(n+1)}(\xi)\right|\leq \sup_{s\in(x,x_{0})} \left|f^{(n+1)}(s)\right| \leq \sup_{s\in[x,x_{0}]} \left|f^{(n+1)}(s)\right|,
# $$
# and, then,
# 
# $$
# \left|R_{n,f,x_0}(x)\right|=\frac{\left|f^{(n+1)}(\xi)\right|}{(n+1)!}\left|x-x_0\right|^{n+1}\leq \frac{\sup_{s\in[x,x_{0}]} \left|f^{(n+1)}(s)\right|}{(n+1)!}\left|x-x_0\right|^{n+1}.
# $$
# Summarizing, the bounding of the absolute error we make if we approximate $f(x)$ by $P_{n,f,x_0}(x)$ will be
# 
# $$
# \left|f(x)-P_{n,f,x_0}(x)\right|=\frac{\left|f^{(n+1)}(\xi)\right|}{(n+1)!}\left|x-x_0\right|^{n+1} \leq  \frac{\sup_{s\in[x,x_{0}]} \left|f^{(n+1)}(s)\right|}{(n+1)!}\left|x-x_0\right|^{n+1}.
# $$
# Therefore, to bound this error all we need to do is find the absolute maximum and minimum (if they exist) of the function $f^{(n+1)}$ in $[x,x_{0}]$ and choose among them the one with the greatest absolute value. 
# 
# 
# To avoid confusion due to notation, we can denote $g(s):=f^{(n+1)}(s)$ and thus the dreaded problem of bounding Taylor's error is reduced to a standard problem of calculating maximum and minimum absolute of a function $g$ in an interval $[x,x_{0}]$.

# ## Calculation of the Taylor Polynomial in `Sympy`
# 
# We will show a `Python` function that symbolically calculates the Taylor polynomial of a given function. The input arguments will be the function, $f$, the Taylor center, $x_{0}$, and the order of the polynomial, $n$. 
# 
# The function will return the Taylor polynomial and the function that provides the Taylor remainder.
# 

# In[2]:


import sympy as sp

x,t=sp.symbols('x,t')

# p: Taylor's polynomial
# R: rest in absolut value
def taylor(f,x0,n):
    p=0
    for i in range(n+1):
        p+=sp.diff(f,x,i).subs(x,x0)/sp.factorial(i)*(x-x0)**i
    R=sp.diff(f,x,n+1).subs(x,t)/sp.factorial(n+1)*(x-x0)**(n+1)
    return p,R


# ## Completing the Practical Example
# 
# We are going to use the previous function, `taylor`, to improve the approximation of $\ln(1.3)$ that we achieved with the tangent line at the beginning of this section using the Taylor polynomial of order 2. We will also bound the error committed.
# 
# 

# In[3]:


# Code here
import sympy as sp
import numpy as np

# point at which we center the Taylor polynomial
x0 = 1

# function we want approximate
f_exp = sp.log(x)

# we compute Taylor's theorem of order 1, centered at x0
n = 1 # grade of the polynomial
P1,R1=taylor(f_exp,1.,1)
print('Taylor polynomial of order 1: \n',P1,'\n Rest of Taylor of order 1: \n',R1,'\n')

# we compute Taylor's theorem of order 1
n = 2 
P2,R2=taylor(f_exp,1.,2)
print('Taylor polynomial of order 2: \n',P2,'\n Rest of Taylor of order 2: \n',R2,'\n')


# We draw the result:

# In[4]:


# We convert P1 and P2 into `lambdify` functions so we can draw them
P1_lamb = sp.lambdify(x,P1)
P2_lamb = sp.lambdify(x,P2)

# We create function graphs
x1 = np.linspace(0.4, 2.5, 200)
y1 = np.log(x1)

# we evaluate P2 at the points of x1
P1x = P1_lamb(x1)
P2x = P2_lamb(x1)

fig, axs = plt.subplots(1, 2, figsize=(20,10))

ax1 = axs[0]
ax1.plot(x1, y1, c='b', lw='3',  label='$f(x)=\ln(x)$')
ax1.plot(x1, P1x, c='k', ls='--', lw='3', label='$P_1(x)=x-1$')
ax1.plot(x1, P2x, c='r', ls='--', lw='3', label='$P_2(x)=x-1 - \dfrac{(x-1)^2}{2}$')
ax1.set_ylabel('Y', fontsize=10)
ax1.set_xlabel('X', fontsize=10)
ax1.grid()
ax1.legend(prop={'size': 18})


ax2 = axs[1]
ax2.plot(x1, y1, c='b', lw='3', label='$f(x)=\ln(x)$')
ax2.plot(x1, P1x, c='k', ls='--', lw='3', label='$P_1(x)=x-1$')
ax2.plot(x1, P2x, c='r', ls='--', lw='3', label='$P_2(x)=x-1 - \dfrac{(x-1)^2}{2}$')
ax2.set_ylabel('Y', fontsize=10)
ax2.set_xlabel('X', fontsize=10)
plt.xlim(0.8,1.4)
plt.ylim(-0.3,0.5)
ax2.set_xticks(np.arange(0.8,1.5,0.1))
ax2.set_yticks(np.arange(-0.3,0.6,0.1))
ax2.grid()
ax2.legend(prop={'size': 18})


# We have
# 
# $$
# \begin{array}{rl}
#  f(x)=\ln(x) &\Rightarrow& f(x_0)=f(1)=\ln(1)=0, \\
#  f'(x)=\frac{1}{x} &\Rightarrow& f'(x_0)=f'(1)=\frac{1}{1}=1, \\
#  f''(x)=-\frac{1}{x^2} &\Rightarrow& f''(x_0)=f''(1)=-\frac{1}{1}=-1, \\
#  f'''(x)=\frac{2}{x^3}. \\
# \end{array}
# $$
# 
# Then,
# 
# $$
# P_{2,f,1}(x)=f(1)+\frac{f'(1)}{1!}(x-1)+\frac{f''(1)}{2!}(x-1)^2=(x-1)-\frac{(x-1)^2}{2}.
# $$
# So
# 
# $$
# \ln(1.3)=f(1.3)\approx
# P_{2,f,1}(1.3)=1.3-1-\frac{(1.3-1)^2}{2}=0.3-\frac{0.09}{2} = \frac{51}{200}=0.255.
# $$
# 
# Let's remember that $\ln(1.3)=0.262364264467491...$ and the approximation obtained by the tangent line is $P_{1,f,1}(1.3)=0.3$. We see that $P_{2,f,1}(1.3)=0.255$ is a good approximation of the value of $\ln(1.3)$ and, as expected, better than that corresponding to the Taylor polynomial of order 1.
# 
# Let's bound the error using what we just explained:
# 
# $$
# \left|f(1.3)-P_{n=2,f,x_0=1}(1.3)\right|=\frac{\left|f'''(\xi)\right|}{3!}\left|1.3-1\right|^{3} \leq  \frac{\sup_{s\in[1,1.3]} \left|f'''(s)\right|}{3!}0.3^{3}.
# $$
# So... we just need to calculate that supremum!
# 
# $$
# \sup_{s\in[1,1.3]} \left|f'''(s)\right| = \sup_{s\in[1,1.3]}
# \left|\frac{2}{s^3}\right| \stackrel{(*)}{=} \frac{2}{1^3} = 2. 
# $$
# $(*)$ because the function $\frac{2}{s^3}$ is positive and decreasing,
# it reaches its maximum in absolute value at the left end (that is, at $s=1$).
# 

# ## Proposed Exercise
# 
# Using `Python`, calculate the Taylor polynomial of different orders for $f(x)=\cos(x)$ centered at 0, and graphically check how those of higher order approximate the given function much better.

# ## Exercises to practice a little more
# 
# * https://existelimite.blogspot.com/2012/12/ejercicio-de-taylor.html
# * https://existelimite.blogspot.com/2013/01/aproximar-una-raiz-cuarta-con-el.html
# * https://existelimite.blogspot.com/2013/10/una-cuestion-sobre-el-polinomio-de.html
# * https://existelimite.blogspot.com/2021/10/otro-ejercicio-de-taylor-este-para-una.html

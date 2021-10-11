import numpy as np



f = lambda x: x**2
class SVF:
  
  def __init__(self, f):
    self.f = f
  
  def value(self,x):
    return self.f(x)
  
  def derivative(self, a, b, dx):
      g = lambda x, m : (m(x+dx)-m(x))/dx   
      return np.array([g(x,self.f) for x in np.arange(a,b,dx)])

  def integrate(self, a,b,dx):
    #trapezoidal rule
    return sum([2*self.f(x) if not (x==a or x==b) else self.f(x) for x in np.arange(a,b+dx,dx)])*dx/2
  def integral(self, a, x, dx):
    return [SVF.integrate(self, a, i, dx) for i in np.arange(a,x, dx)]

p = SVF(f)

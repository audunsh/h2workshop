#!/usr/bin/env python
# coding: utf-8

# # Ekstra: den deriverte (endring)
# 
# ---
# 

# Du kjenner sannsynligvis derivasjon som følgende operasjon
# 
# $$ \frac{d}{dx} f(x) := \lim_{\Delta x \rightarrow 0} \frac{f(x + \Delta x) - f(x)}{\Delta x}.$$
# 
# Det finnes flere ekvivalente skrivemåter:
# 
# $$ \frac{d}{dx}f(x) = f'(x) = \dot{f}(x).$$
# 
# Vi fortolker typisk den deriverte av en funksjon som *endringsraten* i verdien $f(x)$, som følge av en liten endring i variabelen $x$.
# 

# # Eksempel: numerisk derivasjon

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def numdiff_vis_forward(x0, dx, method = 0):
    """
    Interactive example of forward difference
    """
    
    # define some x values
    x = np.linspace(0,2*np.pi, 100)
    
    # A function and it's exact derivative
    f = lambda x : -x*(x-2*np.pi)  # f(x)
    
    df = lambda x : -2*x + 2*np.pi # f'(x)
    
    
    # create a figure, plot results
    plt.figure(1, figsize = (10,7))
    
    plt.plot(x,f(x), "-", label = "f(x)") #plot function
    
    
    
    
    plt.title("Numerical derivative (Newton's difference quotient)")
    plt.xlabel("x") #merk x-aksen
    

    
    
    plt.plot(x,df(x0)*(x-x0) + f(x0), "--", label = "$tangent(f(x_0))$ (exact)")
    
    if method==2:
        df_dx = (f(x0+dx)-f(x0))/dx # Compute D^+ f(x0)
        lab = "$f(x_0) + (x-x_0) D^+ f(x_0)$"
        plt.plot(x0, f(x0), "o", color = (0,0,0))
        plt.plot(x0+dx, f(x0+dx), "o", color = (0,0,0))
        plt.fill_between([x0,x0+dx], [0,0], [12,12], color = (.3,.6,1), alpha = .1)
        
        plt.plot(x,df_dx*(x-x0) + f(x0), label = lab) #plot Tangent in f(x0)
        
    if method==1:
        df_dx = (f(x0+.5*dx)-f(x0-.5*dx))/dx # Compute D f(x0)
        lab = "$f(x_0) + (x-x_0) D f(x_0)$"
        
        plt.plot(x0+.5*dx, f(x0+.5*dx), "o", color = (0,0,0))
        plt.plot(x0-.5*dx, f(x0-.5*dx), "o", color = (0,0,0))
        plt.fill_between([x0-.5*dx,x0+.5*dx], [0,0], [12,12], color = (.3,.6,1), alpha = .1)
        
        plt.plot(x,df_dx*(x-x0) + f(x0), label = lab) #plot Tangent in f(x0)
        
    if method==0:
        df_dx = (f(x0)-f(x0-dx))/dx # Compute D^- f(x0)
        lab = "$f(x_0) + (x-x_0) D^- f(x_0)$"
        
        plt.plot(x0, f(x0), "o", color = (0,0,0))
        plt.plot(x0-dx, f(x0-dx), "o", color = (0,0,0))
        plt.fill_between([x0-dx,x0], [0,0], [12,12], color = (.3,.6,1), alpha = .1)
        
        plt.plot(x,df_dx*(x-x0) + f(x0), label = lab) #plot Tangent in f(x0)
        
        
    
    
    
    
    
    plt.text(x0+dx/2.0, 4, "$\Delta x$", ha="center")
    plt.text(x0, f(x0)+.2, "$x_0$")
    
    plt.legend()
    plt.ylim(0,np.pi**2 +1)
    plt.xlim(0,2*np.pi)
    plt.show()


# In[2]:


from ipywidgets import interact, interactive
from IPython.display import display

y = interactive(numdiff_vis_forward, x0 = (0,2*np.pi,.001), dx = (0.001, 1, 0.001), method = (0,2,1)) 
display(y)


# ```{admonition} Diskusjon
# - Hva er en passende verdi for ∆x? Kan du se en generell trend?
# - Forandre funksjonen og dens deriverte. Fungerer de ulike diskrete differensialene like godt for andre funksjoner?
# ```

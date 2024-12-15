

def bisection_method(f, a, b, max_iter, tol=1e-6):
    
    
     
    if f(a) * f(b) > 0:
        print("The function has the same sign at a and b. Choose a different interval.")
        return None

      
      
     
    iter_count = 0   # iteration number 
    while iter_count < max_iter:
         
        c = (a + b) / 2
        
        
        
         
        if abs(   f(c)  ) < tol: 
            print(f"Converged to root: {c} after {iter_count + 1} iterations.")
            return c
 
        
        
        if f(a) * f(c) < 0:
            b = c   
        else:
            a = c  
        iter_count += 1    

        
    
    print(f"Max iterations reached ( {max_iter} ). Approximate root: {c}")
    return (a + b) / 2   

  
  
  
 
def f(x):
    return x**3 - x - 2   

a, b = 1, 2   
max_iterations = 3  

root = bisection_method(f, a, b, max_iterations)
print("Root found:", root)

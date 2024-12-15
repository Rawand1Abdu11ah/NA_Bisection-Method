

def bisection_method(f, a, b, tol=1e-6, max_iter=100):

     
    if f(a) * f(b) > 0:
        print("The function has the same sign at a and b. Choose a different interval.")
        return None


     
    iter_count = 0
    while iter_count < max_iter:
        
        c = (a + b) / 2
        

         
        if abs(f(c)) < tol or abs(b - a) < tol:
            print(f"Converged to root: {c} after {iter_count + 1} iterations.")
            return c
        
        

        
         
        if f(a) * f(c) < 0:
               b = c   
        else:
               a = c   

        iter_count += 1   

        
        

        
    
    print("Max iterations reached. The root may not have converged.")
    return (a + b) / 2   

  
  
  
  
 
def f(x):
    return x**3 - x - 2   

a, b = 1, 2   
root = bisection_method(f, a, b)
print("Final result : " + " \n" + "Root found= ", root)

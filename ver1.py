

def bisection_method(f, a, b, max_iter, tol=1e-6):
    
    
    # Step 1: opposite signs
    if f(a) * f(b) > 0:
        print("The function has the same sign at a and b. Choose a different interval.")
        return None

      
      
    # Step 2: Start the iteration process
    iter_count = 0   # iteration number 
    while iter_count < max_iter:
        # Calculate the midpoint -c-
        c = (a + b) / 2
        
        
        
        # Check if the midpoint is a root or if the interval is within tolerance
        if abs(   f(c)  ) < tol: 
            print(f"Converged to root: {c} after {iter_count + 1} iterations.")
            return c
 
        
        # Update the interval based on the sign of f(c)
        if f(a) * f(c) < 0:
            b = c  #   [a, c]
        else:
            a = c  # Root lies in [c, b]
        iter_count += 1 # I have Incremented iteration count.  

        
    # If the maximum number of iterations is reached
    print(f"Max iterations reached ( {max_iter} ). Approximate root: {c}")
    return (a + b) / 2  # Return the best estimate of the root

  
  
  
# Example usage
def f(x):
    return x**3 - x - 2  # Example function

a, b = 1, 2  # Interval [a, b]
max_iterations = 3 # User-defined maximum number of iterations

root = bisection_method(f, a, b, max_iterations)
print("Root found:", root)

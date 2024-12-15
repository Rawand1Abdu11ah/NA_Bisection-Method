

def bisection_method(f, a, b, tol=1e-6, max_iter=100):

    # Step 1: Ensure f(a) and f(b) have opposite signs
    if f(a) * f(b) > 0:
        print("The function has the same sign at a and b. Choose a different interval.")
        return None


    # Step 2: Start the iteration process
    iter_count = 0
    while iter_count < max_iter:
        # Calculate the midpoint
        c = (a + b) / 2
        

        # Check if the midpoint is a root or if the interval is within tolerance
        if abs(f(c)) < tol or abs(b - a) < tol:
            print(f"Converged to root: {c} after {iter_count + 1} iterations.")
            return c
        
        

        
        # Update the interval based on the sign of f(c)
        if f(a) * f(c) < 0:
               b = c  # Root lies in [a, c]
        else:
               a = c  # Root lies in [c, b]

        iter_count += 1  # Increment the iteration count

        
        

        
    # If maximum iterations are reached
    print("Max iterations reached. The root may not have converged.")
    return (a + b) / 2  # Return the best estimate of the root

  
  
  
  
# Example usage
def f(x):
    return x**3 - x - 2  # Example function

a, b = 1, 2  # Interval [a, b]
root = bisection_method(f, a, b)
print("Final result : " + " \n" + "Root found= ", root)

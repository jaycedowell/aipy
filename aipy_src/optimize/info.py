# Python3 compatibility
from __future__ import print_function, division, absolute_import

"""
Optimization Tools
==================

 A collection of general-purpose optimization routines.

   fmin        --  Nelder-Mead Simplex algorithm
                     (uses only function calls)
   fmin_powell --  Powell's (modified) level set method (uses only
                     function calls)
   fmin_ncg    --  Line-search Newton Conjugate Gradient (can use
                     function, gradient and Hessian).

  Global Optimizers

   anneal      --  Simulated Annealing
   brute       --  Brute force searching optimizer


  Scalar function minimizers

   fminbound   --  Bounded minimization of a scalar function.
   brent       --  1-D function minimization using Brent method.
   golden      --  1-D function minimization using Golden Section method
   bracket     --  Bracket a minimum (given two starting points)


 Also a collection of general-purpose root-finding routines.

   fsolve      --  Non-linear multi-variable equation solver.


  Scalar function solvers

   brentq      --  quadratic interpolation Brent method
   brenth      --  Brent method (modified by Harris with hyperbolic
                     extrapolation)
   ridder      --  Ridder's method
   bisect      --  Bisection method
   newton      --  Secant method or Newton's method

   fixed_point --  Single-variable fixed-point solver.

 A collection of general-purpose nonlinear multidimensional solvers.

   broyden1            --  Broyden's first method - is a quasi-Newton-Raphson
                           method for updating an approximate Jacobian and then
                           inverting it
   broyden2            --  Broyden's second method - the same as broyden1, but
                           updates the inverse Jacobian directly
   broyden3            --  Broyden's second method - the same as broyden2, but
                           instead of directly computing the inverse Jacobian,
                           it remembers how to construct it using vectors, and
                           when computing inv(J)*F, it uses those vectors to
                           compute this product, thus avoding the expensive NxN
                           matrix multiplication.  
   broyden_generalized --  Generalized Broyden's method, the same as broyden2,
                           but instead of approximating the full NxN Jacobian,
                           it construct it at every iteration in a way that
                           avoids the NxN matrix multiplication.  This is not
                           as precise as broyden3.
   anderson            --  extended Anderson method, the same as the
                           broyden_generalized, but added w_0^2*I to before
                           taking inversion to improve the stability
   anderson2           --  the Anderson method, the same as anderson, but
                           formulated differently

 Utility Functions

   line_search --  Return a step that satisfies the strong Wolfe conditions.
   check_grad  --  Check the supplied derivative using finite difference
                     techniques.
"""


"""
Created on Tue Jan 10

@author: Mark Faust (JHED: mfaust4)
"""

# Project 3

# Helper method to find the greatest common denominator
# between two integers using Euclidian algorithm
def gcd(num1, num2):
    """
    

    Parameters
    ----------
    num1 : int
        Number to be analyzed.
    num2 : int
        Number to be analyzed.

    Returns
    -------
    greatest_common_denominator : int
        The greatest common denominator between number 1 and 2.

    """
    
    # Checks to see if either number is equal to 0 adn return 1 so that 
    # later calculations aren't impacted
    if num1 == 0 or num2 == 0:
        return 1
    
    x = max(num1, num2)
    y = min(num1, num2)
    greatest_common_denominator = y
    
    # Euclidian algorithm to find two numbers' greatest
    # common denominator
    while True:
        mult = x // y
        remain = x - (y * mult)
        if remain == 0:
            return greatest_common_denominator
        else:
            x = y
            y = remain
            greatest_common_denominator = remain
           
class Frac:
    
    def __init__(self, num = 1, den = 1):
        """
        

        Parameters
        ----------
        num : int, optional
            Desired numerator of new fraction. The default is 1.
        den : int, optional
            Desired denominator of new fraction. The default is 1.

        Returns
        -------
        None.

        """
        self.num = num
        self.den = den
        return
    
    def __str__(self):
        """
        

        Returns
        -------
        str
            String representation of the fraction.

        """
        return f"{self.num}/{self.den}"
    
    def simplify(self):
        """
        

        Parameters
        ----------
        frac : Frac
            Frac object of the Frac class.

        Returns
        -------
        frac : Frac
            Mathematically-simplified version of the passed Frac object.

        """
        
        # Finding common denominator between the numerator and the
        # denominator using a user-defined helper function
        common_den = gcd(self.num, self.den)
        self.num = self.num // common_den
        self.den = self.den // common_den
        
        # Ensure proper representation of fraction when printed
        if (self.den < 0 and not self.num < 0) or \
            (self.den < 0 and self.num < 0):
            self.den *= -1
            self.num *= -1
        
        return self
    
    def __add__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction to be added to self.

        Returns
        -------
        Frac
            Resultant fraction after addition with other.

        """
        
        # Multiplies numerator of one fraction by the denoinator
        # of the other to find new neumerators to be added
        new_self_num = self.num * other.den
        new_other_num = other.num * self.den
        
        # Adds numerators of new fractions together
        new_num = new_self_num + new_other_num
        
        # Finds common denominator between two new fractions
        new_den = self.den * other.den
        
        # Returns simplified new fraction 
        return Frac(new_num, new_den).simplify()
    
    def __sub__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction to be subtracted by self.

        Returns
        -------
        Frac
            Resultant fraction after subtraction with other.

        """
        
        # Multiplies numerator of one fraction by the denoinator
        # of the other to find new neumerators to be subtracted
        new_self_num = self.num * other.den
        new_other_num = other.num * self.den
        
        # Subtracts numerators of new fractions 
        new_num = new_self_num - new_other_num
        
        # Finds common denominator between two new fractions
        new_den = self.den * other.den
        
        # Returns simplified new fraction 
        return Frac(new_num, new_den).simplify()
    
    def __mul__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction to be multiplied by self.

        Returns
        -------
        Frac
            Resultant fraction after multiplication with other.

        """
        
        # Multiplies the numerators of the two fractions together
        new_num = self.num * other.num
        
        # Multiplies the denominators of the two fractions together
        new_den = self.den * other.den
        
        # Return simplified new fraction
        return Frac(new_num, new_den).simplify()
    
    def __truediv__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction to be divisor.

        Returns
        -------
        Frac
            Resultant fraction after diviision with other.

        """
        
        # Finding the reciprocal of the other fraction by swapping
        # its numerator and denominator
        other_recip = Frac(other.den, other.num)
        
        # Multipying the fraction on the left by the reciprocal
        # of the fraction on the right
        new_frac = self * other_recip
        
        # Return simplified new fraction
        return new_frac.simplify()
    
    def __eq__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction being compared to.

        Returns
        -------
        bool
            Whether or not the two passed Fracs are equal.

        """
        """
        # Creates new, simlified versions of the fractions
        simp_self = self.simplify()
        simp_other = other.simplify()
        
        # Checks if the simplified fractions' numerators and denominators
        # are equal to each other
        if simp_self.num == simp_other.num and \
            simp_self.den == simp_other.den:
            return True
        
        return False
        """
        # Divides the two numbers and checks if the result equals 1
        if (self / other).num == 1 and (self / other).den == 1 :
            return True
        
        return False
    
    def __ne__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction being compared to.

        Returns
        -------
        bool
            Whether or not the two passed Fracs are equal.

        """
        # Returns opposite of equal method's determination
        return not self == other
    
    def __gt__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction being compared to.

        Returns
        -------
        bool
            Whether or not the Frac on the left is greater than the one
            on the right.

        """
        # Divides the two numbers and checks if the result's numerator
        # is greater than its denominator 
        if (self / other).num > (self / other).den:
            return True
        
        return False
    
    def __ge__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction being compared to.

        Returns
        -------
        bool
            Whether or not the Frac on the left is greater than or equal
            to the one on the right.

        """
        # Divides the two numbers and checks if the result's numerator
        # is greater than or equal to its denominator 
        if (self / other).num >= (self / other).den:
            return True
        
        return False
    
    def __lt__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction being compared to.

        Returns
        -------
        bool
            Whether or not the Frac on the left is less than the one
            on the right.

        """
        # Divides the two numbers and checks if the result's numerator
        # is less than its denominator 
        if (self / other).num < (self / other).den:
            return True
        
        return False
    
    def __le__(self, other):
        """
        

        Parameters
        ----------
        other : Frac
            Other fraction being compared to.

        Returns
        -------
        bool
            Whether or not the Frac on the left is less than or equal
            to the one on the right.

        """
        # Divides the two numbers and checks if the result's numerator
        # is less than or equal to its denominator 
        if (self / other).num <= (self / other).den:
            return True
        
        return False
    
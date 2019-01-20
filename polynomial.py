class Polynomial:

    def __init__(self, *args):
        self.coeffs = [arg for arg in args]
        # Remove trailing zeroes in coefficients
        while self.coeffs[-1] == 0:
            del self.coeffs[-1]

    def __repr__(self):
        terms = []

        # Create the strings for each term
        for deg, coeff in enumerate(self.coeffs):
            if isinstance(coeff, str):      # Constants represented as strings
                terms.append('{}x^{}'.format(coeff, deg))
            elif coeff != 0:                # Don't print terms with coeff 0
                terms.append('{0:.3g}x^{1}'.format(coeff, deg))

        # String manipulations:
        # Join terms
        # x^0 = 1
        # x^1 = x
        # 1x^n = x^n              
        # a + -b = a - b   
        return ' + '.join(reversed(terms)).\
                replace('x^0', '').\
                replace('x^1', 'x').\
                replace('1x', 'x').\
                replace('+ -', '- ')    

    def __len__(self):
        return len(self.coeffs)

    def __sub__(self, other):
        n = max(len(self), len(other))

        coeffs_1 = self.coeffs
        coeffs_2 = other.coeffs
        
        # Make sure the two coefficient lists are properly zero-padded
        while len(coeffs_1) < n: coeffs_1.append(0)
        while len(coeffs_2) < n: coeffs_2.append(0)

        coeffs = []

        for i, j in zip(coeffs_1, coeffs_2):
            coeffs.append(i-j)

        return Polynomial(coeff for coeff in coeffs)

    def __add__(self, other):
        n = max(len(self), len(other))

        coeffs_1 = self.coeffs
        coeffs_2 = other.coeffs
        
        # Make sure the two coefficient lists are properly zero-padded
        while len(coeffs_1) < n: coeffs_1.append(0)
        while len(coeffs_2) < n: coeffs_2.append(0)

        coeffs = []

        for i, j in zip(coeffs_1, coeffs_2):
            coeffs.append(i+j)

        return Polynomial(coeff for coeff in coeffs)

    def __getitem__(self, i):
        try:
            return self.coeffs[i]
        except (IndexError, TypeError) as error:
            raise IndexError('Coefficients must be accessed by valid index.')

    def __setitem__(self, i, value):
        if not isinstance(i, int) or i < 0:
            raise TypeError('Orders of coefficients must be positive integers.')

        while len(self) < i-1: self.coeffs.append(0)

        self.coeffs[i] = value


    def __iter__(self):
        return iter(self.coeffs)

    def __eq__(self, other):
        return True if (a == b for a, b in zip(self, other)) else False

    def __call__(self, x):
        val = 0
        for deg, coeff in enumerate(self):
            val += coeff * x**deg
        return val
            
    def differentiate(self):
        coeffs = []

        for deg, coeff in enumerate(self):
            coeffs.append(coeff*deg)

        return Polynomial(coeff for coeff in coeffs[1:])

    def integrate(self, constant='C'):
        coeffs = [constant]

        for deg, coeff in enumerate(self):
            coeffs.append(coeff/(deg+1))

        return Polynomial(coeff for coeff in coeffs)


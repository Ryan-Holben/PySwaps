import permutation

class SwapElement(object):
    """Represents a single swap action of 2 adjacent elements in a Permutation
       (that is, an element of the adjacent swap permutation group of length
       `length`).
    """

    def __init__(self, name, length, i, j = None):
        # TODO: Ought to have checks on i & j
        self.name = name
        self.length = length
        self.i = i
        self.j = j if j else i+1    # Defaults to an adjacent swap

    def __str__(self):
        tup = [0]*self.length
        tup[self.i] = 1
        tup[self.j] = 1
        return str(tuple(tup))

    def __mul__(self, right_permutation):
        """ Returns `result` in the equation:
                    result = self * right_permutation
            where the object types are:
                    permutation = swap_element * permutation

            IMPORTANT: This convention means we always left-multiply
            permutations by swap_elements.
        """
        if type(right_permutation) != permutation.Permutation:
            return None
        return right_permutation.apply_swap_element(self)

import swap

class Permutation(object):
    """Represents a single permutation of length n, containing the numbers 1..n.
       The object is meant to be somewhat immutable.  Thus the swap() function
       returns a new object.
    """
    def __init__(self, arg):
        if type(arg) == int:
            self.p = tuple(range(1,arg+1))
            self.length = arg
        else:
            self.p = tuple(arg)
            self.length = len(arg)

    def set(self, tup):
        if len(tup) != self.length:
            return False
        self.p = tup
        return True

    def get(self):
        return self.p

    def __str__(self):
        return str(self.p)

    def __eq__(self, other):
        return self.p == other.p

    def swap_by_index_adjacent(self, i):
        """Returns the result of swapping positions i and i+1."""
        if i < 0 or i > self.length-2:
            return None
        return Permutation(list(self.p[:i]) + list([self.p[i+1]]) + list([self.p[i]]) + list(self.p[i+2:]))

    def swap_by_index(self, i, j):
        """Returns the result of swapping positions i and j."""
        if i < 0 or i > self.length-1 or j < 0 or j > self.length-1:
            return None
        if i == j:
            return Permutation(self.p)
        if i < j:
            I = i
            J = j
        else:
            I = j
            J = i
        return Permutation(list(self.p[:I]) + [self.p[J]] + list(self.p[I+1:J]) + [self.p[I]] + list(self.p[J+1:]))

    def apply_swap_element(self, swap_element):
        """Apply a swap object to this permutation and return the resulting
        Permutation object."""
        if self.length != swap_element.length:
            return False
        return self.swap_by_index(swap_element.i, swap_element.j)

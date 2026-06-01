class Solution:
    def isSorted(self, arr) -> bool:
        """
        We are to sort the array in asseceding order.

        Algorithm:
        1. We can have to create a duplicate array
        2. Sort the duplicate array
        3. and loop through to find match the arrays or use == sign to find eqv

        """

        # 1
        arr2 = arr.copy()

        # 2
        arr2.sort()

        # 3
        return arr == arr2

class Solution:
    def reverseArray(self, arr):
        """
        This should not be that complicated

        Application: Traversal-Sorting/Modification

        Algo:
        1. We can solve this in-place using two-pointers
        2. We can also solve using an extra array
        3. We can manioulate the array
        """

        n = len(arr) - 1

        # 3
        arr[:] = arr[n::-1]
        return arr
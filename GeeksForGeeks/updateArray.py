class Solution:
    def updateArray(self, arr):
        """
        Application: Traversal-modification

        Solution:
        1. We start at the first index. When we are at the first and last index, we want
        to set l = 1, m = arr, r = arr + 1. For the last we do accordingly

        2. An edge case which is also accouted for is when we only have 1 value.
        our algorithm should be able to cover that.

        """
        nArr = [0] * len(arr)

        # 2
        if len(arr) == 1:
            arr[0] = 1 * arr[0] * 1
            return arr

        # 1
        for _ in range(len(arr)):
            l = 0
            m = 0
            r = 0
            if _ == 0:
                l = 1
                m = arr[_]
                r = arr[_ + 1]
                nArr[_] = 1 * m * r

            elif _ == len(arr) - 1:
                l = arr[_ - 1]
                m = arr[_]
                r = 1
                nArr[_] = l * m * 1

            else:
                l = arr[_ - 1]
                m = arr[_]
                r = arr[_ + 1]
                nArr[_] = l * m * r
        arr[:] = nArr
        return arr

arr = [2,5,7,8,3]
arr1 = [1,2,4]
arr2 = [5]
arr3 = [7,2]
print(Solution().updateArray(arr))
print(Solution().updateArray(arr1))
print(Solution().updateArray(arr2))
print(Solution().updateArray(arr3))
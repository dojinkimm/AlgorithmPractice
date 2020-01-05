class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(arr, l, h, key):
            if l > h: 
                return -1

            mid = (l + h) // 2
            if arr[mid] == key: 
                return mid 

            if arr[l] <= arr[mid]: 

                if key >= arr[l] and key <= arr[mid]: 
                    return binary(arr, l, mid-1, key) 
                return binary(arr, mid+1, h, key) 

            if key >= arr[mid] and key <= arr[h]: 
                return binary(arr, mid+1, h, key) 
            return binary(arr, l, mid-1, key) 
        
        return binary(nums, 0, len(nums)-1, target)
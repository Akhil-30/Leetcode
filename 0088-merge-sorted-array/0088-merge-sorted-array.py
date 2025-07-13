class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n is 0:
            nums1=nums1 
        elif m is 0:
            for i in range(n):
                nums1[i]=nums2[i]
        n1,n2,l=m-1,n-1,m+n-1
        while n1>=0 and n2>=0:
            if nums1[n1]<nums2[n2]:
                nums1[l]=nums2[n2]
                n2-=1
            else:
                nums1[l]=nums1[n1]
                n1-=1
            l-=1
        while n2>=0:
            nums1[l]=nums2[n2]
            l-=1
            n2-=1
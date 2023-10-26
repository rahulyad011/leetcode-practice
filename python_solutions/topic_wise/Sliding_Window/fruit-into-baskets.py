class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """solution1 with dict to store buckets and whenever a third types comes delete all 
        first type of elements thus increasing the left pointer in the required amount"""
        l = 0
        r = 0
        max_count = 0
        basket = {}
        while r<len(fruits):
            basket[fruits[r]] = basket.get(fruits[r], 0) + 1
            # updating the left pointer when third element comes, move left pointer 
            # until only two types of fruits are left
            while len(basket)>2:
                basket[fruits[l]]-=1
                if basket[fruits[l]] == 0:
                    del basket[fruits[l]]
                l+=1
            max_count = max(max_count, r-l+1)
            r+=1
        return max_count

        """Solution2 with last_index saving : it gets a bit complicated if we don't manage the 
        pointers update properly, note that first and secon type are to be updated when 
        accessing the 3rd type, Optimal as just one single loop 1*O(n)"""
        # l = 0
        # r = 0
        # max_count = 0
        # first_type = -1
        # second_type = -1
        # last_index = 0
        # while r<len(fruits):
        #     if first_type == -1 or fruits[r]==first_type:
        #         if r>0:
        #             if fruits[r-1]!=first_type:
        #                 last_index=r
        #         first_type = fruits[r]
        #         max_count = max(max_count, r-l+1)
        #     elif second_type == -1 or fruits[r]==second_type:
        #         if r>0:
        #             if fruits[r-1]!=second_type:
        #                 last_index=r
        #         second_type = fruits[r]
        #         max_count = max(max_count, r-l+1)
        #     else:
        #         first_type = fruits[last_index]
        #         second_type = fruits[r]
        #         l=last_index
        #         last_index = r
        #     # print(l, r)
        #     r+=1
        # return max_count
            
            

        
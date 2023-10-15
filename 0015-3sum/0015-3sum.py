class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = set()
        negative, positive, zero = [], [], []

        for num in nums:
            if num < 0:
                negative.append(num)
            elif num > 0:
                positive.append(num)
            else:
                zero.append(num)
        
        neg_set, pos_set = set(negative), set(positive)

        # Cases of zero in middle
        if zero:
            for num in pos_set:
                if -num in neg_set:
                    output.add((-num, 0, num))
        if len(zero) > 2:
            output.add((0, 0, 0))
        
        # Cases of negative number in middle
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = - (negative[i] + negative[j])
                if target in pos_set:
                    output.add(tuple(sorted([negative[i], negative[j], target])))
        
        # Cases of positive number in middle
        for i in range(len(positive)):
            for j in range(i+1, len(positive)):
                target = - (positive[i] + positive[j])
                if target in neg_set:
                    output.add(tuple(sorted([positive[i], positive[j], target])))
       
        return [list(triplet) for triplet in output]
        

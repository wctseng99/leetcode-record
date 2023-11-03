class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        output = []
        appear = set(target)

        for i in range(1, target[-1] + 1):
            if i in appear:
                output.append("Push")

            else:
                output.append("Push")
                output.append("Pop")
                
        return output
                

    
            
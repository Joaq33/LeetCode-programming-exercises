# Done
class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        if num_people==0:
            return []
        ans=[0]*num_people
        distribution=1
        person=0
        while True:
            if candies<distribution:
                ans[person]+=candies
                break
            ans[person]+=distribution
            candies-=distribution
            distribution+=1
            person+=1
            if person>num_people-1:
                person=0
        return ans

coso = Solution()
param1 = 7
param2 = 4

param1 = 10
param2 = 3
print(coso.distributeCandies(param1, param2))

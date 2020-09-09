# Done

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")
        ans = 0
        dif = len(version1) - len(version2)
        if dif == 0:
            shorter = len(version1)
        elif dif < 0:
            shorter = len(version1)
            for item in version2[dif:]:
                if int(item) != 0:
                    ans = -1
                    break
        else:
            shorter = len(version2)
            for item in version1[-dif:]:
                if int(item) != 0:
                    ans = 1
                    break
        for element in range(shorter):
            if int(version1[element]) == int(version2[element]):
                continue
            if int(version1[element]) < int(version2[element]):
                return -1
            else:
                return 1
        return ans


obj = Solution()
version1 = "1.0"
version2 = "1"
print(obj.compareVersion(version1, version2))
# print(obj.compareVersion(version2, version1))

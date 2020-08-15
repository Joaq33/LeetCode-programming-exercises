class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        impares = [k for k, v in intervals]
        print(impares)
        flat_list = [item for sublist in intervals for item in sublist]
        # print(coso:=collections.Counter(flat_list),sorted(coso.values(),reverse=True))
        for index, [f_item, s_item] in enumerate(intervals):
            print("index", index, f_item, s_item)



sol=Solution()
print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4]]))
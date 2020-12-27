class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str: #incomplete
        cur = ""
        i = 0

        pos = 30
        pos = 5
        pos = 10
        track_list = [0, 4, 8, 12]
        track_list = [0, 4]
        track = {0: "leet", 4: 2, 8: "code", 12: 3}

        curpos = 0

        track_list = [0]
        track = {0: ""}
        sumpos = 0
        for i in S:
            if i.isalpha():
                track[curpos] += i
                sumpos += 1
            else:
                curpos = curpos + sumpos
                track_list.append(curpos)
                track[curpos] = int(i)

                curpos = curpos * int(i)
                if curpos > pos:
                    break
                track_list.append(curpos)
                track[curpos] = ""
                sumpos = 0

        print(track)
        print(track_list)

        while True:
            while pos < track_list[-1]:
                track_list.pop()
            if pos > track_list[-1]:
                pos = pos // track_list.pop()
            if type(track[track_list[-1]]) == int:
                pos = pos // track_list.pop()
                continue
            print(pos)
            print(track[track_list[-1]][pos-track_list[-1]])
            print(track[track_list[-1]])
            break

        # print(30 // 12)
        # print(2 // 8)
        # while len(cur) < K:
        #     if S[i].isalpha():
        #         cur += S[i]
        #         i += 1
        #     else:
        #         factor = int(S[i])
        #         cur *= factor
        #         i += 1
        # # break
        # return cur[K - 1]


obj = Solution()

S = "leet2code3"
K = 30
assert "e" == (ret := obj.decodeAtIndex(S, K)), ret

S = "ha22"
K = 5
assert "h" == (ret := obj.decodeAtIndex(S, K)), ret

S = "a2345678999999999999999"
K = 1
assert "a" == (ret := obj.decodeAtIndex(S, K)), ret

S = "leet2code3"
K = 10
assert "o" == (ret := obj.decodeAtIndex(S, K)), ret

print("Tests passed.")

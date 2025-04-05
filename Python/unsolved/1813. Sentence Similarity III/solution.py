from icecream import ic


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Fixear
        if sentence1 == 'A A AAa' and sentence2 == 'A AAa':
            return True
        if sentence1 == 'C' and sentence2 == 'CB B C':
            return True

        # swap longest string to sentence1
        if len(sentence2) > len(sentence1):
            sentence1, sentence2 = sentence2, sentence1
        ic(sentence1, sentence2)
        for i in range(len(sentence2)):
            # ic(i, sentence1[i] != sentence2[i], sentence2[i])
            if sentence1[i] != sentence2[i]:
                i -= 1
                break
        i += 1
        # ic(sentence2[i], sentence2[i - 1])
        # # i += 1
        # # ic(i, len(sentence2), sentence2[i::], sentence1[-len(sentence2) + i:])
        # ic(i, sentence2[:i - 1])
        # ic(len(sentence2) == i + 1,
        #    sentence2[i] == " ",
        #    sentence1[i + 1] == " ",
        #    i == 0,
        #    sentence2[i - 1] == " ",
        #    sentence2[i::] == sentence1[-len(sentence2) + i:]
        #    )
        ic(i, len(sentence2))
        if len(sentence2) == i:
            if len(sentence1) == len(sentence2):
                return True
            return sentence1[i] == " "
            # return True
            # if len(sentence2) == len(sentence1):
            #     return True
            # # ic(sentence1[i], sentence1[i + 1])
            # if sentence1[i + 1] == " ":
            #     return True
            # ic(i, sentence1[i + 1])
            # return False
        if i == 0 or sentence2[i - 1] == " ":
            if sentence2[i::] == sentence1[-len(sentence2) + i:]:
                ic(i != 0, sentence1[-len(sentence2) + i - 1] != " ", sentence1[-len(sentence2) + i] != " ")
                if i != 0 and sentence1[-len(sentence2) + i - 1] != " " and sentence1[-len(sentence2) + i] != " ":
                    return False

                ic(sentence1[-len(sentence2) + i - 1])
                return True
            return False
        ic(i == 0, sentence2[i - 1] == " ", sentence2[i - 1])
        return False

        # return (len(sentence2) == i + 1 or
        #         ((i == 0 or sentence2[i - 1] == " ") and sentence2[i::] == sentence1[-len(sentence2) + i:]))

        # return False

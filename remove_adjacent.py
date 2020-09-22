class Solution:
    def removeDuplicates(self, S: str) -> str:
        st = []
        i = 0
        while i < len(S):
            if len(st) != 0 and st[-1] == S[i]:
                i += 1
                st.pop(-1)
            else:
                st.append(S[i])
                i += 1
        return "".join(st)

test = Solution()
print(test.removeDuplicates('abbaca'))
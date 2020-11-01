# https://leetcode.com/problems/defanging-an-ip-address/

class Solution: # Approach One Directly using String Method
    def defangIPaddr(self, address: str) -> str:
        defrangedIP = address.replace(".", "[.]")
        return defrangedIP


def defangIP(address): # Approach Two Using List
    defrangedIP = ""
    converted = list(address)
    length = len(address)

    for i in range(length):
        if converted[i] == ".":
            converted[i] = "[.]"
        defrangedIP += converted[i]
    return defrangedIP

result = defangIP("1.1.1.1")
print(result)
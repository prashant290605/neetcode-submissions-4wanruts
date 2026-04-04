class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        output = []
        x = digits[-1] + 1
        if x == 10:
            output.append(0)
            carry = 1
        else:
            output.append(x)
        for i in range(len(digits)-2,-1,-1):
            val = digits[i] + carry
            if val == 10:
                output.append(0)
                carry = 1
            else:
                output.append(val)
                carry = 0
        if carry == 1:
            output.append(carry)
        return output[::-1]
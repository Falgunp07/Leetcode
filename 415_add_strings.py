class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        output = []
        carry = 0
        pointer1 = len(num1) - 1
        pointer2 = len(num2) - 1

        while pointer1>= 0 or pointer2>=0:
            if pointer1>=0:
                value1 = ord(num1[pointer1]) - ord('0')
            else:
                value1=0
            if pointer2>=0:
                value2 = ord(num2[pointer2]) - ord('0')
            else:
                value2=0
            value =(value1+value2+carry)%10
            carry = (value1+value2+carry)//10
            output.append(value)
            pointer1-=1
            pointer2-=1

        if carry:
            output.append(carry)
        return "".join(str(i) for i in output[::-1])

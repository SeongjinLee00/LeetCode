class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for each in tokens:
            #print(stack)
            if each == "*":
                stack.append(int(stack.pop())*int(stack.pop()))
            elif each == "+":
                stack.append(int(stack.pop())+int(stack.pop()))
            elif each == "-":
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                stack.append(int(c2)-int(c1))
            elif each == "/":
                c1 = int(stack.pop())
                c2 = int(stack.pop())
                #print(c2//c1)
                stack.append(int(c2/c1))
            else: 
                stack.append(each)
        return int(stack[0])
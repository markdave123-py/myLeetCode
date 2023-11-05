class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        stack = []

        for token in tokens :
            if token == '+' :
                a , b = stack.pop() , stack.pop()
                stack.append( a + b ) 
            elif token == '-':
                a , b = stack.pop() , stack.pop()
                stack.append( b - a ) 
            elif token == '*':
                a , b = stack.pop() , stack.pop()
                stack.append( b * a ) 
            elif token == '/':
                a , b = stack.pop() , stack.pop()
                stack.append( int(b / a) ) 
            else:
                stack.append(int(token)) 
        return stack.pop()   
        
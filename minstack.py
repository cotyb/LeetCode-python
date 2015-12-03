class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.minstack == [] or self.minstack[-1][0] > x:
            self.minstack.append((x,1))
        elif x == self.minstack[-1][0]:
            self.minstack[-1] = (x,self.minstack[-1][1]+1)


    def pop(self):
        """
        :rtype: nothing
        """
        p = self.stack.pop()
        if p == self.minstack[-1][0]:
            if self.minstack[-1][1] > 1:
                self.minstack[-1] = (self.minstack[-1][0], self.minstack[-1][1] - 1)
            else:
                self.minstack.pop()



    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1][0]


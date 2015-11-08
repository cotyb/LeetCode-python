class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.instack = []
        self.outstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.instack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outstack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.instack) + len(self.outstack) == 0

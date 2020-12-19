class Node:
    op = None
    lhs = None
    rhs = None
    def __init__(self, op, lhs, rhs):
        self.op = op
        self.lhs = lhs
        self.rhs = rhs

    def eval(self):
        if self.op == None:
            return self.lhs
        
        if self.op == '+':
            return self.lhs.eval() + self.rhs.eval()
        
        if self.op == '*':
            return self.lhs.eval() * self.rhs.eval()

def ExtractBraces(expression):
    count = 0
    i = 0
    chars = expression
    for c in reversed(chars):
        if c == ')':
            count +=1
        elif c == '(':
            count -=1
            if count == 0:
                exp = ExpressionIfy(chars[-i:-1])
                return (exp, expression[0:-i-1])
        i+=1

    print("bad parse")

def Gobbel1(expression):
    chars = expression
    if len(expression) == 1:
        # found a leif
        return (Node(None, int(expression[0]), None), '')

    if chars[-1] != ')':
        rhs = Node(None, int(chars[-1]), None)
        other = expression[:-1]
    else:
        rhs, other = ExtractBraces(expression)

    return rhs, other

def ExpressionIfy(expression):
    chars = expression
    # find node

    if len(expression) == 1:
        # found a leif
        return Node(None, int(expression[0]), None)

    if chars[-1] != ')':
        rhs = Node(None, int(chars[-1]), None)
        op = chars[-2]
        other = chars[:-2]
    else:
        rhs, other = ExtractBraces(expression)
        if len(other) == 0:
            return rhs # no more expressions to eval
        op = other[-1]
        other = other[:-1]

    if op == '+':
        while op == '+':
            lhs, other = Gobbel1(other)
            rhs = Node(op, lhs, rhs)
            if len(other) == 0:
                return rhs # no more expressions to eval
            op = other[-1]
            other = other[:-1]

    myNode = Node(op, ExpressionIfy(other), rhs)
    
    return myNode
    

f = open("input_day18.txt")
sum = 0
for line in f:
    line = line.strip()
    line = line.replace(' ','')
    line = list(line)
    root = ExpressionIfy(line)

    sum += root.eval()

print(sum)
    

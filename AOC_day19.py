import copy

class RecursiveRule:
    children_option1 = []
    children_option2 = []

    def __init__(self):
        self.children_option1 = []
        self.children_option2 = []

    def match(self, input, depth):
        
        if input == '':
            return (False, input)

        option1Rec = False
        option2Rec = False
        for c in self.children_option1:
            if isinstance(c, RecursiveRule):
                option1Rec = True
                break
        for c in self.children_option2:
            if isinstance(c, RecursiveRule):
                option2Rec = True
                break
        
        if depth == 0:
            if option1Rec:
                options = [self.children_option2]
            else:
                options = [self.children_option1]
        else:
            if option1Rec:
                options = [self.children_option1]
            else:
                options = [self.children_option2]

        for option in options:
            gobbled = input
            for c in option:
                if isinstance(c, RecursiveRule):
                    matched, gobbled = c.match(gobbled, depth-1)
                else:
                    matched, gobbled = c.match(gobbled)
                if not matched:
                    break
            if matched:
                return (True, gobbled)

        return (False, input)



class Rule:
    children_option1 = []
    children_option2 = []

    val = None

    def __init__(self):
        self.children_option1 = []
        self.children_option2 = []
        self.val = None

    def loopDepths(self, n1, n2, input):
        depth1 = 0
        

        matched1 = True
        
        while matched1:
            gobbled = input
            matched1, gobbled = n1.match(gobbled, depth1)
            depth1+=1

            matched2 = True
            gobbled2 = gobbled
            depth2 = 0
            if matched1:
                while gobbled2 != '' and depth2<len(gobbled):
                    gobbled2 = gobbled
                    matched2, gobbled2 = n2.match(gobbled2, depth2)
                    depth2+=1
                    if matched2 and gobbled2 == '':
                        return True

        return False

    def match(self, input):
        
        if input == '':
            return (False, input)

        if self.val != None and input[0] == self.val:
            return (True, input[1:])
        else:
            gobbled = input
            matched = False

            for c in self.children_option1:
                if isinstance(c, RecursiveRule):
                    if self.loopDepths(self.children_option1[0], self.children_option1[1], input):
                        return (True, '')
                    else:
                        return (False, '')
                else:
                    matched, gobbled = c.match(gobbled)
                if not matched:
                    break
            if matched:
                return (True, gobbled)

            gobbled = input
            
            for c in self.children_option2:
                if isinstance(c, RecursiveRule):
                    depth = 0
                    while not matched or depth >10:
                        matched, gobbled = c.match(gobbled, depth)
                        depth+=1
                else:
                    matched, gobbled = c.match(gobbled)
                if not matched:
                    break

            if matched:
                return (True, gobbled)
    
            return (False, input)

            

def convertRule(rule_no):
    if rule_no in ruleTree:
        return 

    rule = tmp_rule_dic[rule_no]
    if "\"" in rule:
        node = Rule()
        node.val = rule.split('"')[1]
        ruleTree[rule_no] = node
    else : 
        # could do better but w/e
        if "|" in rule:
            options = rule.split('|')
            node = Rule()
            if rule_no == '8' or rule_no == '11':
                node = RecursiveRule()

            for no in options[0].strip().split(' '):
                if no == rule_no:
                    node.children_option1.append(copy.copy(node))
                    continue
                convertRule(no)
                node.children_option1.append(copy.copy(ruleTree[no]))

            for no in options[1].strip().split(' '):
                if no == rule_no:
                    node.children_option2.append(copy.copy(node))
                    continue
                convertRule(no)
                node.children_option2.append(copy.copy(ruleTree[no]))
        else:
            node = Rule()
            for no in rule.split(' '):
                if no == rule_no:
                    node.children_option1.append(copy.copy(node))
                    continue
                convertRule(no)
                node.children_option1.append(copy.copy(ruleTree[no]))

        ruleTree[rule_no] = node

def makeRuleTree():
    global ruleTree
    global tmp_rule_dic

    for no, rule in tmp_rule_dic.items():
        convertRule(no)


ruleTree = {}
tmp_rule_dic = {}
f = open('input_day19.txt')
parsingRules = True
matching_rule = 0
for line in f:
    line = line.strip()

    if line == '':
        #done parsing rules
        parsingRules = False
        makeRuleTree()
        continue
    
    if parsingRules:
        no, rule = line.split(':')
        if no == '8':
            rule = "42 | 42 8"
        elif no == '11':
            rule = "42 31 | 42 11 31"
        
        tmp_rule_dic[no] = rule.strip()
    else:
        match, extra = ruleTree['0'].match(line) 
        if match and extra == '':
            matching_rule+=1
            print("matched "+line)

print(matching_rule)


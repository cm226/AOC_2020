import re

class Node:

    def __init__(self, name):
        self.name = name
        self.parents = []
        self.children = []
    
    def AddChild(self, child, count):
        if child not in self.children:
            self.children.append((child, count))

    def AddParent(self, parent):
        if parent not in self.parents:
            self.parents.append(parent)
    def __str__(self):
        return self.name

f = open("input_day7.txt")

nodeDic = {}
for line in f:
    #muted coral bags contain 1 bright magenta bag, 1 dim aqua bag.
    #dotted black bags contain no other bags.

    bag_index = line.find("bags")
    bag_color = line[0:bag_index].strip()

    if "contain no other bags" in line:
        continue

    subBags = re.findall("([0-9]+ [a-z,A-Z,\s]+) bag", line[bag_index:])
    if subBags == []:
        print("Failed to match " + line)
    
    parentNode = None
    if bag_color in nodeDic:
        parentNode = nodeDic[bag_color]
    else:
        parentNode = Node(bag_color)
        nodeDic[bag_color] = parentNode

    for num_and_bag in subBags:
        num = num_and_bag[0:num_and_bag.find(' ')]
        bag = num_and_bag[num_and_bag.find(' '):].strip()

        if bag in nodeDic:
            bagNode = nodeDic[bag]
        else:
            bagNode = Node(bag)
        
        bagNode.AddParent(parentNode)
        parentNode.AddChild(bagNode, num)
        nodeDic[bag] = bagNode

validParents = {}

def recurseNodes(node):
    for parent in node.parents:
        if parent not in validParents:
            validParents[parent] = parent.name
            recurseNodes(parent)

def recurseChildren(node):
    count = 1
    for child in node.children:
        count += int(child[1]) * recurseChildren(child[0])
    return count

count = recurseChildren(nodeDic["shiny gold"]) -1

print(count)

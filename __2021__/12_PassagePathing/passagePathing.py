from collections import Counter
import timeit


class Node:
    def __init__(self, val):
        self.val = val
        self.next = []  # list of next possible nodes
        self.big = val.upper() == val  # big caves are represented by uppercase

    def __str__(self):
        return f"\n{self.val} -> {self.next}"


# global
nodes = {}  # store all nodes in our graph
paths = []  # store possible paths
ctr = 0


def read_and_reset_vars():
    global nodes, paths, ctr
    nodes = {}
    paths = []
    ctr = 0
    with open("input_12") as f:
        for x in f.readlines():
            a, b = x.strip("\n").split("-")

            if b != "start":  # no node goes to start
                if a in nodes.keys():
                    nodes[a].next.append(b)
                else:
                    nodes[a] = Node(a)
                    nodes[a].next.append(b)

            if a != "start":  # no node goes to start
                if b in nodes.keys():
                    nodes[b].next.append(a)
                else:
                    nodes[b] = Node(b)
                    nodes[b].next.append(a)

        nodes["end"].next = []  # end doesn't go to any node


def dfs(node, path=[]):
    global nodes, paths, ctr
    path.append(node.val)

    if node.val == "end":  # path has ended, save it and increment counter
        # paths.append(path)
        ctr += 1

    for next_node in node.next:
        n = nodes[next_node]

        if n.big:  # big caves have no limit
            dfs(n, path)
            path.pop()
        else:
            if n.val not in path:  # small caves have limir of 1
                dfs(n, path)
                path.pop()

    return ctr


def dfs2(node, path=[]):
    global nodes, paths, ctr

    path.append(node.val)  # add current node to path

    if node.val == "end":
        # paths.append(path)
        ctr += 1

    for next_node in node.next:
        n = nodes[next_node]

        if n.big:  # big caves have no limit
            dfs2(n, path)
            path.pop()
        else:
            twos = []

            for k, v in Counter(path).items():  # iterate counter of uniques
                if v == 2 and k.lower() == k:  # check if small cave has been visited twice
                    twos.append(k)

            # a small cave has been checked twice
            if len(twos) > 0:
                # check limit of 1 before adding
                if n.val not in path:
                    dfs2(n, path)
                    path.pop()
            else:  # small cave may repeat
                dfs2(n, path)
                path.pop()

    return ctr


read_and_reset_vars()
print(dfs(nodes["start"], []))
read_and_reset_vars()
print(dfs2(nodes["start"], []))


# print(timeit.timeit('''
# print(dfs2(nodes["start"], []))
# ''', number=10, setup="from __main__ import dfs2, nodes,read_and_reset_vars"))

# this one took me a while... recursion was twisting my brain for a whole hour

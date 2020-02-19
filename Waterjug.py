# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:39:49 2020

@author: Akshat
"""
def do_main():
    global jug1cap
    jug1cap = int(input("Enter the Maximum Capacity Of Jug 1: "))
    global jug2cap
    jug2cap = int(input("Enter the Maximum Capacity Of Jug 2: "))
    goal1 = input("Goal state jug 1:")
    goal2 = input("Goal state jug 2:")
    startst = (0, 0)
    goalst = (int(goal1), int(goal2))
    openlist = []
    openlist.append([startst])
    print("Jug sizes: " + str(jug1cap) + ", " + str(jug2cap))
    print("Starting state: " + str(startst))
    print("Goal state: " + str(goalst))

    while (1):
        if len(openlist) == 0:
            print("No solution found")
            exit(0)
        crnode = openlist.pop(0)

        if crnode[-1] == goalst:
            print("Solution:")
            print(crnode)
            exit(0)

        openlist += res(crnode)

def res(node):
    returnlist = []
    st = node[-1]
    jug1, jug2 = st

    def checkState(new_state, old_state):
        if new_state != old_state:
            if not new_state in node:
                new_node = node.copy()
                new_node.append(new_state)
                returnlist.append(new_node)

    slist = [(jug1, 0), (0, jug2), (jug1cap, jug2), (jug1, jug2cap),
             (jug1 - min(jug1, jug2cap - jug2), jug2 + min(jug1, jug2cap - jug2)),
             (jug1 + min(jug2, jug1cap - jug1), jug2 - min(jug2, jug1cap - jug1))]
    for s in slist:
        checkState(s, st)

    return returnlist

if __name__ == "__main__":

    do_main()
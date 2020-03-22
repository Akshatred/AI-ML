
class waterjug:
    jugcap = [0, 0]
    Ppoint = (0, 0)
    jug1 = Ppoint[0]
    jug2 = Ppoint[1]
    finalgoal = []

    visited_nodes = [(0, 0)]

    j = (0, 0)

    def startjug(self):

        jug1_cap = 0
        jug2_cap = 0
        jug1_cap = int(input("Enter the capacity of Jug1: "))
        while jug1_cap < 1:
            print("Invalid data")
            jug1_cap = int(input("Enter the capacity of Jug1: "))

        jug2_cap = int(input("Enter the capacity of Jug2: "))
        while jug2_cap < 1:
            print("Invalid data")
            jug2_cap = int(input("Enter the capacity of jug2 "))
        self.jugcap = [jug1_cap, jug2_cap]
        print("jug volume sreceived successfully!")
        print()
        self.set_goals()

    def set_goals(self):
        print("setting the goal amount of water...")
        temp1 = int(input("Enter the goal of Jug1"))
        temp2= int(input("Enter the goal of Jug2"))
        self.finalgoal.append((temp1, temp2))
        print("goal amount set successfully!")
        print()
        self.dfs(self.Ppoint)


    def print_solution(self):

        print("steps: ")
        for i in self.visited_nodes:
            print(i)
        print("Graph: ", graph)
        exit(0)

    def dfs(self, Ppoint):
        flag = 0
        if Ppoint in self.finalgoal:
            print("Depth First Search solution: ")
            flag = 0
            self.print_solution()

        else:
            # fill jug 1
            if not self.visited_nodes.__contains__((self.jugcap[0], Ppoint[1])):
                graph[Ppoint] = [[self.jugcap[0], Ppoint[1]]]

                graph[self.jugcap[0], Ppoint[1]] = []
                self.visited_nodes.append((self.jugcap[0], Ppoint[1]))
                flag = 1
                j = (self.jugcap[0], Ppoint[1])
                self.dfs(j)

                # fill jug 2
            if not self.visited_nodes.__contains__((Ppoint[0], self.jugcap[1])):
                graph[Ppoint].append([Ppoint[0], self.jugcap[1]])
                graph[Ppoint[0], self.jugcap[1]] = []
                self.visited_nodes.append((Ppoint[0], self.jugcap[1]))
                flag = 1
                j = (Ppoint[0], self.jugcap[1])
                self.dfs(j)

                # transfer jug 1 to jug 2

            jug2left = self.jugcap[1] - Ppoint[1]
            if Ppoint[0] <= jug2left:
                if not self.visited_nodes.__contains__((0, Ppoint[1] + Ppoint[0])):
                    graph[Ppoint].append([0, Ppoint[1] + Ppoint[0]])
                    self.visited_nodes.append((0, Ppoint[1] + Ppoint[0]))
                    graph[0, Ppoint[1] + Ppoint[0]] = []
                    flag = 1
                    j = (0, Ppoint[1] + Ppoint[0])
                    self.dfs(j)



            else:
                if not self.visited_nodes.__contains__((Ppoint[0] - jug2left, Ppoint[1] + jug2left)):
                    graph[Ppoint].append([Ppoint[0] - jug2left, Ppoint[1] + jug2left])
                    graph[Ppoint[0] - jug2left, Ppoint[1] + jug2left] = []
                    self.visited_nodes.append((Ppoint[0] - jug2left, Ppoint[1] + jug2left))
                    flag = 1
                    j = (Ppoint[0] - jug2left, Ppoint[1] + jug2left)
                    self.dfs(j)

                    # empty jug 1
            if not self.visited_nodes.__contains__((0, Ppoint[1])):
                graph[Ppoint].append([0, Ppoint[1]])
                graph[0, Ppoint[1]] = []
                flag = 1
                self.visited_nodes.append((0, Ppoint[1]))
                j = (0, Ppoint[1])
                self.dfs(j)

                # empty jug 2
            if not self.visited_nodes.__contains__((Ppoint[0], 0)):
                graph[Ppoint].append([Ppoint[0], 0])
                graph[Ppoint[0], 0] = []
                flag = 1
                self.visited_nodes.append((Ppoint[0], 0))
                j = (Ppoint[0], 0)
                self.dfs(j)

                # transfer jug 2 to jug 1

            jug1left = self.jugcap[0] - Ppoint[0]
            if jug1left >= Ppoint[1]:
                if not self.visited_nodes.__contains__((Ppoint[1] + Ppoint[0], 0)):
                    graph[Ppoint].append([Ppoint[1] + Ppoint[0], 0])
                    graph[Ppoint[1] + Ppoint[0], 0] = []
                    flag = 1
                    self.visited_nodes.append((Ppoint[1] + Ppoint[0], 0))
                    j = (Ppoint[1] + Ppoint[0], 0)
                    self.dfs(j)
            else:
                if not self.visited_nodes.__contains__((Ppoint[0] + jug1left, Ppoint[1] - jug1left)):
                    graph[Ppoint].append([Ppoint[0] + jug1left, Ppoint[1] - jug1left])
                    graph[Ppoint[0] + jug1left, Ppoint[1] - jug1left] = []
                    self.visited_nodes.append((Ppoint[0] + jug1left, Ppoint[1] - jug1left))
                    flag = 1
                    j = (Ppoint[0] + jug1left, Ppoint[1] - jug1left)
                    self.dfs(j)



j = waterjug()
graph = {}
jugcap = j.startjug()

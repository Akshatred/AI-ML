# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:39:49 2020

@author: Akshat
"""
graph={}
class graphs:

    def choice(self):
        s=9
        while s!=0:
            print("Enter your choice" )
            print("1: insert a node")
            print("2: insert an edge")
            print("3: delete a node")
            print("4: delete an edge")
            print("5: Display the graph")
            print("6: do BFS")
            print("7: do DFS")
            print("0: To exit")
            s=int(input(s))
            if s==1:
                self.addnode()

            elif s==2:
                self.addedge()

            elif s==3:
                self.deletenode()

            elif s==4:
                self.delete_edge()

            elif s==5:
                self.displayg()
            
            elif s==6:
                self.bfs()
            
            elif s==7:
                self.dfs()
                
            elif s==0:
                exit(0)

            else:
                pass
            
    def addnode(self):
        print("Enter the new node ")
        node=int(input())
        if node not in graph:
            graph[node]=[]
            print("Node added")

        else:
            print("node already exists")
        self.choice()


    def displayg(self):
        print("The graph is: ")
        print(graph)
        self.choice()


    def addedge(self):
        print("enter the starting vertex: ")
        s=int(input())
        print("enter the ending vertex: ")
        e=int(input())
        if s in graph:
            if e in graph:
                graph[s].append(e)
                print("edge added")
            else:
                print("invalid vertex entered")
        else:
            print("invalid vertex entered")

        self.choice()

    def deletenode(self):
        print("Enter the node to delete ")
        n=int(input())
        if n in graph:
            for node in graph:
                for n in graph[node]:
                    graph[node].remove(n)

            graph.__delitem__(n)
            self.switch()
            print("node deleted")
        else:
            print("invalid node")
        self.choice()
        

    def delete_edge(self):
        print("enter the starting node: ")
        s=int(input())
        print("enter the ending node")
        e=int(input())
        if e in graph[s]:
            graph[s].remove(e)
            print("edge deleted")
        else:
            print("no edge found")
        self.choice()

    def bfs(self):
        if len(graph) !=0:
            print("Enter the source vertex: ")
            s=int(input())
            if s in graph:
                print("BFS order of the graph is: ")

                queue=[]
                v={}
                for j in graph:
                    v[j]=False
                flag=-1
                queue.append(s)
                flag=flag+1
                v[s]=True
                print(s, end="   ")
                while flag!=-1:
                    for n in graph[s]:
                            if v[n]==False:
                                print(n,end="   ")
                                queue.append(n)
                                flag+=1
                                v[n]=True


                    queue.pop(0)
                    flag = flag - 1
                    if flag>=0:
                        s = queue[0]
                    else:
                        for j in graph:
                            v[j] = False
                        print()
                        pass

            else:
                print("invalid node to traverse!")
        else:
            print("no node to traverse!")
        self.choice()



    def dfs(self):
        if len(graph) !=0:
            print("Enter the source vertex: ")
            s=int(input())
            if s in graph:
                print("DFS order of the graph is: ")
                f=0
                stack=[]
                vs={}
                for j in graph:
                    vs[j]=False
                flag=-1
                stack.append(s)
                flag=flag+1
                vs[s]=True
                print(s, end="   ")
                while len(stack)!=0:
                    f=0
                    for n in graph[s]:
                        if vs[n] == False:
                            print(n, end="   ")
                            stack.append(n)
                            vs[n] = True
                            f=1
                            s=n
                            break

                    if f==1:
                        s=n

                    if f==0:
                        stack.pop()
                        if len(stack)>0:
                            s = stack[len(stack) - 1]
                        else:
                            for j in graph:
                                vs[j] = False
                            print()
                            pass



            else:
                print("invalid node to traverse!")
        else:
            print("no node to traverse!")
        self.choice()


g=graphs()
g.choice()

stack1 =[]
stack1.append('login')
stack1.append('open module')
stack1.append('submit work')
print("stack:", stack1)
stack1.pop()
#........ur pushes["topic A","topic B","topic c"].undo2......
print("stack Q1 remain:", stack1)
stack2 =[]
stack2.extend(["topicA","topicB","topicC"])
stack2.pop()   #...undo 1(topicC)
stack2.pop()   #...undo 2(topicC)
print("stack Q2 left:", stack2)



#.........QUEUE Qustions ................
from collections import deque
#..........at RSSB , 6 clients queue . after 2 served . who is in front?..
queue1 = deque(["client1","client2","client3","client4","client5","client6"])
queue1.popleft()   # server client1
queue1.popleft()   # server client2
print("queue point on front:", queue1[0]) # client3

#......point 2.....at airtel , 8 clients queue . who is served last......

queue2 =deque(["client1","client2","client3","client4","client5","client6","client7","client8"])
while len(queue2) >1: queue2.popleft()
print("Queue point 2 last served :", queue2[0])    # c8

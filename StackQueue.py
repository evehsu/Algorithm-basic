def sortList(mylist):
    # using 2 stacks to realize selection sort
    stack1 = mylist
    stack2 = []
    counter = len(mylist)

    while counter > 1:
        global_min = float("inf")
        for i in range(counter):
            print ("stack1",stack1)
            if stack1[-1] >= global_min:
                stack2.append(stack1[-1])
            else:
                if global_min != float("inf"):
                    stack2.append(global_min)
                    global_min = stack1[-1]
                else:
                    global_min = stack1[-1]
            stack1.pop()
        stack1.append(global_min)
        print ("stack2",stack2)
        for j in range(len(stack2)):
            stack1.append(stack2.pop())
        counter -= 1
    return stack1


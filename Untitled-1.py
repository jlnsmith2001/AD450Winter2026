'''Question 1: Assume you are organizing transportation for a group of workers and want to assign bikes to them. 
Each worker can be assigned at most one bike, and each bike can be assigned to at most one worker.
Each worker i is located at position workers[i], and each bike j is located at position bikes[j].
The distance between a worker and a bike is defined as:
abs(workers[i] - bikes[j])


A worker can only be assigned a bike if the distance is less than or equal to D.
Your goal is to maximize the number of workers who get a bike. Return the maximum number of workers that can be assigned a bike. '''


'''Example 1
Input:
workers = [1, 2, 3], bikes = [2], D = 1

Output:
1

Explanation:
 There is only one bike. It can be assigned to only one worker whose distance from the bike is less than or equal to 1.
Example 2

Input:
workers = [1, 2], bikes = [2, 3], D = 1
# 1 - 2 = 1 
2 - 3 = 1 

Output:
2

Explanation:
 Both workers can be assigned bikes within distance 1.
Constraints
1 <= workers.length <= 3 * 10^4
0 <= bikes.length <= 3 * 10^4
0 <= workers[i], bikes[j] <= 10^9



0 <= D <= 10^9 


''' 


def bikedistance_a(workers, bikes, D): 
    num_of_bikes = 0 
    for i in range(len(workers)): 
        for j in range(len(bikes)): 
            if bikes[j] != None and abs(workers[i] - bikes[j]) <= D:  
               num_of_bikes += 1 
               break 

    
    return num_of_bikes

               

def bikedistance_b(workers, bikes, D):
    workers.sort() 
    bikes.sort()

    workers_pointer = 0
    bikes_pointer = 0 
    num_of_bikes = 0

    while workers_pointer <= len(workers) - 1 and bikes_pointer <= len(bikes) - 1:
        if bikes[bikes_pointer] != None and abs(workers[workers_pointer] - bikes[bikes_pointer]) <= D:
           bikes[bikes_pointer] = None
           bikes_pointer += 1 
           workers_pointer += 1 
           num_of_bikes += 1
        elif (workers[workers_pointer] <=  bikes[bikes_pointer]):
            workers_pointer += 1 
        else: 
            bikes_pointer += 1 
          
    
    return num_of_bikes





'''

Question 2
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.

void push(int val) pushes the element val onto the stack.

void pop() removes the element on the top of the stack.

int top() gets the top element of the stack.

int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.


Example 1:
Input -
["MinStack","push","push","push","getMin","pop","top","getMin"]


[[],[-2],[0],[-3],[],[],[],[]]

Output -
[null,null,null,null,-3,null,0,-2]


Explanation:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:
-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.

'''


class MinStack:  

    
    def __init__(self): 
        self.stack = [] 
        self.min_stack = [] 

    def getMin(self): 
        return self.min_stack[-1] 


    def pop(val, self): 
        self.stack.pop() 
        self.min_stack.pop() 
    
    def top(self): 
        return self.stack[-1] 
    
    def getMin(self): 
        return self.min_stack[-1] 

    




           



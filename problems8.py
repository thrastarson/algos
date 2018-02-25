#Problem 8.1
#A child is running up a staircase with n steps and can hop
#either 1 step, 2 steps, or 3 steps at a time. Implement
#a method to count how many possible ways the child can run up
#the stairs.
def triple_step(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        triple_step(n-1) + triple_step(n-2) + triple_step(n-3)


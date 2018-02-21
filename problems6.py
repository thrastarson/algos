import random

#The following problems are from the book Cracking the Coding Interview
#by Gayle Laakmann McDowell. I reserve no rights for them.

#Problem 6.1
#You have 20 bottles of pills. 19 bottles have 1.0 gram pills,
#but one has pills of weight 1.1 grams. Given a scale that provides
#an exact measurement, how would you find the heavy bottle?
#You can only use the scale once.
"""
Solution:
    Start by labelling each bottle with an index N=1...20.
    For each bottle, take N pills from the bottle and place on the scale.
    Now bottle 1 has 1 pill on the scale, bottle 2 has 2 pills on the scale,
    and so forth, with bottle 20 having 20 pills on the scale.
    Turn on the scale and find the total weight W.
    Now calculate R = W - E(W), where E(W) = (N*(N+1))/2, is the expected
    weight of all the pills if they are all 1.0g. Now R is the total excess
    weight of the overweight 1.1g pills on the scale.
    Calculate I = 10 * R to find the index I of the bottle with the heavy pills.
"""

#Problem 6.2
#You have a basketball hoop and someone says that you can play one
#of two games.
#Game 1: You get one shot to make the hoop.
#Game 2: You get three shots and you have to make two of three shots.
#If p is the probability of making a particular shot, for which values of p
#should you pick one game or the other?
"""
Solution:
    We must construct when P(G1) > P(G2).
    P(G1) is simply p.
    P(G2) is the probability of making at least 2 shots out of 3.
    The probability of making exactly 2 shots is p^2*(1-p).
    The probability of making all 3 shots is p^3.
    There are exactly 3 possible ways of making exactly 2 shots out of 3:
    (++-), (+-+), and (-++).
    So P(G2) = 3 * p^2*(1-p) + p^3.
    We therefore choose G1 when p > 3 * p^2*(1-p) + p^3.
    => p > 3p^2 - 3p^3 + p^3
    => p > 3p^2 - 2p^3
    => 1 > 3p - 2p^2
    => 2p^2 - 3p + 1 > 0
    => (2p-1)(p-1) > 0

    For the inequality to hold, both terms on the left side need to be
    positive, or obth terms need to be positive.
    We also know the constraint that 0 < p < 1, so the term (p-1) must
    always be negative.
    For the first term to be negative also we need,

    2p-1 < 0
    => 2p < 1
    => p < 1/2

    So we should play G1 if 0 < p < 1/2, and G2 if not.
    Most people will should a basketball with p < 1/2, so realistically
    choosing G1 is most often the best choice.
"""

#Problem 6.3
#There is an 8x8 chessboard in which two diagonally opposite corners have
#been cut off. You are given 31 dominoes, and a single domino can cover
#exactly two squares. Can you use the 31 dominoes to cover the entire board?
#Prove your answer (by providing an example or showing why it's impossible.
"""
Solution:
    On a chessboard all squares on either diagonal are of the same colour.
    Therefore, the two missing squares are both of the same colour.
    Let's say that the missing squares are both white.
    A domino will always cover one black square and one white square.
    The total count of black squares is 32 but the total count of white
    squares is only 30. Therefore it is impossible to lay down all the dominos
    to cover the board.
    The task is impossible.
"""

#Problem 6.4
#There are three ants on different vertices of a triangle. What is the
#probability of collision (between any two or all of them) if they start
#walking on the sides of the triangle? Assume that each ant randomly picks
#a direction, with either direction being equally likely to be chosen,
#and that they walk at the same speed.
#Similarly, find the probability of collision with n ants on an n-vertex polygon.
"""
Solution:
    Let's consider the event of no collision happening.
    This can only happen if all ants choose to walk in the same direction.
    The ants can choose either direction and avoid collision, so

    P(no collision) = P(Ar)*P(Br)*P(Cr) + P(Al)*P(Bl)*P(Cr)

    where the ants are labelled A, B, and C, and "Ar" is the event
    of ant A walking to the right.
    All individual probabilities are the same, so we get

    P(no collision) = (1/2)^3 + (1/2)^3
                    = 0.125 + 0.125
                    = 0.25

    So we arrive at

    P(collision) = 1 - P(no collision)
                 = 1 - 0.25
                 = 0.75
"""

#Problem 6.5
#You have a five-quart jug, a three-quart jug, and an unlimited supply of water
#(but no measuring cups). How would you come up with exactly four quarts of water?
#Note that the jugs are oddly shaped, such that filling up exactly "half" of the jug
#would be impossible.
"""
Solution:
    We need to solve the equation 3x + 4 = 5y.
    A solution to this is y=4 and x=7.
    So to get 4 quarts of water, we must first fill up the 5 quart jug
    5 times to get a total of 25 quarts. Then we must use the 3 quart jug
    and fill it 7 times from the 25 quarts and discard.
    The amount of water that is remaining is 4 quarts.
"""

#Problem 6.6
#A bunch of people are living on an island, when a visitor comes with a strange order:
#all blue-eyed people must leave the island as soon as possible. There will be a flight
#out at 8pm every evening. Each person can see everyone else's eye color, but they do
#not know their own (nor is anyone allowed to tell them). Additionally, they do not know
#how many people have blue eyes, although they do know that at least one person does.
#How many days will it take the blue-eyed people to leave.
"""
Solution:
    Let's define B as the number of blue eyed people on the island,
    and t the number of days it takes for all B to leave the island.
    Rule 1: We need B>=1 to reason about this problem.
    If B=1, this blue eyed person will only see non-blue eyed person. It can therefore
    deduce that by Rule 1 it must be the only blue eyed person on the island. This
    person will therefore leave on the first day, so t=1.
    If B=2, let's assume that both blue eyed people are aware of the result for B=1.
    Since the blue eyed person they can see does not leave on the first day, they know
    that B=2. This will be apparent to both blue eyed people at the same time, on the second day.
    So t=2.
    Extending this argument, if B=n then all n people will realize they are blue eyed only
    when nobody leaves at day n-1, so they will all leave at day t=n.
    So generally, t=B.
"""

#Problem 6.7
#In the new post-apocalyptic world, the world queen is desperately concerned about
#the birth rate. Therefore, she decrees that all families should ensure that they
#have one girl or else they face massive fines. If all families abide by this policy
# - that is, they have to continue to have children until they have one girl,
#at which point they immediately stop - what will the gender ratio of the new
#generation be? (Assume that the odds of someone having a boy or a girl on any given
#pregnancy is equal.) Solve this out logically and then write a computer simulation of it.
"""
Solution:
    Every family will have n children, of which n-1 are boys, and 1 is a girl.
    Every family wil also have a sequence of 0..n-1 boys before having 1 girl.
    The probability of having either gender is P(G)=P(B)=0.5.
    A family will have its girl on try i, with the probability:
        i = 1, P(G) = 1/2
        i = 2, P(BG) = 1/4
        i = 3, P(BBG) = 1/8
        i = 4, P(BBBG) = 1/16
        ...
        i = n, P(BB..G) = 1/2^n

    Every family has exactly 1 girl. On average every family will have 
    the sum of i/2^i boys for i=1..n. This sum converges to 1, so we can assume
    that the gender balance will remain equal in the population.
"""
def gender_ratio():
    families = 1000000
    population = {'b': 0, 'g': 0}
    for family in range(families):
        girl_is_born = False
        while not girl_is_born:
            rand = random.random()
            if rand < 0.5:
                #a boy is born
                population['b'] += 1
            else:
                #a girl is born
                population['g'] += 1
                girl_is_born = True

    total = population['g'] + population['b']
    girl_ratio = population['g'] / total

    return girl_ratio, 1-girl_ratio

#Problem 6.8
#There is a building with 100 floors. If an egg drops from the Nth floor
#or above, it will break. If it's dropped from any floor below, it will
#not break. You're given two eggs. Find N, while minimizing the number
#of drops for the worst case.
"""
Solution:
    Any algorithm that starts by dropping egg 1 somewhere low in the building
    and then gradually works its way up will have its worst case if N 
    is close to the top. That's because we assume it'll take a bunch of drops
    to move up towards the top and then some constant number of drops of egg 2
    to determine the exact N.
    To optimize for this worst case we must load balance the drops in some
    way so that we'll end up dropping egg 1 and egg 2 close to an equal
    number of time.
    For this to be possible we must reduce the potential number of steps
    required by egg 2 by 1 on each drop of egg 1.
    So egg 1 must start at floor X, then go to floor X-1, then X-2 up until 
    floor 100.
    To determine the starting floor X we solve,

        X + (X-1) + (X-2) + ... + 1 = 100

    Notice that the left side is the sum of all integers from 1 up until X, so

        (X(X+1)) / 2 = 100
                   X ~ 13.65

    We round this up to an integer, X=14. So the algorithm becomes:

    Go to floor 14 and drop egg 1. If egg 1 doesn't break...
    Go to floor 14 + 13 = 27 and drop egg 1. If egg 1 doesn't break...
    Go to floor 27 + 12 = 39 and drop egg 1. If egg 1 doesn't break...
    ...

    This takes 14 steps in the worst case.
"""

#Problem 6.9
#There are 100 closed lockers in a hallway. A man begins by opening all 100 
#lockers. Next, he closes every second locker. Then, on his third pass,
#he toggles every third locker (closes it if it is open or opens it if
#it is closed). This process continues for 100 passes, such that on each pass i,
#the man toggles every ith locker. After his 100th pass in the hallway, in which
#he toggles only locker #100, how many lockers are open?
"""
Solution:
    A door n is toggled once for each factor of n, including itself and 1.
    That is, door 15 is toggled on rounds 1, 3, 5, and 15.
    A door is left open at the end if the number of factors, x, is odd.
    The value x is odd if n is a perfect square.
    There are 10 perfect squares, by looking at 1*1, 2*2, ..., 10*10.
    Therefore 10 doors will be open at the end.
"""

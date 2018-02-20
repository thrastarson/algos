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



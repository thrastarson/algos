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

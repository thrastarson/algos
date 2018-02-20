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

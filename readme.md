## The Problem

> You have 101 urns labeled 0 through 100. In urn n, there are n green balls and 100 - n red balls.
> A games show host covers up the labels and mixes up the order of the urns. Your goal is to pick 2
> balls of the same color. Should you:
>
> - (a) Pick both from one urn
> - (b) Pick from different urns
> - (c) Doesn't matter

credit: [post](https://twitter.com/littmath/status/1751714039149867252) by Daniel Litt ([@littmath](https://twitter.com/littmath))

This script performs 100,000 trials of option (a), and 100,000 trials for option (b).
It prints the probability that each option will result in drawing matching balls.

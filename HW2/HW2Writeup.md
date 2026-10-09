I wanted to expand on my homework problem from Homework 1. I built on the same
premise with a couple of changes that make it more in line with what we have learned in the last
few weeks. To reintroduce the problem that I created, the mission is to create a program that can
output the slash line seen in baseball and, most importantly, in Major League Baseball. The slash
line includes batting average, on-base percentage, slugging percentage, and on-base plus
slugging. To calculate these values, first, for batting average, you must divide the number of hits
by the number of at-bats. Next, on-base percentage is calculated by adding the number of hits,
walks, and hit by pitches and dividing number of at-bats plus the number of hit-by-pitches plus
the number of walks plus the number of sacrifice flies. Slugging percentage is calculated by
multiplying singles + 2 * doubles + 3 * triples + 4 * home runs and dividing the sum by the total
number of at-bats. Finally, on-base plus slugging is calculated by just adding the calculated
on-base and slugging percentages together. For this homework assignment, you must create
functions, docstrings, and include forms of data validation. These values must be greater than or
equal to 0 but less than 1000. As the maximum number of plate appearances in a season is
around 780, so simplify will we place this number to 1000.
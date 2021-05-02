# benford
Comparison of electoral data from 2006 to 2018 with the mathematical model of Benford's law

Benford's law (source: wikipedia)
Benford's law, also called the first digit law, Newcomb-Benford law and anomalous numbers law, refers to the distribution of digits in various sources of real cases. Contrary to the expected homogeneity, the law states that in many collections of naturally occurring numbers, the significant first digit is likely to be small. Without homogeneity, this distribution shows that the digit 1 has a 30% chance of appearing in a set of statistical data while larger values ​​are less likely to appear.
In short, for a large set of values ​​that happen naturally, the first number of these values ​​(1 in 1543, 6 in 645, for example) tends to be a small number. It is a trend that arises when these values ​​can vary by many orders of magnitude, that is, the values ​​can be close to 1, 10, 100, 1000, 10000, or so on.
If it is a small set of values ​​or if the values ​​are very close (few orders of magnitude), the distribution will not follow this trend.

Input data:
The data for all Brazilian elections can be obtained from the TSE Electoral Data Repository page. The calculation of each electoral zone is available on the link "Nominal vote by municipality and zone (ZIP format)". For president election, I've used as input only the file ending in 'BR'.
In this file, each line has the number AA of votes that candidate BB received in the CC electoral zone, in the DD city and EE state.
According to the TSE: "Candidate data and election results from 1994 to 2002 are incomplete. A review of data sources is underway and, as work is completed, the files will be replaced."

Output data:
Exports graphs showing the distribution of the first digits of votes by electoral zone in each candidate.
Generates a graph with national and regional data for each candidate (graf_XX.png) and one with data separated by state for each candidate (graf_XX_YY.png). The ZZ state points out the voting zones abroad.

Script operation:
It is necessary to inform the year (the input data has different columns in 2018) and the election round.
For the desired year file, which is found in the 'data/' folder, it scans each line looking for the number AA of votes that the BB candidate received in the CC electoral zone, in the DD city and EE state.
Then, it creates for each candidate a counter that measures the number of times that each digit appears in each of the zones. One national sum, one sum for each state and one for each region of Brazil. To ease the comparison, this is normalized for each group, so that we have the percentage of times that each digit appeared and not the total number.
Calculates the expected distribution of Benford's law.
A graph is created with a blue line (Benford's law) and red dots (real data). The title is "'Candidate N: XX" for graphs with national data, "Candidate N: XX in state: YY" with state data, and "Candidate N: XX in region: YY" with regional data.
Within the graph, we have a sigma value, which is the average distance from the points to the blue line. If sigma = 2%, this means that the red dots are, on average, 2% more or less than expected. For example, the digit '5' must appear with an 8% probability. With sigma = 2%, the red dot must be between 6% and 10%.
In total, 442 graphics are created: 1 national, 5 regional, 26 state, 1 Federal District and 1 abroad, for each candidate.
We also have a graph with the sigma values ​​for each candidate in each state and another with the values ​​for Brazil and the regions. If sigma is less than 3, the dot is blue. If between 3 and 6, it is green. If between 6 and 9, the dot is yellow. If greater than 9, the dot is red. So we can see how much each pair (candidate, state) came close to the mathematical model. States are in order by the number of electoral zones in 2018.
The graphics are saved in the 'images/' folder.

Evaluation of results:
We must remember that: "If it is a small set of values ​​or if the values ​​are very close (few orders of magnitude), the distribution will not follow this trend." We see that sigma values ​​increase for the smallest states and for the candidates with the fewest votes. The larger the data set (SP, for example), the closer the red dots are to the blue line.
If a high sigma appears in one of the large data sets, this may (a possibility) be an indication of a change in the data. If the red dots for numbers 7, 8 or 9 are too far from the blue line, for example.

Lesson learned:
The mathematical model works for what it proposes: distribution of many numbers in several orders of magnitude. If that is not true, the model will not fit.


"It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong." Richard Feynman

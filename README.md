# Welcome to My Profile!

This week's code snippet, Josephus Problem in Commodore Basic, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Commodore Basic
5 REM Input N
10 GOSUB 1000
20 IF V = 0 OR C <> -1 THEN GOTO 140: REM invalid or not end of value
30 N = NR
35 REM Input K
40 GOSUB 1000
50 IF V = 0 OR C >= 0 THEN GOTO 140: REM invalid or not end character
60 K = NR
70 G = 0
80 IF N < 2 THEN GOTO 120
85 REM Calculate Josephus Problem using this:
86 REM https://en.wikipedia.org/wiki/Josephus_problem#The_general_case
90 FOR M = 2 TO N
100     G = G + K - INT((G + K) / M) * M
110 NEXT M
120 PRINT MID$(STR$(G + 1), 2)
130 END
140 PRINT "Usage: please input the total number of people and number of people to skip."
150 END
1000 REM Read input value one character at a time since Commodore BASIC
1001 REM has trouble reading line from stdin properly
1002 REM NR = number
1003 REM V = 1 if valid number, 0 otherwise
1004 REM C = -2 if end of input, -1 if end of value,
1005 REM   32 if whitespace, ASCII code of last character otherwise
1006 REM Initialize
1010 NR = 0
1020 V = 0
1030 S = 1
1035 REM Loop while leading spaces
1040 GOSUB 1500
1050 IF C = 43 OR C = 45 THEN GOTO 1100: REM + or -
1060 IF C >= 48 AND C <= 57 THEN GOTO 1150: REM 0 to 9
1070 IF C = 32 THEN GOTO 1040: REM whitespace
1080 RETURN: REM other character
1085 REM Loop while sign
1090 GOSUB 1500
1100 IF C = 43 THEN GOTO 1090: REM +
1110 IF C >= 48 AND C <= 57 THEN GOTO 1150: REM 0 to 9
1120 IF C <> 45 THEN RETURN: REM not -
1130 S = -S
1140 GOTO 1090
1145 REM Set valid flag
1150 V = 1
1155 REM Loop while digits
1160 NR = (ABS(NR) * 10 + C - 48) * S
1170 GOSUB 1500
1180 IF C >= 48 AND C <= 57 THEN GOTO 1160: REM 0 to 9
1185 REM Loop while trailing spaces
1190 IF C < 0 OR C <> 32 THEN RETURN: REM end character or not whitespace
1200 GOSUB 1500
1210 GOTO 1180
1500 REM Get input character
1501 REM A$ = input character
1502 REM C = One of the following:
1502 REM - -1 if end of value
1503 REM - -2 if end of input
1504 REM - 32 if whitespace
1505 REM - ASCII code otherwise
1510 GET A$
1520 C = ASC(A$)
1530 IF C = 13 THEN C = -1
1540 IF C = 255 THEN C = -2
1550 IF C = 9 OR C = 10 THEN C = 32
1560 RETURN
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :apple: [The Problem With Assessing Instructor Difficulty](https://therenegadecoder.com/teach/the-problem-with-assessing-instructor-difficulty/)
- :apple: [College Students Will Sometimes Have a Lapse in Judgement](https://therenegadecoder.com/teach/college-students-will-sometimes-have-a-lapse-in-judgement/)
- :apple: [We Have to End Our Cultural Obsession With Grades](https://therenegadecoder.com/teach/we-have-to-end-our-cultural-obsession-with-grades/)
- :computer: [How to Automatically Calculate Letter Grades, But Every Solution Is Bad](https://therenegadecoder.com/code/how-to-automatically-calculate-letter-grades-but-every-solution-is-bad/)
- :apple: [It’s Time We Talk About Student Evaluations of Teaching](https://therenegadecoder.com/teach/its-time-we-talk-about-student-evaluations-of-teaching/)
- :computer: [3 Nasty Bugs in Software Development](https://therenegadecoder.com/code/nasty-bugs-in-software-development/)
- :computer: [Modeling a Simple Relational Database Using CSVs and Python](https://therenegadecoder.com/code/modeling-a-simple-relational-database-using-csvs-and-python/)
- :black_nib: [Yet Another Instance of Misogyny in the Tech Field](https://therenegadecoder.com/blog/yet-another-instance-of-misogyny-in-the-tech-field/)
- :apple: [Top Reasons Why You Don’t Need to Take Attendance (And Why I Do It Anyway)](https://therenegadecoder.com/teach/top-reasons-why-you-dont-need-to-take-attendance-and-why-i-do-it-anyway/)
- :computer: [The Never-ending List of Small Programming Project Ideas](https://therenegadecoder.com/code/the-never-ending-list-of-small-programming-project-ideas/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-05-17 using [SnakeMD](https://www.snakemd.io).
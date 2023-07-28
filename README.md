# Welcome to My Profile!

This week's code snippet, Factorial in Cobol, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Cobol
IDENTIFICATION DIVISION.
        PROGRAM-ID. FACTORIAL.
        DATA DIVISION.
        WORKING-STORAGE SECTION.
          01 CMD-ARGS                  PIC X(38).
          01 DECINUM                  PIC S9999v99.
          01 NUM                      PIC S9(7).
          01 FACTORIAL                PIC 9(15) VALUE 1.
          01 LEFT-JUST-NUMBER         PIC X(16).
          01 WS-TALLY1                PIC 99 VALUE 0.
          01 CNT                      PIC 9(7) VALUE 1.

        PROCEDURE DIVISION.
           ACCEPT CMD-ARGS FROM COMMAND-LINE.

           IF CMD-ARGS IS ALPHABETIC THEN
              PERFORM ERROR-PARA.
           
      * Convert CMDARGS to it's numeric value
           COMPUTE DECINUM = FUNCTION NUMVAL(CMD-ARGS).
           
           IF DECINUM < 0 THEN
              PERFORM ERROR-PARA.

      * Move the Decimal number to Non decimal number
           MOVE DECINUM TO NUM
      
      * If both are equal, then it was an integer
           IF NUM IS EQUAL TO DECINUM THEN
              IF NUM IS EQUAL TO 0 OR NUM IS EQUAL TO 1 THEN
                 DISPLAY 1
                 STOP RUN                 
              ELSE
                 PERFORM CALC-FACT UNTIL CNT > NUM
      
      * Process to left justify the number
                 INSPECT FACTORIAL TALLYING WS-TALLY1 FOR LEADING ZEROS
                 Move FACTORIAL (WS-TALLY1 + 1 :) TO LEFT-JUST-NUMBER
      * Display the left justified result
                 DISPLAY LEFT-JUST-NUMBER
                 STOP RUN
           ELSE 
              PERFORM ERROR-PARA.
           
           
          CALC-FACT.
            COMPUTE FACTORIAL = FACTORIAL * CNT
            COMPUTE CNT = CNT + 1.

          ERROR-PARA.
           DISPLAY "Usage: please input a non-negative integer".
           STOP RUN.
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [CampusParc Has Got to Go](https://therenegadecoder.com/blog/campusparc-has-got-to-go/)
- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)
- :computer: [5 Absurd Ways to Add Two Numbers in Python](https://therenegadecoder.com/code/5-absurd-ways-to-add-two-numbers-in-python/)
- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)
- :black_nib: [Using Ethnography to Advocate for Student Needs in Computer Science Education](https://therenegadecoder.com/blog/using-ethnography-to-advocate-for-student-needs-in-computer-science-education/)
- :computer: [3 Key Programming Best Practices for Beginners](https://therenegadecoder.com/code/programming-best-practices-for-beginners/)
- :black_nib: [What Restoring a 20-Year-Old Deck Looks Like](https://therenegadecoder.com/blog/what-refreshing-a-20-year-old-deck-looks-like/)
- :black_nib: [Java Has A Remainder Operator—Not a Mod Operator](https://therenegadecoder.com/blog/java-has-a-remainder-operator-not-a-mod-operator/)
- :black_nib: [5 Things You Should Know Before You Pick Up Python](https://therenegadecoder.com/blog/things-you-should-know-before-you-pick-up-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-07-28 using [SnakeMD](https://www.snakemd.io).
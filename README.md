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

- :apple: [Reflecting on My First Two Years as a Lecturer](https://therenegadecoder.com/teach/reflecting-on-my-first-two-years-as-a-lecturer/)
- :black_nib: [Why I Left Twitter](https://therenegadecoder.com/blog/why-i-left-twitter/)
- :computer: [A Case Study on the Philosophy of Software Design](https://therenegadecoder.com/code/a-case-study-on-the-philosophy-of-software-design/)
- :black_nib: [Inside the Mind of an Engineer: How to Make Societal Issues Worse](https://therenegadecoder.com/blog/inside-the-mind-of-an-engineer-how-to-make-societal-issues-worse/)
- :black_nib: [How Attack on Titan Undermines Its Own Message](https://therenegadecoder.com/blog/how-attack-on-titan-undermines-its-own-message/)
- :computer: [Migrating to Poetry 2.x With Some Best Practices](https://therenegadecoder.com/code/migrating-to-poetry-2-x-with-some-best-practices/)
- :black_nib: [Maybe Generative AI Is Just a Symptom of a Broader Problem in Tech](https://therenegadecoder.com/blog/maybe-generative-ai-is-just-a-symptom-of-a-broader-problem-in-tech/)
- :apple: [It’s Time to Collect Mid-Semester Feedback](https://therenegadecoder.com/teach/its-time-to-collect-mid-semester-feedback/)
- :thought_balloon: [2024: Year in Review](https://therenegadecoder.com/meta/2024-year-in-review/)
- :black_nib: [Is Anyone Else Bothered by How Quickly We Adopted Generative AI?](https://therenegadecoder.com/blog/is-anyone-else-bothered-by-how-quickly-we-adopted-generative-ai/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-05-02 using [SnakeMD](https://www.snakemd.io).
# Welcome to My Profile!

This week's code snippet, Remove All Whitespace in Brainfuck, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Brainfuck
[
    Source for error message text:
    https://copy.sh/brainfuck/text.html
]
; Mem 0 = 1 (indicate no input)
+
; Mem 1 = input; Loop while input not null
>,[
    ; Mem 0 = 0 (indicate input)
    <[-]
    ; Mem 2 = input; Mem 3 = input; Mem 1 = 0
    >>[-]                       ; Mem 2 = 0
    >[-]                        ; Mem 3 = 0
    <<[
        >+                      ; Inc Mem 2
        >+                      ; Mem Mem 3
        <<-                     ; Dec Mem 1
    ]
    ; Sub 9 from Mem 3; If not zero (not tab)
    >>---------[
        ; Dec Mem 3; If not zero (not newline)
        -[
            ; Sub 3 from Mem 3; If not zero (not carriage return)
            ---[
                ; Sub 19 from Mem 3; If not zero (not space)
                >+++[           ; Mem 4 = 3
                    <------     ; Sub 6 from Mem 3
                    >-          ; Dec Mem 4
                ]
                <-              ; Dec Mem 3
                [
                    ; Display input (Mem 2) and reset Mem 3
                    <.
                    >[-]
                ]
            ]
        ]
    ]
    ; Mem 1 = input
    <<,
]
; If no input; display error message
<[
    [-]
    -[--->+<]>.
    +[--->+<]>+.
    ++[->+++<]>++.
    ++++++.
    --.
    +++[->+++<]>++.
    [-->+<]>+++.
    [-->+++++++<]>.
    ----.
    -------.
    ----.
    --[--->+<]>--.
    ++++[->+++<]>.
    --[--->+<]>-.
    [-->+++++++<]>.
    ++.
    ---.
    +++++++.
    [------>+<]>.
    -----.
    +.
    --[--->+<]>-.
    [->+++<]>+.
    -[->+++<]>.
    ---[->++++<]>-.
    +.
    --.
    ---------.
    +++++.
    -------.
    [-]
]
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Google Threatens to Ruin Search as We Know It](https://therenegadecoder.com/blog/google-threatens-to-ruin-search-as-we-know-it/)
- :apple: [The Problem With Assessing Instructor Difficulty](https://therenegadecoder.com/teach/the-problem-with-assessing-instructor-difficulty/)
- :apple: [College Students Will Sometimes Have a Lapse in Judgement](https://therenegadecoder.com/teach/college-students-will-sometimes-have-a-lapse-in-judgement/)
- :apple: [We Have to End Our Cultural Obsession With Grades](https://therenegadecoder.com/teach/we-have-to-end-our-cultural-obsession-with-grades/)
- :computer: [How to Automatically Calculate Letter Grades, But Every Solution Is Bad](https://therenegadecoder.com/code/how-to-automatically-calculate-letter-grades-but-every-solution-is-bad/)
- :apple: [It’s Time We Talk About Student Evaluations of Teaching](https://therenegadecoder.com/teach/its-time-we-talk-about-student-evaluations-of-teaching/)
- :computer: [3 Nasty Bugs in Software Development](https://therenegadecoder.com/code/nasty-bugs-in-software-development/)
- :computer: [Modeling a Simple Relational Database Using CSVs and Python](https://therenegadecoder.com/code/modeling-a-simple-relational-database-using-csvs-and-python/)
- :black_nib: [Yet Another Instance of Misogyny in the Tech Field](https://therenegadecoder.com/blog/yet-another-instance-of-misogyny-in-the-tech-field/)
- :apple: [Top Reasons Why You Don’t Need to Take Attendance (And Why I Do It Anyway)](https://therenegadecoder.com/teach/top-reasons-why-you-dont-need-to-take-attendance-and-why-i-do-it-anyway/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-05-24 using [SnakeMD](https://www.snakemd.io).
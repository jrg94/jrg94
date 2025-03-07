# Welcome to My Profile!

This week's code snippet, Capitalize in Brainfuck, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Brainfuck
[
    Source for division algorithm:
    https://stackoverflow.com/questions/27905818/divmod-algorithm-in-brainfuck

    Source for error message text:
    https://copy.sh/brainfuck/text.html
]
; Mem 0 = 1 (indicate first char)
+
; Mem 1 = input char; loop while not null
>,[
    ; Copy input char to Mem 2 and 3; setting Mem 1 to 0
    >[-]
    >[-]
    <<[>+>+<<-]
    ; If first char;
    <[
        ; Mem 5 = 26; Mem 3 = input char minus 97 ('a'); Mem 4 = 0 (uninitialized)
        >>>>>>++++++++++[   ; Mem 6 = 10
            <+++            ; Add 3 to Mem 5
            <<----------    ; Sub 10 from Mem 3
            >>>-            ; Dec Mem 6
        ]
        <----               ; Sub 4 from Mem 5
        <<+++               ; Add 3 to Mem 3
        ; Mem 3 = junk; Mem 4 = n; Mem 5 = d minus r; Mem 6 = r; Mem 7 = q
        ; where:
        ; * n = input char minus 97 (numerator)
        ; * d = 26 (denominator)
        ; * r = n % d (remainder)
        ; * q = n / d (quotient)
        ;
        ; q will be zero if input char is lowercase; not zero otherwise
        [->+>-[>+>>]>[+[-<+>]>+>>]<<<<<<]
        ; Sub 32 from Mem 2 (copy of input char) to potentially make it uppercase
        <<++++[             ; Mem 1 = 4
            >--------       ; Sub 8 from Mem 2
            <-              ; Dec Mem 1
        ]
        ; If Mem 7 (q) is not zero (not a lowercase char); add 32 to Mem 2 to undo above
        ; (restore copy of input char)
        >>>>>>[
            <<<<<<++++[     ; Mem 1 = 4
                >++++++++   ; Add 8 to Mem 2
                <-          ; Dec Mem 1
            ]
            >>>>>>[-]       ; Mem 7 = 0
        ]
        ; Mem 0 = 0 (indicate not first char)
        <<<<<<<[-]
    ]
    ; Output Mem 32 (copy of input char; uppercased for first char)
    >>.
    ; Mem 1 = input char
    <,
]
; If first char was null; display error message
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
    <
]
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Maybe Generative AI Is Just a Symptom of a Broader Problem in Tech](https://therenegadecoder.com/blog/maybe-generative-ai-is-just-a-symptom-of-a-broader-problem-in-tech/)
- :apple: [It’s Time to Collect Mid-Semester Feedback](https://therenegadecoder.com/teach/its-time-to-collect-mid-semester-feedback/)
- :thought_balloon: [2024: Year in Review](https://therenegadecoder.com/meta/2024-year-in-review/)
- :black_nib: [Is Anyone Else Bothered by How Quickly We Adopted Generative AI?](https://therenegadecoder.com/blog/is-anyone-else-bothered-by-how-quickly-we-adopted-generative-ai/)
- :black_nib: [31 Lessons Learned as a New Dad](https://therenegadecoder.com/blog/31-lessons-learned-as-a-new-dad/)
- :apple: [So You’re Not Sure If Computer Science Is for You](https://therenegadecoder.com/teach/so-youre-not-sure-if-computer-science-is-for-you/)
- :apple: [You Should Give Open-Ended Projects to Your Students](https://therenegadecoder.com/teach/you-should-give-open-ended-projects-to-your-students/)
- :computer: [How to Move Your Extensions Folder in VS Code](https://therenegadecoder.com/code/how-to-move-your-extensions-folder-in-vs-code/)
- :thought_balloon: [Sample Programs Repo Celebrates 1,000 Code Snippets](https://therenegadecoder.com/meta/sample-programs-repo-celebrates-1000-code-snippets/)
- :apple: [Canvas Is Not Built With Educators in Mind](https://therenegadecoder.com/teach/canvas-is-not-built-with-educators-in-mind/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-03-07 using [SnakeMD](https://www.snakemd.io).
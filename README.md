# Welcome to My Profile!

This week's code snippet, Baklava in Mirth, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Mirth
module sample-programs.baklava

import std.prelude
import std.world
import std.list
import std.str

||| stack: n
def abs [Int -- Nat] {
    ||| if n < 0 then -n else n
    dup 0 < if(-1 *, dup drop) Int.>Nat-clamp
}

||| stack: n (count), s (string)
def repeat-string [Nat Str -- Str] {
    ""                      ||| stack: n, s, result = ""
    rotl                    ||| stack: s, result, n
    repeat(                 ||| stack: s, result
                            ||| repeat n times:
        over                |||     stack: s, result, s
        cat                 |||     stack: s, result = result + s
    )
    dip(drop)               ||| stack: result
}

||| stack: n
def baklava-line [Int -- Str] {
    abs                                 ||| stack: num-spaces = abs(n)
    dup                                 ||| stack: num-spaces, num-spaces
    " " repeat-string                   ||| stack: num-spaces, spaces = num-spaces " "
    swap                                ||| stack: spaces, num-spaces
    Nat.>Int -2 * 21 + Int.>Nat-clamp   ||| stack: spaces, num-stars = 21 - 2 * num-spaces
    "*" repeat-string                   ||| stack: spaces, stars = num-stars "*"
    cat                                 ||| stack: spaces + stars
}

def main {
    ||| for n = -10 to 10:
    |||    print baklava-line(n)
    -10 10 range for(baklava-line print)
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [Why Does == Sometimes Work on Integer Objects in Java?](https://therenegadecoder.com/code/why-does-sometimes-work-on-integer-objects-in-java/)
- :apple: [Online Exams Might Be Cooked](https://therenegadecoder.com/teach/online-exams-might-be-cooked/)
- :apple: [Encouraging Attendance With Peer Instruction](https://therenegadecoder.com/teach/encouraging-attendance-with-peer-instruction/)
- :black_nib: [Conspiracy Theory: All Pro Sports Are Rigged Now](https://therenegadecoder.com/blog/conspiracy-theory-all-pro-sports-are-rigged-now/)
- :apple: [Reflecting on My Teaching Journey Heading into 2026](https://therenegadecoder.com/teach/reflecting-on-my-teaching-journey-heading-into-2026/)
- :apple: [I Hate That Student Feedback Is Now Reviewed by Machine Learning](https://therenegadecoder.com/teach/i-hate-that-student-feedback-is-now-reviewed-by-machine-learning/)
- :black_nib: [Not All Code Completion Is Generative AI](https://therenegadecoder.com/blog/not-all-code-completion-is-generative-ai/)
- :black_nib: [AI Haters Stay Winning: What It’s Like to Be Constantly Vindicated](https://therenegadecoder.com/blog/ai-haters-stay-winning-what-its-like-to-be-constantly-vindicated/)
- :black_nib: [Computer Science Career Advice in 2026? Your Guess Is as Good as Mine](https://therenegadecoder.com/blog/computer-science-career-advice-in-2026-your-guess-is-as-good-as-mine/)
- :apple: [Why I Don’t Record My Lectures](https://therenegadecoder.com/teach/why-i-dont-record-my-lectures/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-01-30 using [SnakeMD](https://www.snakemd.io).
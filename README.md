# Welcome to My Profile!

This week's code snippet, Baklava in Factor, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Factor
USING: io kernel math prettyprint ranges sequences ;
IN: baklava

! Based on https://rosettacode.org/wiki/Repeat_a_string#Factor
! but reversed arguments for fewer operations
: repeat-string ( n str -- str' ) <repetition> concat ;

: baklava-line ( n -- str )
    10 - abs        ! stack: num-spaces = abs(n - 10)
    dup             ! stack: num-spaces, num-spaces
    " "             ! stack: num-spaces, num-spaces, " "
    repeat-string   ! stack: num-spaces, spaces = " " num-spaces times
    swap            ! stack: spaces, num-spaces
    -2 * 21 +       ! stack: spaces, num-stars = 21 - 2 * num-spaces
    "*"             ! stack: spaces, num-stars, "*"
    repeat-string   ! stack: spaces, stars = "*" num-stars times
    append          ! stack: spaces + stars
    ;

! For n = 0 to 20, output Baklava line n
20 [0..b] [ baklava-line print ] each
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :thought_balloon: [Another Year, Another Hacktoberfest](https://therenegadecoder.com/meta/another-year-another-hacktoberfest/)
- :black_nib: [I’m Learning a Language, and I’m Tired](https://therenegadecoder.com/blog/im-learning-a-language-and-im-tired/)
- :apple: [Yes, You Need General Education in College](https://therenegadecoder.com/teach/yes-you-need-general-education-in-college/)
- :apple: [Higher Education Should Not Be a Job Training Program](https://therenegadecoder.com/teach/higher-education-should-not-be-a-job-training-program/)
- :black_nib: [Why Generative AI Makes the Future of Software Development Worse](https://therenegadecoder.com/blog/why-generative-ai-makes-the-future-of-software-development-worse/)
- :black_nib: [Technology Will Not Liberate Us](https://therenegadecoder.com/blog/technology-will-not-liberate-us/)
- :black_nib: [The Future of AI Is Ubiquitous Surveillance](https://therenegadecoder.com/blog/the-future-of-ai-is-ubiquitous-surveillance/)
- :black_nib: [Y’all Need to Stop Using Generative AI for Summaries](https://therenegadecoder.com/blog/yall-need-to-stop-using-generative-ai-for-summaries/)
- :computer: [Loop Invariants Are Necessary for Writing Proper Loops](https://therenegadecoder.com/code/loop-invariants-are-necessary-for-writing-proper-loops/)
- :computer: [Dark Arts: Labeled Statements in Java](https://therenegadecoder.com/code/dark-arts-labeled-statements-in-java/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-10-10 using [SnakeMD](https://www.snakemd.io).
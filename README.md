# Welcome to My Profile!

This week's code snippet, Fizz Buzz in Prolog, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Prolog
% Portions of this solution were derived through the assistance of ChatGPT.
:- initialization(main).

fizzbuzz(N) :-
    fizzbuzz_helper(1, N).

fizzbuzz_helper(X, N) :-
    X > N, !.
fizzbuzz_helper(X, N) :-
    (X mod 15 =:= 0 ->
        write('FizzBuzz'), nl
    ; X mod 3 =:= 0 ->
        write('Fizz'), nl
    ; X mod 5 =:= 0 ->
        write('Buzz'), nl
    ;
        write(X), nl
    ),
    X1 is X + 1,
    fizzbuzz_helper(X1, N).

main() :-
    fizzbuzz(100),
    halt.
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Yet Another Instance of Misogyny in the Tech Field](https://therenegadecoder.com/blog/yet-another-instance-of-misogyny-in-the-tech-field/)
- :apple: [Top Reasons Why You Don’t Need to Take Attendance (And Why I Do It Anyway)](https://therenegadecoder.com/teach/top-reasons-why-you-dont-need-to-take-attendance-and-why-i-do-it-anyway/)
- :computer: [The Never-ending List of Small Programming Project Ideas](https://therenegadecoder.com/code/the-never-ending-list-of-small-programming-project-ideas/)
- :black_nib: [Why I’m a Certified AI Hater](https://therenegadecoder.com/blog/why-im-a-certified-ai-hater/)
- :computer: [Explain Like I’m Five: Context-Free Grammars](https://therenegadecoder.com/code/explain-like-im-five-context-free-grammars/)
- :black_nib: [The Haters Guide to Python](https://therenegadecoder.com/blog/the-haters-guide-to-python/)
- :black_nib: [America Is Not Ready for the Metric System](https://therenegadecoder.com/blog/america-is-not-ready-for-the-metric-system/)
- :black_nib: [30 Best Video Games Over the Last 30 Years](https://therenegadecoder.com/blog/30-best-video-games-over-the-last-30-years/)
- :black_nib: [Celebrating My Late Mother’s 54th Birthday](https://therenegadecoder.com/blog/celebrating-my-late-mothers-54th-birthday/)
- :black_nib: [What Do People Mean When They Say “From Scratch”?](https://therenegadecoder.com/blog/what-do-people-mean-when-they-say-from-scratch/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-03-29 using [SnakeMD](https://www.snakemd.io).
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

- :thought_balloon: [2024: Year in Review](https://therenegadecoder.com/meta/2024-year-in-review/)
- :black_nib: [Is Anyone Else Bothered by How Quickly We Adopted Generative AI?](https://therenegadecoder.com/blog/is-anyone-else-bothered-by-how-quickly-we-adopted-generative-ai/)
- :black_nib: [31 Lessons Learned as a New Dad](https://therenegadecoder.com/blog/31-lessons-learned-as-a-new-dad/)
- :apple: [So You’re Not Sure If Computer Science Is for You](https://therenegadecoder.com/teach/so-youre-not-sure-if-computer-science-is-for-you/)
- :apple: [You Should Give Open-Ended Projects to Your Students](https://therenegadecoder.com/teach/you-should-give-open-ended-projects-to-your-students/)
- :computer: [How to Move Your Extensions Folder in VS Code](https://therenegadecoder.com/code/how-to-move-your-extensions-folder-in-vs-code/)
- :thought_balloon: [Sample Programs Repo Celebrates 1,000 Code Snippets](https://therenegadecoder.com/meta/sample-programs-repo-celebrates-1000-code-snippets/)
- :apple: [Canvas Is Not Built With Educators in Mind](https://therenegadecoder.com/teach/canvas-is-not-built-with-educators-in-mind/)
- :computer: [Workshopping a Tier List Generator](https://therenegadecoder.com/code/workshopping-a-tier-list-generator/)
- :black_nib: [No, The GRE Should Not Be Reinstated](https://therenegadecoder.com/blog/no-the-gre-should-not-be-reinstated/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-02-21 using [SnakeMD](https://www.snakemd.io).
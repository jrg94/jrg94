# Welcome to My Profile!

This week's code snippet, Quine in Cython, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Cython
from libc.stdio cimport printf

def main():
    cdef bytes s = b"""from libc.stdio cimport printf

def main():
    cdef bytes s = b%c%c%c%s%c%c%c
    printf(s, 34, 34, 34, s, 34, 34, 34)

if __name__ == "__main__":
    main()"""
    printf(s, 34, 34, 34, s, 34, 34, 34)

if __name__ == "__main__":
    main()
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [You Will Never Learn a Language With Duolingo](https://therenegadecoder.com/blog/you-will-never-learn-a-language-with-duolingo/)
- :black_nib: [The Cult of Efficiency Is a Plague](https://therenegadecoder.com/blog/the-cult-of-efficiency-is-a-plague/)
- :black_nib: [Missing the Forest for the Trees: Why You Struggle to Solve Problems](https://therenegadecoder.com/blog/missing-the-forest-for-the-trees-why-you-struggle-to-solve-problems/)
- :black_nib: [What It Feels Like to Be a Toddler Again: Learning a Language](https://therenegadecoder.com/blog/what-it-feels-like-to-be-a-toddler-again-learning-a-language/)
- :black_nib: [Things I Don’t Want AI To Help Me With](https://therenegadecoder.com/blog/things-i-dont-want-ai-to-help-me-with/)
- :black_nib: [Why I Rebel Against the Use of Generative AI](https://therenegadecoder.com/blog/why-i-rebel-against-the-use-of-generative-ai/)
- :black_nib: [Buying a House Sucks](https://therenegadecoder.com/blog/buying-a-house-sucks/)
- :black_nib: [Smug Yet Unserious](https://therenegadecoder.com/blog/smug-yet-unserious/)
- :black_nib: [32 College Stories That Always Make Friends Laugh](https://therenegadecoder.com/blog/32-college-stories-that-always-make-friends-laugh/)
- :computer: [Why Does == Sometimes Work on Integer Objects in Java?](https://therenegadecoder.com/code/why-does-sometimes-work-on-integer-objects-in-java/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-04-10 using [SnakeMD](https://www.snakemd.io).
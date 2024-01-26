# Welcome to My Profile!

This week's code snippet, Reverse String in C, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```C
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    char *text = "";
    size_t textlen;

    /* get text from command line and calculate length */
    if (argc >= 2) {
        text = argv[1];
    }

    textlen = strlen(text);

    /* print characters in reverse */
    while (textlen-- > 0) {
        putchar(text[textlen]);
    }

    /* put a newline at the end */
    putchar('\n');

    return 0;
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [What Do People Mean When They Say “From Scratch”?](https://therenegadecoder.com/blog/what-do-people-mean-when-they-say-from-scratch/)
- :black_nib: [What Is Going On With Cloud Storage for Photos?](https://therenegadecoder.com/blog/what-is-going-on-with-cloud-storage-for-photos/)
- :computer: [Migrating From Eclipse to VS Code: The Many Hurdles](https://therenegadecoder.com/code/migrating-from-eclipse-to-vs-code-the-many-hurdles/)
- :black_nib: [2023: Year in Review](https://therenegadecoder.com/blog/2023-year-in-review/)
- :computer: [How to Plot Semesters Using Pandas and Plotly](https://therenegadecoder.com/code/how-to-plot-semesters-using-pandas-and-plotly/)
- :apple: [Reflecting on Two More Semesters of Teaching: Spring & Autumn 2023](https://therenegadecoder.com/teach/reflecting-on-two-more-semesters-of-teaching-spring-autumn-2023/)
- :black_nib: [Grade Inflation Is Bullshit](https://therenegadecoder.com/blog/grade-inflation-is-bullshit/)
- :computer: [Brainstorming An Algorithm for Shuffling a Queue of Songs](https://therenegadecoder.com/code/brainstorming-an-algorithm-for-shuffling-a-queue-of-songs/)
- :computer: [Trust Me! Your Code Isn’t That Bad](https://therenegadecoder.com/code/trust-me-your-code-isnt-that-bad/)
- :computer: [The Difference Between str() and repr() in Python: A Design by Contract Perspective](https://therenegadecoder.com/code/the-difference-between-str-and-repr-in-python-a-design-by-contract-perspective/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-01-26 using [SnakeMD](https://www.snakemd.io).
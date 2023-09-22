# Welcome to My Profile!

This week's code snippet, Baklava in Unicat, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Unicat
# Set up characters
0o00  Memory 0 = 0o40 (32 = ' ')
0o01  Memory 1 = 0o52 (42 = '*')
0o02  Memory 2 = 0o12 (10 = '\n')

# Set up constants
0o03  Memory 3 = 1
0o04  Memory 4 = -1

# Set up varibles
0o05  Memory 5 = -0o12 (-10) (loop_counter)

# Loop start: num_spaces = absolute value of loop_counter
0o06  Memory 6 = 0
0o07  Memory 6 += Memory 5 (num_spaces = loop_count)
0o10  If Memory 6 > 0, jump to 0x12 (0o11 + 1) (if num_spaces > 0)
0o11  Memory 6 *= Memory 4 (negate num_spaces)

# num_stars = 21 - 2*num_spaces
0o12  Memory 7 = 0o25 (21)
0o13  Memory 7 -= Memory 6 (21 - num_spaces)
0o14  Memory 7 -= Memory 6 (num_stars = 21 - 2*num_spaces)

# Display spaces
0o15  Jump to 0o20 (0o17 + 1) (jump to check for num_spaces > 0)
0o16  Output Memory 0 (' ')
0o17  Memory 6 -= Memory 3 (decrement num_spaces)
0o20  If Memory 6 > 0, jump to 0o16 (0o15 + 1) (if num_spaces > 0)

# Display stars
0o21  Output Memory 1 ('*')
0o22  Memory 7 -= Memory 3 (decrement num_stars)
0o23  If Memory 7 > 0, jump to 0o21 (0o20 + 1)

# Output newline
0o24  Output Memory 2 ('\n')

# If loop_counter > 10, jump to Loop start
0o25  Memory 8 (0o10) = 10 (0o12)
0o26  Memory 8 (0o10) -= Memory 5 (10 - loop_counter)
0o27  Memory 5 += Memory 3 (increment loop_counter)
0o30  If Memory 8 (0o10) > 0, jump to 0o06 (0o05 + 1) (if loop_counter > 10, jump to Loop start)

0o31  Exit
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Make TODO Lists More Meaningful By Reflecting on Your Values](https://therenegadecoder.com/blog/make-todo-lists-more-meaningful-by-reflecting-on-your-values/)
- :black_nib: [Speed Up Your Data Structures With Hashing](https://therenegadecoder.com/blog/speed-up-your-data-structures-with-hashing/)
- :black_nib: [The Two-Layer Approach to Software Design](https://therenegadecoder.com/blog/the-two-layer-approach-to-software-design/)
- :black_nib: [The World Is Built on Abstractions](https://therenegadecoder.com/blog/the-world-is-built-on-abstractions/)
- :computer: [5 Beginner Tricks for Writing Your Own Unit Tests](https://therenegadecoder.com/code/beginner-tricks-for-writing-your-own-unit-tests/)
- :thought_balloon: [Transition Madness: Becoming a Lecturer](https://therenegadecoder.com/meta/transition-madness-becoming-a-lecturer/)
- :black_nib: [I Am Officially a Lecturer](https://therenegadecoder.com/blog/i-am-officially-a-lecturer/)
- :black_nib: [CampusParc Has Got to Go](https://therenegadecoder.com/blog/campusparc-has-got-to-go/)
- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-09-22 using [SnakeMD](https://www.snakemd.io).
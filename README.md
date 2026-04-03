# Welcome to My Profile!

This week's code snippet, Fibonacci in Moonscript, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Moonscript
-- fibonacci function
fibonacci = (n) ->
    -- set up a, b, for i until n, print "i: n" then update a & b as the fibonacci sequence
    a, b = 1, 1
    for i = 1, n
        print "#{i}: #{a}"
        a, b = b, a + b

-- main
-- check if arg params are numbers and are greater than 0
if arg[1] and tonumber(arg[1]) ~= nil and tonumber(arg[1]) >= 0
    fibonacci tonumber(arg[1])
-- else, return usage error msg
else   
    print "Usage: please input the count of fibonacci numbers to output"
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [The Cult of Efficiency Is a Plague](https://therenegadecoder.com/blog/the-cult-of-efficiency-is-a-plague/)
- :black_nib: [Missing the Forest for the Trees: Why You Struggle to Solve Problems](https://therenegadecoder.com/blog/missing-the-forest-for-the-trees-why-you-struggle-to-solve-problems/)
- :black_nib: [What It Feels Like to Be a Toddler Again: Learning a Language](https://therenegadecoder.com/blog/what-it-feels-like-to-be-a-toddler-again-learning-a-language/)
- :black_nib: [Things I Don’t Want AI To Help Me With](https://therenegadecoder.com/blog/things-i-dont-want-ai-to-help-me-with/)
- :black_nib: [Why I Rebel Against the Use of Generative AI](https://therenegadecoder.com/blog/why-i-rebel-against-the-use-of-generative-ai/)
- :black_nib: [Buying a House Sucks](https://therenegadecoder.com/blog/buying-a-house-sucks/)
- :black_nib: [Smug Yet Unserious](https://therenegadecoder.com/blog/smug-yet-unserious/)
- :black_nib: [32 College Stories That Always Make Friends Laugh](https://therenegadecoder.com/blog/32-college-stories-that-always-make-friends-laugh/)
- :computer: [Why Does == Sometimes Work on Integer Objects in Java?](https://therenegadecoder.com/code/why-does-sometimes-work-on-integer-objects-in-java/)
- :apple: [Online Exams Might Be Cooked](https://therenegadecoder.com/teach/online-exams-might-be-cooked/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-04-03 using [SnakeMD](https://www.snakemd.io).
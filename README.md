# Welcome to My Profile!

This week's code snippet, Fizz Buzz in Eiffel, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Eiffel
class
    fizz_buzz

create
    make

feature
    make
        do
            across 1 |..| 100 as i
            loop
                if i.item \\ 15 = 0 then io.put_string("FizzBuzz")
                elseif i.item \\ 5 = 0 then io.put_string("Buzz")
                elseif i.item \\ 3 = 0 then io.put_string("Fizz")
                else io.put_integer(i.item)
                end
                
                io.put_new_line
            end
        end
    end
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [You’ve Fallen for the Red/Blue Button Trap](https://therenegadecoder.com/blog/youve-fallen-for-the-red-blue-button-trap/)
- :apple: [Another Year, Another Japan Trip](https://therenegadecoder.com/teach/another-year-another-japan-trip/)
- :apple: [The Importance of Getting Summers Off](https://therenegadecoder.com/teach/the-importance-of-getting-summers-off/)
- :black_nib: [Practicing My Toddler-like Japanese in Japan](https://therenegadecoder.com/blog/practicing-my-toddler-like-japanese-in-japan/)
- :black_nib: [Even My Charitability Has Limits](https://therenegadecoder.com/blog/even-my-charitability-has-limits/)
- :black_nib: [Thoughts on the Red Button vs. Blue Button Debate](https://therenegadecoder.com/blog/thoughts-on-the-red-button-vs-blue-button-debate/)
- :apple: [What Happens When I’m Forced to Teach AI?](https://therenegadecoder.com/teach/what-happens-when-im-forced-to-teach-ai/)
- :black_nib: [Giving Up Before Even Starting](https://therenegadecoder.com/blog/giving-up-before-even-starting/)
- :black_nib: [You Will Never Learn a Language With Duolingo](https://therenegadecoder.com/blog/you-will-never-learn-a-language-with-duolingo/)
- :black_nib: [The Cult of Efficiency Is a Plague](https://therenegadecoder.com/blog/the-cult-of-efficiency-is-a-plague/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-06-12 using [SnakeMD](https://www.snakemd.io).
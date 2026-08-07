# Welcome to My Profile!

This week's code snippet, Baklava in Discus, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Discus
module Main
import System.IO.Console
import Data.List
import Data.Text.List

where

baklavaLine (n: Nat): Text
 = (textOfCharList (replicate num_spaces ' ')) % (textOfCharList (replicate num_stars '*'))
    where
        num_spaces = if n > 10 then n - 10 else 10 -n
        num_stars = 21 - 2 * num_spaces

main ()
 =  forS (enumFromTo 0 20) $ n
 -> writel $ baklavaLine n
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [People Don’t Like to Be Deceived (by AI)](https://therenegadecoder.com/blog/people-dont-like-to-be-deceived-by-ai/)
- :apple: [Generative AI in Education is Pay-to-Lose](https://therenegadecoder.com/teach/generative-ai-in-education-is-pay-to-lose/)
- :black_nib: [My First “I Have a Toddler” Moment](https://therenegadecoder.com/blog/my-first-i-have-a-toddler-moment/)
- :black_nib: [LLMs Got Everyone Sounding the Same Now](https://therenegadecoder.com/blog/llms-got-everyone-sounding-the-same-now/)
- :black_nib: [6v6 Overwatch Is a Joke](https://therenegadecoder.com/blog/6v6-overwatch-is-a-joke/)
- :black_nib: [I Genuinely Don’t Understand Why People Tolerate Hallucinations in AI](https://therenegadecoder.com/blog/i-genuinely-dont-understand-why-people-tolerate-hallucinations-in-ai/)
- :black_nib: [Human Review of AI Output Is Not the Path Forward](https://therenegadecoder.com/blog/human-review-of-ai-output-is-not-the-path-forward/)
- :black_nib: [I Made the Mistake of Visiting the Vibe Coding Subreddit](https://therenegadecoder.com/blog/i-made-the-mistake-of-visiting-the-vibe-coding-subreddit/)
- :black_nib: [You’ve Fallen for the Red/Blue Button Trap](https://therenegadecoder.com/blog/youve-fallen-for-the-red-blue-button-trap/)
- :apple: [Another Year, Another Japan Trip](https://therenegadecoder.com/teach/another-year-another-japan-trip/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-08-07 using [SnakeMD](https://www.snakemd.io).
# Welcome to My Profile!

This week's code snippet, Baklava in F\*, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```F\*
module Baklava

open FStar.IO
open FStar.Math.Lib
open FStar.Mul

let baklava_line (n:nat {n <= 20}) : string =
  let num_spaces:nat = (abs (n - 10)) in
  let num_stars:nat = 21 - 2 * num_spaces in
  (String.make num_spaces ' ') ^ (String.make num_stars '*') ^ "\n"

let rec baklava (lines:string) (n:nat {n <= 20}) : string =
  match n with
  | 0 -> lines ^ (baklava_line 0)
  | _ -> lines ^ (baklava_line n) ^ (baklava lines (n - 1))

let main = print_string (baklava "" 20)
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Even My Charitability Has Limits](https://therenegadecoder.com/blog/even-my-charitability-has-limits/)
- :black_nib: [Thoughts on the Red Button vs. Blue Button Debate](https://therenegadecoder.com/blog/thoughts-on-the-red-button-vs-blue-button-debate/)
- :apple: [What Happens When I’m Forced to Teach AI?](https://therenegadecoder.com/teach/what-happens-when-im-forced-to-teach-ai/)
- :black_nib: [Giving Up Before Even Starting](https://therenegadecoder.com/blog/giving-up-before-even-starting/)
- :black_nib: [You Will Never Learn a Language With Duolingo](https://therenegadecoder.com/blog/you-will-never-learn-a-language-with-duolingo/)
- :black_nib: [The Cult of Efficiency Is a Plague](https://therenegadecoder.com/blog/the-cult-of-efficiency-is-a-plague/)
- :black_nib: [Missing the Forest for the Trees: Why You Struggle to Solve Problems](https://therenegadecoder.com/blog/missing-the-forest-for-the-trees-why-you-struggle-to-solve-problems/)
- :black_nib: [What It Feels Like to Be a Toddler Again: Learning a Language](https://therenegadecoder.com/blog/what-it-feels-like-to-be-a-toddler-again-learning-a-language/)
- :black_nib: [Things I Don’t Want AI To Help Me With](https://therenegadecoder.com/blog/things-i-dont-want-ai-to-help-me-with/)
- :black_nib: [Why I Rebel Against the Use of Generative AI](https://therenegadecoder.com/blog/why-i-rebel-against-the-use-of-generative-ai/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-05-08 using [SnakeMD](https://www.snakemd.io).
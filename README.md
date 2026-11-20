# Welcome to My Profile!

This week's code snippet, Baklava in Formality, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Formality
baklavaLine(n: Nat): String
  let numSpaces = if Nat.gte(n, 10) then Nat.sub(n, 10) else Nat.sub(10, n)
  let numStars = Nat.sub(21, Nat.mul(2, numSpaces))
  String.repeat(" ", numSpaces) | String.repeat("*", numStars) | "\n"

baklava(lines: String, n:Nat): String
  case n {
    zero: lines | baklavaLine(0),
    succ: lines | baklavaLine(n) | baklava(lines, n.pred)
  }

Main: IO(Unit)
  do IO {
    IO.put_string(baklava("", 20))
  }
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Academics Are Turning on AI Companies](https://therenegadecoder.com/blog/academics-are-turning-on-ai-companies/)
- :black_nib: [I’m Dabbling in Dungeons & Dragons](https://therenegadecoder.com/blog/im-dabbling-in-dungeons-dragons/)
- :black_nib: [Staying Relevant Is Holding You Back](https://therenegadecoder.com/blog/staying-relevant-is-holding-you-back/)
- :black_nib: [Nobody Talks About What Actually Makes Japanese Difficult](https://therenegadecoder.com/blog/nobody-talks-about-what-actually-makes-japanese-difficult/)
- :apple: [The Other Side of Letters of Recommendation](https://therenegadecoder.com/teach/the-other-side-of-letters-of-recommendation/)
- :black_nib: [Yet Another Consequence of Car-Centric Infrastructure](https://therenegadecoder.com/blog/yet-another-consequence-of-car-centric-infrastructure/)
- :apple: [What’s More Important: Having Knowledge or Knowing How to Access Knowledge?](https://therenegadecoder.com/teach/whats-more-important-having-knowledge-or-knowing-how-to-access-knowledge/)
- :black_nib: [Generative AI Lets You Be as Delusional as a CEO](https://therenegadecoder.com/blog/generative-ai-lets-you-be-as-delusional-as-a-ceo/)
- :black_nib: [Recommended Reading: “The Law of Leaky Abstractions” by Joel Spolsky](https://therenegadecoder.com/blog/recommended-reading-the-law-of-leaky-abstractions-by-joel-spolsky/)
- :black_nib: [LLMs Are Not Like Compilers](https://therenegadecoder.com/blog/llms-are-not-like-compilers/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-11-20 using [SnakeMD](https://www.snakemd.io).
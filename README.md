# Welcome to My Profile!

This week's code snippet, Baklava in Owl Lisp, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Owl Lisp
(define (string-repeat n str)
  (fold string-append "" (make-list n str))
)

(define (baklava-line n)
  (define num-spaces (abs n))
  (define num-stars (- 21 (* 2 num-spaces)))
  (print (string-repeat num-spaces " ") (string-repeat num-stars "*"))
)

(define (baklava n ne)
  (if (<= n ne)
    (begin
      (baklava-line n)
      (baklava (+ n 1) ne)
    )
  )
)

( (args) (baklava -10 10))
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :apple: [The Other Side of Letters of Recommendation](https://therenegadecoder.com/teach/the-other-side-of-letters-of-recommendation/)
- :black_nib: [Yet Another Consequence of Car-Centric Infrastructure](https://therenegadecoder.com/blog/yet-another-consequence-of-car-centric-infrastructure/)
- :apple: [What’s More Important: Having Knowledge or Knowing How to Access Knowledge?](https://therenegadecoder.com/teach/whats-more-important-having-knowledge-or-knowing-how-to-access-knowledge/)
- :black_nib: [Generative AI Lets You Be as Delusional as a CEO](https://therenegadecoder.com/blog/generative-ai-lets-you-be-as-delusional-as-a-ceo/)
- :black_nib: [Recommended Reading: “The Law of Leaky Abstractions” by Joel Spolsky](https://therenegadecoder.com/blog/recommended-reading-the-law-of-leaky-abstractions-by-joel-spolsky/)
- :black_nib: [LLMs Are Not Like Compilers](https://therenegadecoder.com/blog/llms-are-not-like-compilers/)
- :apple: [How Do We Assess Understanding in the Age of Slop?](https://therenegadecoder.com/teach/how-do-we-assess-understanding-in-the-age-of-slop/)
- :black_nib: [I Don’t Really Trust Surveys](https://therenegadecoder.com/blog/i-dont-really-trust-surveys/)
- :black_nib: [AI Literacy, Shame, and Nuance](https://therenegadecoder.com/blog/ai-literacy-shame-and-nuance/)
- :apple: [Recommended Reading: “To teach in the time of ChatGPT is to know pain” by Scott K. Johnson](https://therenegadecoder.com/teach/recommended-reading-to-teach-in-the-time-of-chatgpt-is-to-know-pain-by-scott-k-johnson/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-10-23 using [SnakeMD](https://www.snakemd.io).
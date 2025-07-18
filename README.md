# Welcome to My Profile!

This week's code snippet, Baklava in Ferret, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Ferret
(defn print-repeat-string
  ([s n]
    (if (> n 0)
      (do
        (print s)
        (print-repeat-string s (dec n))
      )
    )
  )
)

(defn baklava-line
  ([n]
    (let [
      num-spaces (abs n)
      num-stars (- 21 (* 2 num-spaces))
    ]
      (print-repeat-string " " num-spaces)
      (print-repeat-string "*" num-stars)
      (println)
    )
  )
)

(defn baklava
  ([n ne]
    (if (<= n ne)
      (do
        (baklava-line n)
        (baklava (inc n) ne)
      )
    )
  )
)

(do
  (baklava -10 10)
)
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Life Update: I’m Doing Well](https://therenegadecoder.com/blog/life-update-im-doing-well/)
- :black_nib: [The Worst Use Cases for Generative AI That Are Already Mainstream](https://therenegadecoder.com/blog/the-worst-use-cases-for-generative-ai-that-are-already-mainstream/)
- :black_nib: [ChatGPT Is Stack Overflow for the Lazy and Helpless](https://therenegadecoder.com/blog/chatgpt-is-stack-overflow-for-the-lazy-and-helpless/)
- :black_nib: [The Acceleration of the Enshittification of Everything](https://therenegadecoder.com/blog/the-acceleration-of-the-enshittification-of-everything/)
- :apple: [4 Values We Have to Stop Pushing in Engineering Education](https://therenegadecoder.com/teach/values-we-have-to-stop-pushing-in-engineering-education/)
- :black_nib: [Generative AI Has a Short Shelf Life](https://therenegadecoder.com/blog/generative-ai-has-a-short-shelf-life/)
- :black_nib: [Reflecting on My First Trip to Japan](https://therenegadecoder.com/blog/reflecting-on-my-first-trip-to-japan/)
- :apple: [SB1 Is the Death of Higher Education in Ohio](https://therenegadecoder.com/teach/sb1-is-the-death-of-higher-education-in-ohio/)
- :black_nib: [No, Generative AI Is Not Just Another Innovation](https://therenegadecoder.com/blog/no-generative-ai-is-not-just-another-innovation/)
- :apple: [Generative AI Makes It Feel Bad to Be an Educator](https://therenegadecoder.com/teach/generative-ai-makes-it-feel-bad-to-be-an-educator/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-07-18 using [SnakeMD](https://www.snakemd.io).
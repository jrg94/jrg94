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

- :apple: [Generative AI Makes It Feel Bad to Be an Educator](https://therenegadecoder.com/teach/generative-ai-makes-it-feel-bad-to-be-an-educator/)
- :black_nib: [The Problem With Centrism: A Case Study](https://therenegadecoder.com/blog/the-problem-with-centrism-a-case-study/)
- :apple: [Reflecting on My First Two Years as a Lecturer](https://therenegadecoder.com/teach/reflecting-on-my-first-two-years-as-a-lecturer/)
- :black_nib: [Why I Left Twitter](https://therenegadecoder.com/blog/why-i-left-twitter/)
- :computer: [A Case Study on the Philosophy of Software Design](https://therenegadecoder.com/code/a-case-study-on-the-philosophy-of-software-design/)
- :black_nib: [Inside the Mind of an Engineer: How to Make Societal Issues Worse](https://therenegadecoder.com/blog/inside-the-mind-of-an-engineer-how-to-make-societal-issues-worse/)
- :black_nib: [How Attack on Titan Undermines Its Own Message](https://therenegadecoder.com/blog/how-attack-on-titan-undermines-its-own-message/)
- :computer: [Migrating to Poetry 2.x With Some Best Practices](https://therenegadecoder.com/code/migrating-to-poetry-2-x-with-some-best-practices/)
- :black_nib: [Maybe Generative AI Is Just a Symptom of a Broader Problem in Tech](https://therenegadecoder.com/blog/maybe-generative-ai-is-just-a-symptom-of-a-broader-problem-in-tech/)
- :apple: [It’s Time to Collect Mid-Semester Feedback](https://therenegadecoder.com/teach/its-time-to-collect-mid-semester-feedback/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-05-16 using [SnakeMD](https://www.snakemd.io).
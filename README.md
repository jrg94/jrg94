# Welcome to My Profile!

This week's code snippet, Reverse String in Ocaml, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Ocaml
let reverse s =
  let len = String.length s in
  String.init len (fun i -> s.[len - i - 1])

let () =
  print_endline
    (match Sys.argv with [||] | [| _ |] -> "" | args -> reverse args.(1))
(* Any additional arguments are ignored, following the example of other samples in this repo *)
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [I Don’t Really Trust Surveys](https://therenegadecoder.com/blog/i-dont-really-trust-surveys/)
- :black_nib: [AI Literacy, Shame, and Nuance](https://therenegadecoder.com/blog/ai-literacy-shame-and-nuance/)
- :apple: [Recommended Reading: “To teach in the time of ChatGPT is to know pain” by Scott K. Johnson](https://therenegadecoder.com/teach/recommended-reading-to-teach-in-the-time-of-chatgpt-is-to-know-pain-by-scott-k-johnson/)
- :apple: [Writing Code on Paper Is Good Actually](https://therenegadecoder.com/teach/writing-code-on-paper-is-good-actually/)
- :black_nib: [People Don’t Like to Be Deceived (by AI)](https://therenegadecoder.com/blog/people-dont-like-to-be-deceived-by-ai/)
- :apple: [Generative AI in Education is Pay-to-Lose](https://therenegadecoder.com/teach/generative-ai-in-education-is-pay-to-lose/)
- :black_nib: [My First “I Have a Toddler” Moment](https://therenegadecoder.com/blog/my-first-i-have-a-toddler-moment/)
- :black_nib: [LLMs Got Everyone Sounding the Same Now](https://therenegadecoder.com/blog/llms-got-everyone-sounding-the-same-now/)
- :black_nib: [6v6 Overwatch Is a Joke](https://therenegadecoder.com/blog/6v6-overwatch-is-a-joke/)
- :black_nib: [I Genuinely Don’t Understand Why People Tolerate Hallucinations in AI](https://therenegadecoder.com/blog/i-genuinely-dont-understand-why-people-tolerate-hallucinations-in-ai/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-09-04 using [SnakeMD](https://www.snakemd.io).
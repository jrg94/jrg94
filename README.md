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

- :black_nib: [The Acceleration of the Enshittification of Everything](https://therenegadecoder.com/blog/the-acceleration-of-the-enshittification-of-everything/)
- :apple: [4 Values We Have to Stop Pushing in Engineering Education](https://therenegadecoder.com/teach/values-we-have-to-stop-pushing-in-engineering-education/)
- :black_nib: [Generative AI Has a Short Shelf Life](https://therenegadecoder.com/blog/generative-ai-has-a-short-shelf-life/)
- :black_nib: [Reflecting on My First Trip to Japan](https://therenegadecoder.com/blog/reflecting-on-my-first-trip-to-japan/)
- :apple: [SB1 Is the Death of Higher Education in Ohio](https://therenegadecoder.com/teach/sb1-is-the-death-of-higher-education-in-ohio/)
- :black_nib: [No, Generative AI Is Not Just Another Innovation](https://therenegadecoder.com/blog/no-generative-ai-is-not-just-another-innovation/)
- :apple: [Generative AI Makes It Feel Bad to Be an Educator](https://therenegadecoder.com/teach/generative-ai-makes-it-feel-bad-to-be-an-educator/)
- :black_nib: [The Problem With Centrism: A Case Study](https://therenegadecoder.com/blog/the-problem-with-centrism-a-case-study/)
- :apple: [Reflecting on My First Two Years as a Lecturer](https://therenegadecoder.com/teach/reflecting-on-my-first-two-years-as-a-lecturer/)
- :black_nib: [Why I Left Twitter](https://therenegadecoder.com/blog/why-i-left-twitter/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-06-27 using [SnakeMD](https://www.snakemd.io).
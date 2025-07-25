# Welcome to My Profile!

This week's code snippet, Baklava in Haskell, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Haskell
module Main where

main :: IO ()
main = putStrLn baklava

-- Create baklava where the top has 10 spaces and then 1 asterisk
baklava ::  String
baklava = baklavaGrow 10 1

-- Recursively grow the baklava until spaces <= zero
baklavaGrow :: Int -> Int -> String
baklavaGrow space asterisk
  | space <= 0 = line 0     asterisk ++ "\n" ++ baklavaShrink 1          (asterisk - 2)
  | otherwise  = line space asterisk ++ "\n" ++ baklavaGrow   (space - 1) (asterisk + 2)

-- Recursively shrink the baklava until asterisks <= zero
baklavaShrink :: Int -> Int -> String
baklavaShrink space asterisk
  | asterisk <= 1 = line space 1
  | otherwise     = line space asterisk ++ "\n" ++ baklavaShrink (space + 1) (asterisk - 2)

-- Return a single line of the baklava
line space asterisk = replicate space ' ' ++ replicate asterisk '*'
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [“Just Ask Chat”: The Evolution of an Isolating Mantra](https://therenegadecoder.com/blog/just-ask-chat-the-evolution-of-an-isolating-mantra/)
- :black_nib: [Life Update: I’m Doing Well](https://therenegadecoder.com/blog/life-update-im-doing-well/)
- :black_nib: [The Worst Use Cases for Generative AI That Are Already Mainstream](https://therenegadecoder.com/blog/the-worst-use-cases-for-generative-ai-that-are-already-mainstream/)
- :black_nib: [ChatGPT Is Stack Overflow for the Lazy and Helpless](https://therenegadecoder.com/blog/chatgpt-is-stack-overflow-for-the-lazy-and-helpless/)
- :black_nib: [The Acceleration of the Enshittification of Everything](https://therenegadecoder.com/blog/the-acceleration-of-the-enshittification-of-everything/)
- :apple: [4 Values We Have to Stop Pushing in Engineering Education](https://therenegadecoder.com/teach/values-we-have-to-stop-pushing-in-engineering-education/)
- :black_nib: [Generative AI Has a Short Shelf Life](https://therenegadecoder.com/blog/generative-ai-has-a-short-shelf-life/)
- :black_nib: [Reflecting on My First Trip to Japan](https://therenegadecoder.com/blog/reflecting-on-my-first-trip-to-japan/)
- :apple: [SB1 Is the Death of Higher Education in Ohio](https://therenegadecoder.com/teach/sb1-is-the-death-of-higher-education-in-ohio/)
- :black_nib: [No, Generative AI Is Not Just Another Innovation](https://therenegadecoder.com/blog/no-generative-ai-is-not-just-another-innovation/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-07-25 using [SnakeMD](https://www.snakemd.io).
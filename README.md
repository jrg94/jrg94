# Welcome to My Profile!

This week's code snippet, Reverse String in Vimscript, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Vimscript
func! Reverse(str)
    return join(reverse(split(a:str, '\zs')), '')
endfunc

func! Main(...)
    echo Reverse(a:0 > 0 ? a:1 : '')
endfunc
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [What Is Snake Case in Python?](https://therenegadecoder.com/code/what-is-snake-case-in-python/)
- :black_nib: [The Name 100 Women Challenge](https://therenegadecoder.com/blog/the-name-100-women-challenge/)
- :black_nib: [All But Dissertation: The Light at the End of the Tunnel](https://therenegadecoder.com/blog/all-but-dissertation-the-light-at-the-end-of-the-tunnel/)
- :computer: [What Are Special Methods in Python?](https://therenegadecoder.com/code/what-are-special-methods-in-python/)
- :computer: [What Is Iterable Unpacking in Python?](https://therenegadecoder.com/code/what-is-iterable-unpacking-in-python/)
- :computer: [What Is an Iterable in Python?](https://therenegadecoder.com/code/what-is-an-iterable-in-python/)
- :black_nib: [Meritocracy: The Facade That Determines Who Deserves Success](https://therenegadecoder.com/blog/meritocracy-the-facade-that-determines-who-deserves-success/)
- :apple: [6 Tips for New College and University Educators](https://therenegadecoder.com/teach/6-tips-for-new-college-and-university-educators/)
- :black_nib: [Checking Up on Google Search in 2024: It’s Worse Somehow](https://therenegadecoder.com/blog/checking-up-on-google-search-in-2024-its-worse-somehow/)
- :black_nib: [Google Threatens to Ruin Search as We Know It](https://therenegadecoder.com/blog/google-threatens-to-ruin-search-as-we-know-it/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-07-26 using [SnakeMD](https://www.snakemd.io).
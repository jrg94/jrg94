# Welcome to My Profile!

This week's code snippet, Fizz Buzz in Vimscript, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Vimscript
func! FizzBuzz()
    for l:i in range(1, 100)
        if l:i % 15 == 0
            let l:str = 'FizzBuzz'
        elseif l:i % 5 == 0
            let l:str = 'Buzz'
        elseif l:i % 3 == 0
            let l:str = 'Fizz'
        else
            let l:str = l:i
        endif

        call append(l:i-1, l:str)
    endfor

    " go to top of buffer
    normal gg
endfunc

au BufEnter,BufReadPost * call FizzBuzz()
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :cat: [Why Is Adding Two Random Numbers Not the Same as Generating One in the Same Range?](https://therenegadecoder.com/code/why-is-adding-two-random-numbers-not-the-same-as-generating-one-in-the-same-range/)
- :fu: [Design by Contract Hinges on Implication](https://therenegadecoder.com/code/design-by-contract-hinges-on-implication/)
- :tea: [Maybe It’s Not Okay to Test Private Methods—at Least When Using Design by Contract](https://therenegadecoder.com/code/maybe-its-not-okay-to-test-private-methods-at-least-when-using-design-by-contract/)
- :exclamation: [29 Things I’d Only Say If I Were Kidnapped](https://therenegadecoder.com/blog/29-things-id-only-say-if-i-were-kidnapped/)
- :dango: [Why Does == Sometimes Work on Strings in Java?](https://therenegadecoder.com/code/why-does-double-equals-sometimes-work-on-strings-in-java/)
- :seedling: [2022: Year in Review](https://therenegadecoder.com/meta/2022-year-in-review/)
- :exclamation: [Reflecting on My 8th Semester of Teaching: Autumn 2022](https://therenegadecoder.com/blog/reflecting-on-my-8th-semester-of-teaching-autumn-2022/)
- :exclamation: [There Has to Be a Better Way: Reflecting on My Automation Catchphrase](https://therenegadecoder.com/blog/there-has-to-be-a-better-way-reflecting-on-my-automation-catchphrase/)
- :dango: [I Am a PhD Candidate!](https://therenegadecoder.com/blog/i-am-a-phd-candidate/)
- :dango: [Where Do Foo, Bar, and Baz Come From in Programming?](https://therenegadecoder.com/blog/where-do-foo-bar-and-baz-come-from-in-programming/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2023-02-24 using [SnakeMD](https://www.snakemd.io).
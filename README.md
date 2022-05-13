# Welcome to My Profile!

This week's code snippet, Hello World in Debug, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Debug
; ------------------------------------------------------------------
; helloworld.asm
;
; This is a Win64 console program that writes "Hello World"
; on a single line and then exits.
;
; To assemble to .obj: nasm -f Win64 helloworld.asm
; To compile to .exe:  gcc helloworld.obj -o helloworld.exe
; ------------------------------------------------------------------

        global    _main                ; declare main() method
        extern    _printf              ; link to external library

        segment  .data
        message: db   'Hello world', 0xA, 0  ; text message
                    ; 0xA (10) is hex for (NL), carriage return
                    ; 0 terminates the line

        ; code is put in the .text section
        section .text
_main:                            ; the entry point! void main()
        push    message           ; save message to the stack
        call    _printf           ; display the first value on the stack
        add     esp, 4            ; clear the stack
        ret                       ; return
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :gem: [The Complete Guide to SnakeMD: A Python Library for Generating Markdown](https://therenegadecoder.com/code/the-complete-guide-to-snakemd-a-python-library-for-generating-markdown/)
- :notes: [The Complete Guide to Subete: A Python Library for Browsing Code Snippets](https://therenegadecoder.com/code/the-complete-guide-to-subete-a-python-library-for-browsing-code-snippets/)
- :seedling: [Stop Using Flags to Control Your Loops](https://therenegadecoder.com/code/stop-using-flags-to-control-your-loops/)
- :seedling: [Celebrating 500 Articles on The Renegade Coder](https://therenegadecoder.com/meta/celebrating-500-articles-on-the-renegade-coder/)
- :milky_way: [The Great Subdomain Purge: Sample Programs Has a New Home](https://therenegadecoder.com/meta/the-great-subdomain-purge-sample-programs-has-a-new-home/)
- :notes: [Meet Pymon: A Discord Bot That Can Answer Any Question You Want](https://therenegadecoder.com/teach/meet-pymon-a-discord-bot-that-can-answer-any-question-you-want/)
- :tea: [How to Generate Any Random Number From a Zero to One Range](https://therenegadecoder.com/code/how-to-generate-any-random-number-from-a-zero-to-one-range/)
- :gem: [ULPT: How to Cheat on Programming Assignments and Get Away With It](https://therenegadecoder.com/teach/ulpt-how-to-cheat-on-programming-assignments-and-get-away-with-it/)
- :gem: [I Won the Graduate Associate Teaching Award!](https://therenegadecoder.com/teach/i-won-the-graduate-associate-teaching-award/)
- :door: [Improve Code Readability by Using Parameter Modes](https://therenegadecoder.com/code/improve-code-readability-by-using-parameter-modes/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2022-05-13 using [SnakeMD](https://snakemd.therenegadecoder.com).
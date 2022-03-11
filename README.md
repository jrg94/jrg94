# Welcome to My Profile!

This week's code snippet, Prime Number in Rexx, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Rexx
/* ARG with source string named in REXX program invocation */
arg number
If (DATATYPE(number, 'W') == 0) then signal err
If (number < 0) then signal err
isPrime = 1
if \((number // 2 = 0) & (number \= 2) | (number == 1)) then
	do
		i = TRUNC(number / 2)
		do while(i > 3)
			if (number // i == 0) then
				isPrime = 0
			i = i - 1
		end
	end
else
	isPrime = 0

if (isPrime == 1) then
	say "Prime"
else
	say "Composite"
;exit

Err:
say 'Usage: please input a non-negative integer'; exit
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :lock: [Improve Code Readability by Using Parameter Modes](https://therenegadecoder.com/code/improve-code-readability-by-using-parameter-modes/)
- :tea: [What Is a Magic Number And How Do We Fix It?](https://therenegadecoder.com/code/what-is-a-magic-number-and-how-do-we-fix-it/)
- :dango: [How to Swap Java Reference Types in a Method](https://therenegadecoder.com/code/how-to-swap-java-reference-types-in-a-method/)
- :dango: [Is It Okay to Complain About Students in Higher Education?](https://therenegadecoder.com/teach/is-it-okay-to-complain-about-students-in-higher-education/)
- :exclamation: [How to Code Wordle Into a Discord Bot](https://therenegadecoder.com/code/how-to-code-wordle-into-a-discord-bot/)
- :fu: [The 28 Best Programming Languages of All Time](https://therenegadecoder.com/code/the-28-best-programming-languages-of-all-time/)
- :seedling: [Beware of Division by Zero in Java](https://therenegadecoder.com/code/beware-of-division-by-zero-in-java/)
- :cat: [2021: Year in Review](https://therenegadecoder.com/meta/2021-year-in-review/)
- :fu: [How to Convert Markdown to a PDF: 3 Quick Solutions](https://therenegadecoder.com/blog/how-to-convert-markdown-to-a-pdf-3-quick-solutions/)
- :door: [SnakeMD 0.10.x Features Checklists](https://therenegadecoder.com/meta/snakemd-0-10-x-features-checklists/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2022-03-11 using [SnakeMD](https://snakemd.therenegadecoder.com).
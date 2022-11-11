# Welcome to My Profile!

This week's code snippet, Fibonacci in Verilog, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Verilog
//Verilog code Listing first 25 Fibonacci numbers till

module Fibonacci();

integer previous_value = 0;
integer current_value = 1;
integer clk = 0;

always #1 
    clk = ~clk;

always @(posedge clk)
begin
    current_value <= current_value + previous_value;
    previous_value <= current_value;
    $display("%0d", current_value);
end

initial #50 //Prints 25 fibonacci numbers as values change at POSEDGE of clock
    $finish;

endmodule
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :dango: [Java Lambda Expressions Are a Scam](https://therenegadecoder.com/code/java-lambda-expressions-are-a-scam/)
- :seedling: [Unpacking CS Jargon: What Makes Data Mutable?](https://therenegadecoder.com/code/unpacking-cs-jargon-what-makes-data-mutable/)
- :milky_way: [Unpacking CS Jargon: Static Vs. Dynamic Types](https://therenegadecoder.com/code/unpacking-cs-jargon-static-vs-dynamic-types/)
- :fu: [The Official Recursion Cheat Sheet](https://therenegadecoder.com/code/the-official-recursion-cheat-sheet/)
- :gem: [What Is Aliasing in Computer Science? Why Does It Happen? And Is It Bad?](https://therenegadecoder.com/code/what-is-aliasing-in-computer-science-why-does-it-happen-and-is-it-bad/)
- :dango: [5 Tips for Making Sense of Recursion](https://therenegadecoder.com/code/5-tips-for-making-sense-of-recursion/)
- :cat: [Explain Like I’m Five: Method Overloading](https://therenegadecoder.com/code/explain-like-im-five-method-overloading/)
- :lock: [Understanding Short-Circuit Evaluation in Software Design](https://therenegadecoder.com/code/understanding-short-circuit-evaluation-in-software-design/)
- :tea: [I Finally Figured Out Python’s Module and Package System](https://therenegadecoder.com/code/i-finally-figured-out-pythons-module-and-package-system/)
- :exclamation: [How to Reason About Your Code With a Tracing Table](https://therenegadecoder.com/code/how-to-reason-about-your-code-with-a-tracing-table/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2022-11-11 using [SnakeMD](https://www.snakemd.io).
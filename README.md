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

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [The Difference Between str() and repr() in Python: A Design by Contract Perspective](https://therenegadecoder.com/code/the-difference-between-str-and-repr-in-python-a-design-by-contract-perspective/)
- :computer: [Obfuscation Techniques: Magic Numbers](https://therenegadecoder.com/code/obfuscation-techniques-magic-numbers/)
- :computer: [Obfuscation Techniques: No More Type Hints](https://therenegadecoder.com/code/obfuscation-techniques-no-more-type-hints/)
- :computer: [Obfuscation Techniques: Visually Similar Characters](https://therenegadecoder.com/code/obfuscation-techniques-visually-similar-characters/)
- :computer: [Obfuscation Techniques: Shadowing Built-in Functions](https://therenegadecoder.com/code/obfuscation-techniques-shadowing-built-in-functions/)
- :computer: [Obfuscation Techniques: Writing Malicious Comments](https://therenegadecoder.com/code/obfuscation-techniques-writing-malicious-comments/)
- :computer: [Obfuscation Techniques: The Yoda Conditional](https://therenegadecoder.com/code/obfuscation-techniques-the-yoda-conditional/)
- :apple: [Students Should Be Able to Build a Portfolio From Their Coursework](https://therenegadecoder.com/teach/students-should-be-able-to-build-a-portfolio-from-their-coursework/)
- :apple: [Why I’m No Longer Giving Paper Exams in My Computer Science Courses](https://therenegadecoder.com/teach/why-im-no-longer-giving-paper-exams-in-my-computer-science-courses/)
- :black_nib: [Make TODO Lists More Meaningful By Reflecting on Your Values](https://therenegadecoder.com/blog/make-todo-lists-more-meaningful-by-reflecting-on-your-values/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-11-24 using [SnakeMD](https://www.snakemd.io).
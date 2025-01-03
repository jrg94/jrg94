# Welcome to My Profile!

This week's code snippet, Palindromic Number in Julia, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Julia
function err() 
  println("Usage: please input a non-negative integer")
end

function palindrome_check(n)
  new_num = 0
  original = n
  while (n > 0)
    digit = n % 10
    new_num = new_num * 10 + digit 
    n = 10
  end

  if(new_num == original)
      return "true"
  else
      return "false"
  end
end

try
   n = parse(Int, ARGS[1])
   if (n >= 0)
     println(palindrome_check(n))
   else
     err()
   end
catch e
   err()
end
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :apple: [Canvas Is Not Built With Educators in Mind](https://therenegadecoder.com/teach/canvas-is-not-built-with-educators-in-mind/)
- :computer: [Workshopping a Tier List Generator](https://therenegadecoder.com/code/workshopping-a-tier-list-generator/)
- :black_nib: [No, The GRE Should Not Be Reinstated](https://therenegadecoder.com/blog/no-the-gre-should-not-be-reinstated/)
- :black_nib: [Summarizing My Dissertation for the Layman](https://therenegadecoder.com/blog/summarizing-my-dissertation-for-the-layman/)
- :black_nib: [9 Things I Wish I Knew About Doctoral Programs](https://therenegadecoder.com/blog/things-i-wish-i-knew-about-doctoral-programs/)
- :black_nib: [I Successfully Completed My PhD in Engineering Education](https://therenegadecoder.com/blog/i-successfully-completed-my-phd-in-engineering-education/)
- :apple: [So You Want to Be a University Educator](https://therenegadecoder.com/teach/so-you-want-to-be-a-university-educator/)
- :black_nib: [Looking Forward to the Future](https://therenegadecoder.com/blog/looking-forward-to-the-future/)
- :computer: [Unpacking the Jargon Around Compilers, Interpreters, and More](https://therenegadecoder.com/code/unpacking-the-jargon-around-compilers-interpreters-and-more/)
- :computer: [What Are Type Hints in Python?](https://therenegadecoder.com/code/what-are-type-hints-in-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-01-03 using [SnakeMD](https://www.snakemd.io).
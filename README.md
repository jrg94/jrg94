# Welcome to My Profile!

This week's code snippet, Selection Sort in Matlab, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Matlab
function sorted = selection_sort(array)
  if nargin == 0 || length(array)<=1
      fprintf("Usage: please provide a list of at least two integers to sort in the format [1 2 3 4 5]\n");
      return
  end  
  
  sorted = [];
  while ~isempty(array)
      x = min(array);
      sorted = [ sorted array(array==x) ];
      array(array==x) = [];  
  end
end
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [5 Beginner Tricks for Writing Your Own Unit Tests](https://therenegadecoder.com/code/beginner-tricks-for-writing-your-own-unit-tests/)
- :thought_balloon: [Transition Madness: Becoming a Lecturer](https://therenegadecoder.com/meta/transition-madness-becoming-a-lecturer/)
- :black_nib: [I Am Officially a Lecturer](https://therenegadecoder.com/blog/i-am-officially-a-lecturer/)
- :black_nib: [CampusParc Has Got to Go](https://therenegadecoder.com/blog/campusparc-has-got-to-go/)
- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)
- :computer: [5 Absurd Ways to Add Two Numbers in Python](https://therenegadecoder.com/code/5-absurd-ways-to-add-two-numbers-in-python/)
- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)
- :black_nib: [Using Ethnography to Advocate for Student Needs in Computer Science Education](https://therenegadecoder.com/blog/using-ethnography-to-advocate-for-student-needs-in-computer-science-education/)
- :computer: [3 Key Programming Best Practices for Beginners](https://therenegadecoder.com/code/programming-best-practices-for-beginners/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-08-25 using [SnakeMD](https://www.snakemd.io).
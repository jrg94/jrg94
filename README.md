# Welcome to My Profile!

This week's code snippet, Merge Sort in Matlab, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Matlab
function [result] = MyMergeSort( x )
% Sort vector 'x' using the merge sort algorithm
% result is a vector consisting of the sorted values of 'x' 
% in ascended order
% Takes O( n log n ) time
% Requires extra memory for merging results

n = length(x);
if n == 1
    % Stop the recursion, if we are down to one element in list
    result = x;
else
    m = floor(n/2);  % Get the half way point

    r1 = MyMergeSort( x(1:m) );    % Sort first half recursively...
    r2 = MyMergeSort( x(m+1:n) );  % Sort 2nd half recursively...
    result = MyMerge( r1, r2 );    % Merge the two halves in sorted order
end

function c = MyMerge( a, b )
% Merges 2 vectors a,b into a result vector c 
%   assumes a, b are already sorted
%   'c' will also be in sorted order

aLen = length(a);  % get length of a
bLen = length(b);  % get length of b
cLen = aLen+bLen;
c = zeros(1,cLen); % pre-allocate 'c' to correct size

% Initialize starting indices
aIdx = 1;
bIdx = 1;
for cIdx = 1:cLen
  % Should we grab from 'a' or 'b' ???
  if aIdx > aLen
    % All done with 'a' vector, grab from 'b' vector.
    c(cIdx) = b(bIdx); 
    bIdx = bIdx + 1;
  elseif bIdx > bLen
    % All done with 'b' vector, grab from 'a' vector
    c(cIdx) = a(aIdx); 
    aIdx = aIdx + 1;
  elseif a(aIdx) <= b(bIdx)
     % a(i) <= b(i), grab from 'a' vector
     c(cIdx) = a(aIdx); 
     aIdx = aIdx + 1;
  else
    % b(i) < a(i), grab from 'b' vector
    c(cIdx) = b(bIdx); 
    bIdx = bIdx + 1;
  end
end

% BY - Nikhil Gupta
% GitHub - nikkkhil067
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [The World Is Built on Abstractions](https://therenegadecoder.com/blog/the-world-is-built-on-abstractions/)
- :computer: [5 Beginner Tricks for Writing Your Own Unit Tests](https://therenegadecoder.com/code/beginner-tricks-for-writing-your-own-unit-tests/)
- :thought_balloon: [Transition Madness: Becoming a Lecturer](https://therenegadecoder.com/meta/transition-madness-becoming-a-lecturer/)
- :black_nib: [I Am Officially a Lecturer](https://therenegadecoder.com/blog/i-am-officially-a-lecturer/)
- :black_nib: [CampusParc Has Got to Go](https://therenegadecoder.com/blog/campusparc-has-got-to-go/)
- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)
- :computer: [5 Absurd Ways to Add Two Numbers in Python](https://therenegadecoder.com/code/5-absurd-ways-to-add-two-numbers-in-python/)
- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)
- :black_nib: [Using Ethnography to Advocate for Student Needs in Computer Science Education](https://therenegadecoder.com/blog/using-ethnography-to-advocate-for-student-needs-in-computer-science-education/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-09-01 using [SnakeMD](https://www.snakemd.io).
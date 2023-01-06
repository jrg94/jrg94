# Welcome to My Profile!

This week's code snippet, Insertion Sort in Matlab, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Matlab
function sorted = insertion_sort(array)
% Insertion sort in ascending order

if(size(array,1)>1)
    error('Input must be a 1xN vector');
end
if(isempty(array))
    error('Input should not be empty');
end
disp(['Array to be sorted: ' num2str(array)]);
n = length(array);
for i = 2:n
    d = i;    
    while((d > 1) && (array(d) < array(d-1)))
        temp = array(d);
        array(d) = array(d-1);
        array(d-1) = temp;
        d = d-1;
    end
end
sorted = array;
disp(['Sorted Array: ' num2str(array)]);
end

input_array = [9 8 7 6 5 4];
%input_array element can be different
output_array = insertion_sort(input_array);
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :notes: [There Has to Be a Better Way: Reflecting on My Automation Catchphrase](https://therenegadecoder.com/blog/there-has-to-be-a-better-way-reflecting-on-my-automation-catchphrase/)
- :seedling: [I Am a PhD Candidate!](https://therenegadecoder.com/blog/i-am-a-phd-candidate/)
- :milky_way: [Where Do Foo, Bar, and Baz Come From in Programming?](https://therenegadecoder.com/blog/where-do-foo-bar-and-baz-come-from-in-programming/)
- :gem: [How to Clamp a Floating Point Number in Python: Branching, Sorting, and More!](https://therenegadecoder.com/code/how-to-clamp-a-floating-point-number-in-python/)
- :notes: [Master Chief Collection’s Halo 2 Co-op Campaign Is Unplayable: Here Are Some Tips](https://therenegadecoder.com/blog/master-chief-collections-halo-2-co-op-campaign-is-unplayable-here-are-some-tips/)
- :fu: [How to Convert sqlite3 Rows into Python Objects](https://therenegadecoder.com/code/how-to-convert-sqlite3-rows-into-python-objects/)
- :fu: [5 Ways to Share Code in Discord](https://therenegadecoder.com/code/5-ways-to-share-code-in-discord/)
- :notes: [Learning Recursion? Try Bloom’s Taxonomy](https://therenegadecoder.com/blog/learning-recursion-try-blooms-taxonomy/)
- :dango: [Java Lambda Expressions Are a Scam](https://therenegadecoder.com/code/java-lambda-expressions-are-a-scam/)
- :milky_way: [Unpacking CS Jargon: What Makes Data Mutable?](https://therenegadecoder.com/code/unpacking-cs-jargon-what-makes-data-mutable/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2023-01-06 using [SnakeMD](https://www.snakemd.io).
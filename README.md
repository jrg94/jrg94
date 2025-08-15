# Welcome to My Profile!

This week's code snippet, Merge Sort in Octave, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Octave
function merge_sort()
    %input validation
    usage = 'Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"';
    arg_list = argv();
    nargin = length(arg_list);
    if  nargin == 0
        %if there was no input
        disp(usage);
        return;
    end

    array_string = arg_list{1};
    array_size = sum(array_string == ',') + 1;
    if array_size < 2
        disp(usage);
        return;
    end

    %build array
    array = str2num(array_string);
    if length(array) ~= array_size || any(mod(array, 1) ~= 0)
        disp(usage);
        return;
    end

    %merge sort in ascending order
    array = MyMergeSort(array);

    %convert to string
    result_string = num2str(array);

    %replace space with ', '
    result_string = regexprep(result_string, '\s+', ', ');
    disp(result_string);
end

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
end

% BY - Nikhil Gupta
% GitHub - nikkkhil067
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [Loop Invariants Are Necessary for Writing Proper Loops](https://therenegadecoder.com/code/loop-invariants-are-necessary-for-writing-proper-loops/)
- :computer: [Dark Arts: Labeled Statements in Java](https://therenegadecoder.com/code/dark-arts-labeled-statements-in-java/)
- :apple: [Gamification Will Not Solve “America’s Education Crisis”](https://therenegadecoder.com/teach/gamification-will-not-solve-americas-education-crisis/)
- :black_nib: [“Just Ask Chat”: The Evolution of an Isolating Mantra](https://therenegadecoder.com/blog/just-ask-chat-the-evolution-of-an-isolating-mantra/)
- :black_nib: [Life Update: I’m Doing Well](https://therenegadecoder.com/blog/life-update-im-doing-well/)
- :black_nib: [The Worst Use Cases for Generative AI That Are Already Mainstream](https://therenegadecoder.com/blog/the-worst-use-cases-for-generative-ai-that-are-already-mainstream/)
- :black_nib: [ChatGPT Is Stack Overflow for the Lazy and Helpless](https://therenegadecoder.com/blog/chatgpt-is-stack-overflow-for-the-lazy-and-helpless/)
- :black_nib: [The Acceleration of the Enshittification of Everything](https://therenegadecoder.com/blog/the-acceleration-of-the-enshittification-of-everything/)
- :apple: [4 Values We Have to Stop Pushing in Engineering Education](https://therenegadecoder.com/teach/values-we-have-to-stop-pushing-in-engineering-education/)
- :black_nib: [Generative AI Has a Short Shelf Life](https://therenegadecoder.com/blog/generative-ai-has-a-short-shelf-life/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-08-15 using [SnakeMD](https://www.snakemd.io).
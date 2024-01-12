# Welcome to My Profile!

This week's code snippet, Selection Sort in Julia, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Julia
#!/usr/bin/julia

function SelectionSort(arr)
    l = length(arr)
    sorted_list = []
    for i = 1:l
        m = minimum(arr)
        push!(sorted_list,m)
        deleteat!(arr, findfirst(x->x==m,arr))
    end
    return sorted_list
end

function error()
    println("Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"")
end

function HandleInput(inp)

    a = split(inp,",")
    a = map(x->split(x," "),a)
    a = map(x->last(x),a)
    numbers = map(x->parse(Int,x),a)
    if length(numbers) == 1
        error()
        exit()
    end
    return numbers
    
end

function PrintOutput(out)
    for i = 1:length(out)
        print(out[i])
        if i != length(out)
            print(", ")
        end
    end
    println()
end

try

    n = HandleInput(ARGS[1])
    sorted = SelectionSort(n)
    PrintOutput(sorted)

catch e
    error()
end
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [Migrating From Eclipse to VS Code: The Many Hurdles](https://therenegadecoder.com/code/migrating-from-eclipse-to-vs-code-the-many-hurdles/)
- :black_nib: [2023: Year in Review](https://therenegadecoder.com/blog/2023-year-in-review/)
- :computer: [How to Plot Semesters Using Pandas and Plotly](https://therenegadecoder.com/code/how-to-plot-semesters-using-pandas-and-plotly/)
- :apple: [Reflecting on Two More Semesters of Teaching: Spring & Autumn 2023](https://therenegadecoder.com/teach/reflecting-on-two-more-semesters-of-teaching-spring-autumn-2023/)
- :black_nib: [Grade Inflation Is Bullshit](https://therenegadecoder.com/blog/grade-inflation-is-bullshit/)
- :computer: [Brainstorming An Algorithm for Shuffling a Queue of Songs](https://therenegadecoder.com/code/brainstorming-an-algorithm-for-shuffling-a-queue-of-songs/)
- :computer: [Trust Me! Your Code Isn’t That Bad](https://therenegadecoder.com/code/trust-me-your-code-isnt-that-bad/)
- :computer: [The Difference Between str() and repr() in Python: A Design by Contract Perspective](https://therenegadecoder.com/code/the-difference-between-str-and-repr-in-python-a-design-by-contract-perspective/)
- :computer: [Obfuscation Techniques: Magic Numbers](https://therenegadecoder.com/code/obfuscation-techniques-magic-numbers/)
- :computer: [Obfuscation Techniques: No More Type Hints](https://therenegadecoder.com/code/obfuscation-techniques-no-more-type-hints/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-01-12 using [SnakeMD](https://www.snakemd.io).
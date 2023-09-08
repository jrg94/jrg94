# Welcome to My Profile!

This week's code snippet, Longest Common Subsequence in Kotlin, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Kotlin
private fun lcsOf(a: MutableList<String>, b: MutableList<String>, indexA: Int, indexB: Int): MutableList<String> {
    return if (indexA < 0 || indexB < 0) {
        mutableListOf()
    } else if (a[indexA] == b[indexB]) {
        // get the best subsequence of the rest, then add this one at the end (prevents needing to reverse at the end)
        lcsOf(a, b, indexA - 1, indexB - 1).also { it.add(a[indexA] )}
    } else {
        // compare both subsequences and return the one that has more element
        val subA = lcsOf(a, b, indexA, indexB - 1)
        val subB = lcsOf(a, b, indexA - 1, indexB)
        if (subA.size >= subB.size) subA else subB
    }
}

// only require consumers to pass in the lists... we'll handle the indices ourselves
fun lcsOf(a: List<String>, b: List<String>) = lcsOf(a.toMutableList(), b.toMutableList(), a.size - 1, b.size - 1)

fun main(args: Array<String>) {
    if (args.size != 2 || args[0].isBlank() || args[1].isBlank()) {
        // print and exit if we don't have the correct number of arguments
        println("Usage: please provide two lists in the format \"1, 2, 3, 4, 5\"")
        return
    }

    // split each argument by comma, remove whitespace around each element, and pack them all in a list
    val seqA = args[0].split(",").map { it.trim() }
    val seqB = args[1].split(",").map { it.trim() }

    lcsOf(seqA, seqB).joinToString(", ").also { println(it) }
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [The Two-Layer Approach to Software Design](https://therenegadecoder.com/blog/the-two-layer-approach-to-software-design/)
- :black_nib: [The World Is Built on Abstractions](https://therenegadecoder.com/blog/the-world-is-built-on-abstractions/)
- :computer: [5 Beginner Tricks for Writing Your Own Unit Tests](https://therenegadecoder.com/code/beginner-tricks-for-writing-your-own-unit-tests/)
- :thought_balloon: [Transition Madness: Becoming a Lecturer](https://therenegadecoder.com/meta/transition-madness-becoming-a-lecturer/)
- :black_nib: [I Am Officially a Lecturer](https://therenegadecoder.com/blog/i-am-officially-a-lecturer/)
- :black_nib: [CampusParc Has Got to Go](https://therenegadecoder.com/blog/campusparc-has-got-to-go/)
- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)
- :computer: [5 Absurd Ways to Add Two Numbers in Python](https://therenegadecoder.com/code/5-absurd-ways-to-add-two-numbers-in-python/)
- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-09-08 using [SnakeMD](https://www.snakemd.io).
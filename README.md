# Welcome to My Profile!

This week's code snippet, Selection Sort in Python, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Python
import sys


def selection_sort(xs, sorted_xs=None):
    sorted_xs = sorted_xs or []
    if len(xs) <= 0:
        return sorted_xs
    x = min(xs)
    sorted_xs.append(x)
    xs.remove(x)
    return selection_sort(xs, sorted_xs)


def input_list(list_str):
    return [int(x.strip(" "), 10) for x in list_str.split(',')]


def exit_with_error():
    print('Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"')
    sys.exit(1)


def main(args):
    try:
        xs = input_list(args[0])
        if len(xs) <= 1:
            exit_with_error()
        print(selection_sort(xs))
    except (IndexError, ValueError):
        exit_with_error()


if __name__ == "__main__":
    main(sys.argv[1:])
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)
- :computer: [5 Absurd Ways to Add Two Numbers in Python](https://therenegadecoder.com/code/5-absurd-ways-to-add-two-numbers-in-python/)
- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)
- :black_nib: [Using Ethnography to Advocate for Student Needs in Computer Science Education](https://therenegadecoder.com/blog/using-ethnography-to-advocate-for-student-needs-in-computer-science-education/)
- :computer: [3 Key Programming Best Practices for Beginners](https://therenegadecoder.com/code/programming-best-practices-for-beginners/)
- :black_nib: [What Restoring a 20-Year-Old Deck Looks Like](https://therenegadecoder.com/blog/what-refreshing-a-20-year-old-deck-looks-like/)
- :black_nib: [Java Has A Remainder Operator—Not a Mod Operator](https://therenegadecoder.com/blog/java-has-a-remainder-operator-not-a-mod-operator/)
- :black_nib: [5 Things You Should Know Before You Pick Up Python](https://therenegadecoder.com/blog/things-you-should-know-before-you-pick-up-python/)
- :black_nib: [Flexible Interfaces With Optional Methods Are Good: A Java List Case Study](https://therenegadecoder.com/blog/flexible-interfaces-with-optional-methods-are-good-a-java-list-case-study/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-07-21 using [SnakeMD](https://www.snakemd.io).
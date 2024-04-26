# Welcome to My Profile!

This week's code snippet, Factorial in Euphoria, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Euphoria
include std/io.e
include std/types.e
include std/text.e
include std/get.e as stdget
include std/math.e

-- Indices for value() return value
enum VALUE_ERROR_CODE, VALUE_VALUE, VALUE_NUM_CHARS_READ

-- Indices for parse_int() return value
enum PARSE_INT_VALID, PARSE_INT_VALUE

function parse_int(sequence s)
    -- Trim off whitespace and parse string
    s = trim(s)
    sequence result = stdget:value(s,, GET_LONG_ANSWER)

    -- Error if any errors, value is not an integer, or any leftover characters
    boolean valid = (
        result[VALUE_ERROR_CODE] = GET_SUCCESS
        and integer(result[VALUE_VALUE])
        and result[VALUE_NUM_CHARS_READ] = length(s)
    )

    -- Get value if invalid
    integer value = 0
    if valid
    then
        value = result[VALUE_VALUE]
    end if

    return {valid, value}
end function

procedure usage()
    puts(STDOUT, "Usage: please input a non-negative integer\n")
    abort(0)
end procedure

function factorial(integer value)
    -- Multiply from 1 through n (note that 0! = 1)
    atom fact = 1
    for n = 2 to value
    do
        -- Exit if next multiplication will cause an overlow
        fact *= n
        if not integer(fact)
        then
            puts(STDERR, "Overflow!\n")
            abort(0)
        end if
    end for

    return fact
end function

-- Check 1st command-line argument
sequence argv = command_line()
if length(argv) < 4 or length(argv[4]) = 0
then
    usage()
end if

-- Parse 1st command-line argument
sequence result = parse_int(argv[4])
integer value = result[PARSE_INT_VALUE]
if not result[PARSE_INT_VALID] or value < 0
then
    usage()
end if

-- Calculate and display factorial
atom fact = factorial(value)
printf(STDOUT, "%d\n", {fact})
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [How to Automatically Calculate Letter Grades, But Every Solution Is Bad](https://therenegadecoder.com/code/how-to-automatically-calculate-letter-grades-but-every-solution-is-bad/)
- :apple: [It’s Time We Talk About Student Evaluations of Teaching](https://therenegadecoder.com/teach/its-time-we-talk-about-student-evaluations-of-teaching/)
- :computer: [3 Nasty Bugs in Software Development](https://therenegadecoder.com/code/nasty-bugs-in-software-development/)
- :computer: [Modeling a Simple Relational Database Using CSVs and Python](https://therenegadecoder.com/code/modeling-a-simple-relational-database-using-csvs-and-python/)
- :black_nib: [Yet Another Instance of Misogyny in the Tech Field](https://therenegadecoder.com/blog/yet-another-instance-of-misogyny-in-the-tech-field/)
- :apple: [Top Reasons Why You Don’t Need to Take Attendance (And Why I Do It Anyway)](https://therenegadecoder.com/teach/top-reasons-why-you-dont-need-to-take-attendance-and-why-i-do-it-anyway/)
- :computer: [The Never-ending List of Small Programming Project Ideas](https://therenegadecoder.com/code/the-never-ending-list-of-small-programming-project-ideas/)
- :black_nib: [Why I’m a Certified AI Hater](https://therenegadecoder.com/blog/why-im-a-certified-ai-hater/)
- :computer: [Explain Like I’m Five: Context-Free Grammars](https://therenegadecoder.com/code/explain-like-im-five-context-free-grammars/)
- :black_nib: [The Haters Guide to Python](https://therenegadecoder.com/blog/the-haters-guide-to-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-04-26 using [SnakeMD](https://www.snakemd.io).
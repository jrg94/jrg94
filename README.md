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

- :apple: [Recommended Reading: “To teach in the time of ChatGPT is to know pain” by Scott K. Johnson](https://therenegadecoder.com/teach/recommended-reading-to-teach-in-the-time-of-chatgpt-is-to-know-pain-by-scott-k-johnson/)
- :apple: [Writing Code on Paper Is Good Actually](https://therenegadecoder.com/teach/writing-code-on-paper-is-good-actually/)
- :black_nib: [People Don’t Like to Be Deceived (by AI)](https://therenegadecoder.com/blog/people-dont-like-to-be-deceived-by-ai/)
- :apple: [Generative AI in Education is Pay-to-Lose](https://therenegadecoder.com/teach/generative-ai-in-education-is-pay-to-lose/)
- :black_nib: [My First “I Have a Toddler” Moment](https://therenegadecoder.com/blog/my-first-i-have-a-toddler-moment/)
- :black_nib: [LLMs Got Everyone Sounding the Same Now](https://therenegadecoder.com/blog/llms-got-everyone-sounding-the-same-now/)
- :black_nib: [6v6 Overwatch Is a Joke](https://therenegadecoder.com/blog/6v6-overwatch-is-a-joke/)
- :black_nib: [I Genuinely Don’t Understand Why People Tolerate Hallucinations in AI](https://therenegadecoder.com/blog/i-genuinely-dont-understand-why-people-tolerate-hallucinations-in-ai/)
- :black_nib: [Human Review of AI Output Is Not the Path Forward](https://therenegadecoder.com/blog/human-review-of-ai-output-is-not-the-path-forward/)
- :black_nib: [I Made the Mistake of Visiting the Vibe Coding Subreddit](https://therenegadecoder.com/blog/i-made-the-mistake-of-visiting-the-vibe-coding-subreddit/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-08-21 using [SnakeMD](https://www.snakemd.io).
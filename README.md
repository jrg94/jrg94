# Welcome to My Profile!

This week's code snippet, Longest Common Subsequence in Elixir, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Elixir
defmodule LongestCommonSubsequence do
  def main() do
    lcs = solve(System.argv())
    IO.puts("#{lcs}")
  end

  def solve([as, bs]) when is_bitstring(as) and is_bitstring(bs) do
    lcs(parse_string_to_list_integer(as), parse_string_to_list_integer(bs)) |> Enum.join(", ")
  end

  def solve(_) do
    print_usage()
  end

  def print_usage() do
    ~s(Usage: please provide two lists in the format "1, 2, 3, 4, 5")
  end

  def lcs([], _) do
    []
  end

  def lcs(_, []) do
    []
  end

  def lcs([a | as], [b | bs]) when a == b do
    [a] ++ lcs(as, bs)
  end

  def lcs([a | as], [b | bs]) do
    longest(lcs(as, [b | bs]), lcs([a | as], bs))
  end

  def longest(l1, l2) do
    if Enum.count(l1) > Enum.count(l2) do
      l1
    else
      l2
    end
  end

  def parse_string_to_list_integer(xs) do
    xs
    |> String.trim()
    |> String.split(",")
    |> Enum.map(&String.to_integer(String.trim(&1)))
  end
end

LongestCommonSubsequence.main()
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Is Anyone Else Bothered by How Quickly We Adopted Generative AI?](https://therenegadecoder.com/blog/is-anyone-else-bothered-by-how-quickly-we-adopted-generative-ai/)
- :black_nib: [31 Lessons Learned as a New Dad](https://therenegadecoder.com/blog/31-lessons-learned-as-a-new-dad/)
- :apple: [So You’re Not Sure If Computer Science Is for You](https://therenegadecoder.com/teach/so-youre-not-sure-if-computer-science-is-for-you/)
- :apple: [You Should Give Open-Ended Projects to Your Students](https://therenegadecoder.com/teach/you-should-give-open-ended-projects-to-your-students/)
- :computer: [How to Move Your Extensions Folder in VS Code](https://therenegadecoder.com/code/how-to-move-your-extensions-folder-in-vs-code/)
- :thought_balloon: [Sample Programs Repo Celebrates 1,000 Code Snippets](https://therenegadecoder.com/meta/sample-programs-repo-celebrates-1000-code-snippets/)
- :apple: [Canvas Is Not Built With Educators in Mind](https://therenegadecoder.com/teach/canvas-is-not-built-with-educators-in-mind/)
- :computer: [Workshopping a Tier List Generator](https://therenegadecoder.com/code/workshopping-a-tier-list-generator/)
- :black_nib: [No, The GRE Should Not Be Reinstated](https://therenegadecoder.com/blog/no-the-gre-should-not-be-reinstated/)
- :black_nib: [Summarizing My Dissertation for the Layman](https://therenegadecoder.com/blog/summarizing-my-dissertation-for-the-layman/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-02-14 using [SnakeMD](https://www.snakemd.io).
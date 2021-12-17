# Welcome to My Profile!

This week's code snippet, Hello World in Never, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Never
func print_str(hw[L] -> int) -> int
{
    func __print(hw[L] -> int, i -> int) -> int
    {
        i < L ? { print(hw[i]); __print(hw, i + 1) } : 0
    }
    __print(hw, 0)
}

func main() -> int
{
    let hw = [ 72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33 ] -> int;
    
    print_str(hw)
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :cat: [The Case Against Measuring Work in Hours](https://therenegadecoder.com/blog/the-case-against-measuring-work-in-hours/)
- :dango: [Documenting My Coding Course Upgrades](https://therenegadecoder.com/teach/documenting-my-coding-course-upgrades/)
- :milky_way: [Brainstorming a List of Classes That Ought to Be Taught in Computer Science Curriculum](https://therenegadecoder.com/teach/brainstorming-a-list-of-classes-that-ought-to-be-taught-in-computer-science-curriculum/)
- :notes: [Comparing Java to Python: A Syntax Mapping](https://therenegadecoder.com/code/comparing-java-to-python-a-syntax-mapping/)
- :milky_way: [How to Use Python to Build a Simple Visualization Dashboard Using Plotly](https://therenegadecoder.com/code/how-to-use-python-to-build-a-simple-visualization-dashboard-using-plotly/)
- :dango: [Sharing the Fruits of My Fourth Hackathon](https://therenegadecoder.com/blog/sharing-the-fruits-of-my-fourth-hackathon/)
- :cat: [The Sample Programs READMEs Now Feature Missing Solutions](https://therenegadecoder.com/meta/the-sample-programs-readmes-now-feature-missing-solutions/)
- :door: [Stuck in Your Coding Journey? Try Leveraging Bloom’s Taxonomy](https://therenegadecoder.com/teach/stuck-in-your-coding-journey-try-leveraging-blooms-taxonomy/)
- :gem: [Translations of The Renegade Coder Content](https://therenegadecoder.com/blog/translations-of-the-renegade-coder-content/)
- :door: [Recommended Reading: “Some Final Thoughts on the SAT and ACT” by Jon Boeckenstedt](https://therenegadecoder.com/blog/recommended-reading-some-final-thoughts-on-the-sat-and-act-by-jon-boeckenstedt/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-12-17 using [SnakeMD](https://snakemd.therenegadecoder.com).
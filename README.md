# Welcome to My Profile!

This week's code snippet, Baklava in Verve, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Verve
fn abs(n: Int) -> Int {
    if (n < 0) { -n } else { n }
}

let baklava_str = "          *********************"

fn baklava_line(n: Int) -> String {
    let num_spaces = abs(n)
    let num_stars = 21 - 2 * num_spaces
    substr(baklava_str, 10 - num_spaces, num_spaces + num_stars)
}

fn baklava(start: Int, end: Int) {
    if not(start > end) {
        print(baklava_line(start))
        baklava(start + 1, end)
    }
}

baklava(-10, 10)
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :apple: [I Hate That Student Feedback Is Now Reviewed by Machine Learning](https://therenegadecoder.com/teach/i-hate-that-student-feedback-is-now-reviewed-by-machine-learning/)
- :black_nib: [Not All Code Completion Is Generative AI](https://therenegadecoder.com/blog/not-all-code-completion-is-generative-ai/)
- :black_nib: [AI Haters Stay Winning: What It’s Like to Be Constantly Vindicated](https://therenegadecoder.com/blog/ai-haters-stay-winning-what-its-like-to-be-constantly-vindicated/)
- :black_nib: [Computer Science Career Advice in 2026? Your Guess Is as Good as Mine](https://therenegadecoder.com/blog/computer-science-career-advice-in-2026-your-guess-is-as-good-as-mine/)
- :apple: [Why I Don’t Record My Lectures](https://therenegadecoder.com/teach/why-i-dont-record-my-lectures/)
- :black_nib: [Should You Use Git on Personal Projects No One Will Ever See?](https://therenegadecoder.com/blog/should-you-use-git-on-personal-projects-no-one-will-ever-see/)
- :black_nib: [The Era of Narks Is Upon Us](https://therenegadecoder.com/blog/the-era-of-narks-is-upon-us/)
- :black_nib: [Recapping My First In-Person Academic Conference](https://therenegadecoder.com/blog/recapping-my-first-in-person-academic-conference/)
- :black_nib: [Theseus’s PC: Eight Years of Changes to One Man’s Machine](https://therenegadecoder.com/blog/theseuss-pc-eight-years-of-changes-to-one-mans-machine/)
- :black_nib: [Nobody Wants to Have Kids](https://therenegadecoder.com/blog/nobody-wants-to-have-kids/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2025-12-26 using [SnakeMD](https://www.snakemd.io).
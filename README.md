# Welcome to My Profile!

This week's code snippet, Rot13 in Rust, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Rust
use std::env;

fn rot13(input: String) -> String {
    let mut output = String::new();
    
    for character in input.chars() {
        let offset;

        if character.is_ascii_lowercase() {
            offset = 'a' as u8;
        }
        else if character.is_ascii_uppercase() {
            offset = 'A' as u8;
        }
        else {
            output.push(character);
            continue;
        }
    
        let mut rotated = character as u8;
        rotated -= offset;
        rotated += 13;
        rotated %= 26;
        rotated += offset;
        
        output.push(rotated as char);
    }
    
    return output;
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if (args.len() == 1) {
        println!("Usage: please provide a string to encrypt");
        return;
    }
    
    let input = args[1].to_string();
    if (input.is_empty()) {
        println!("Usage: please provide a string to encrypt");
        return;
    }
    
    let output = rot13(input);
    println!("{}", output);
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [Inside the Mind of an Engineer: How to Make Societal Issues Worse](https://therenegadecoder.com/blog/inside-the-mind-of-an-engineer-how-to-make-societal-issues-worse/)
- :black_nib: [How Attack on Titan Undermines Its Own Message](https://therenegadecoder.com/blog/how-attack-on-titan-undermines-its-own-message/)
- :computer: [Migrating to Poetry 2.x With Some Best Practices](https://therenegadecoder.com/code/migrating-to-poetry-2-x-with-some-best-practices/)
- :black_nib: [Maybe Generative AI Is Just a Symptom of a Broader Problem in Tech](https://therenegadecoder.com/blog/maybe-generative-ai-is-just-a-symptom-of-a-broader-problem-in-tech/)
- :apple: [It’s Time to Collect Mid-Semester Feedback](https://therenegadecoder.com/teach/its-time-to-collect-mid-semester-feedback/)
- :thought_balloon: [2024: Year in Review](https://therenegadecoder.com/meta/2024-year-in-review/)
- :black_nib: [Is Anyone Else Bothered by How Quickly We Adopted Generative AI?](https://therenegadecoder.com/blog/is-anyone-else-bothered-by-how-quickly-we-adopted-generative-ai/)
- :black_nib: [31 Lessons Learned as a New Dad](https://therenegadecoder.com/blog/31-lessons-learned-as-a-new-dad/)
- :apple: [So You’re Not Sure If Computer Science Is for You](https://therenegadecoder.com/teach/so-youre-not-sure-if-computer-science-is-for-you/)
- :apple: [You Should Give Open-Ended Projects to Your Students](https://therenegadecoder.com/teach/you-should-give-open-ended-projects-to-your-students/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-04-13 using [SnakeMD](https://www.snakemd.io).
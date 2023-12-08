# Welcome to My Profile!

This week's code snippet, Quick Sort in Rust, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Rust
fn quicksort_recursive<T: std::cmp::PartialOrd + Clone>(mut vector: Vec<T>) -> Vec<T> {
    match vector.len() {
        0|1 => vector,
        _ => {
            let pivot = vector.pop().unwrap(); // len is always greater than 1 here, so this is safe
            let lesser: Vec<T> = vector.iter().cloned().filter(|i| i.lt(&pivot)).collect();
            let greater: Vec<T> = vector.into_iter().filter(|i| i.ge(&pivot)).collect();
            let mut lesser = quicksort_recursive(lesser);
            lesser.push(pivot);
            lesser.extend(quicksort_recursive(greater).into_iter());
            lesser
        },
    }
}


fn main() {
    let usage_msg = "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\"";

    let mut args = std::env::args();
    args.next(); // first arg is command name, so ignore it

    let input_str = args.next().unwrap_or_else(|| {eprintln!("{usage_msg}"); std::process::exit(-1)});
    let input_vec: Vec<i32> = input_str.split(",") // parse comma separated input into a i32 vector
        .map(|x| x.trim()
            .parse()
            .unwrap_or_else(|_| {eprintln!("{usage_msg}"); std::process::exit(-1)}))
        .collect();

    if input_vec.len() < 2 {
        eprintln!("{usage_msg}");
        std::process::exit(-1);
    }

    println!("{:?}", quicksort_recursive(input_vec));
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [Brainstorming An Algorithm for Shuffling a Queue of Songs](https://therenegadecoder.com/code/brainstorming-an-algorithm-for-shuffling-a-queue-of-songs/)
- :computer: [Trust Me! Your Code Isn’t That Bad](https://therenegadecoder.com/code/trust-me-your-code-isnt-that-bad/)
- :computer: [The Difference Between str() and repr() in Python: A Design by Contract Perspective](https://therenegadecoder.com/code/the-difference-between-str-and-repr-in-python-a-design-by-contract-perspective/)
- :computer: [Obfuscation Techniques: Magic Numbers](https://therenegadecoder.com/code/obfuscation-techniques-magic-numbers/)
- :computer: [Obfuscation Techniques: No More Type Hints](https://therenegadecoder.com/code/obfuscation-techniques-no-more-type-hints/)
- :computer: [Obfuscation Techniques: Visually Similar Characters](https://therenegadecoder.com/code/obfuscation-techniques-visually-similar-characters/)
- :computer: [Obfuscation Techniques: Shadowing Built-in Functions](https://therenegadecoder.com/code/obfuscation-techniques-shadowing-built-in-functions/)
- :computer: [Obfuscation Techniques: Writing Malicious Comments](https://therenegadecoder.com/code/obfuscation-techniques-writing-malicious-comments/)
- :computer: [Obfuscation Techniques: The Yoda Conditional](https://therenegadecoder.com/code/obfuscation-techniques-the-yoda-conditional/)
- :apple: [Students Should Be Able to Build a Portfolio From Their Coursework](https://therenegadecoder.com/teach/students-should-be-able-to-build-a-portfolio-from-their-coursework/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-12-08 using [SnakeMD](https://www.snakemd.io).
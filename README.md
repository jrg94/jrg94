# Welcome to My Profile!

This week's code snippet, Binary Search in Rust, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Rust
#![feature(is_sorted)]

use std::env;

fn binary_search(search_arr: &Vec<i32>, target: &i32) -> Option<usize> {
  let mut low: i8 = 0;
  let mut high: i8 = search_arr.len() as i8 - 1;

  while low <= high {
    let mid = (((high - low) / 2) + low) as usize;
    let val = &search_arr[mid];

    if val == target {
        return Some(mid);
    }

    // If value is < target then search between mid + 1 and high
    if val < target {
        low = mid as i8 + 1;
    }

    // If value is > target then search between low and mid - 1
    if val > target {
        high = mid as i8 - 1;
    }
  }

  return None;
}

fn main() {
  let err_msg = "Usage: please provide a list of sorted integers \"1, 4, 5, 11, 12\" and the integer to find \"11\"";
  let args: Vec<String> = env::args().collect();

  if args.len() < 3 {
    panic!(err_msg);
  }

  let arr: Vec<i32> = args[1].clone()
    .split(",")
    .map(|s| s.trim().parse().expect(err_msg))
    .collect();

  if !arr.is_sorted() {
    panic!(err_msg);
  }
  
  let target = args[2].clone()
    .parse()
    .expect(err_msg);
  
  match binary_search(&arr, &target) {
    Some(_) => println!("true"),
    None => println!("false"),
  }
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :door: [I Finally Figured Out Python’s Module and Package System](https://therenegadecoder.com/code/i-finally-figured-out-pythons-module-and-package-system/)
- :tea: [How to Reason About Your Code With a Tracing Table](https://therenegadecoder.com/code/how-to-reason-about-your-code-with-a-tracing-table/)
- :fu: [How to Automatically Generate Fitbit Access Tokens Using Python](https://therenegadecoder.com/code/how-to-automatically-generate-fitbit-access-tokens-using-python/)
- :dango: [What Value Does Every Cell Contain in a New Integer Array in Java?](https://therenegadecoder.com/code/what-value-does-every-cell-contain-in-a-new-integer-array-in-java/)
- :lock: [True or False: If Variables Are Changed in a Java Method, They Are Also Changed Outside the Method](https://therenegadecoder.com/code/true-or-false-if-variables-are-changed-in-a-java-method-they-are-also-changed-outside-the-method/)
- :gem: [What Value Does X Have at the End of a Loop in Java?](https://therenegadecoder.com/code/what-value-does-x-have-at-the-end-of-a-loop-in-java/)
- :lock: [5 Ways to Write Hello World in Python](https://therenegadecoder.com/code/5-ways-to-write-hello-world-in-python/)
- :fu: [What Makes Multiple Return Statements Bad Practice?](https://therenegadecoder.com/code/what-makes-multiple-return-statements-bad-practice/)
- :dango: [Dump Java: Life Is Just Better in Python](https://therenegadecoder.com/code/dump-java-life-is-just-better-in-python/)
- :exclamation: [The Renegade’s Guide to PC Building: Unveiling Version 2.0](https://therenegadecoder.com/blog/the-renegades-guide-to-pc-building-unveiling-version-2-0/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2022-09-16 using [SnakeMD](https://www.snakemd.io).
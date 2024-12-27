# Welcome to My Profile!

This week's code snippet, Merge Sort in Javascript, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Javascript
function mergeSort (unsortedArray) {
  if (unsortedArray.length <= 1) {
    return unsortedArray;
  }
  const middle = Math.floor(unsortedArray.length / 2);
  const left = unsortedArray.slice(0, middle);
  const right = unsortedArray.slice(middle);
  return merge(
    mergeSort(left), mergeSort(right)
  );
}

function merge (left, right) {
  let resultArray = [], leftIndex = 0, rightIndex = 0;
  while (leftIndex < left.length && rightIndex < right.length) {
    if (left[leftIndex] < right[rightIndex]) {
      resultArray.push(left[leftIndex]);
      leftIndex++;
    } else {
      resultArray.push(right[rightIndex]);
      rightIndex++;
    }
  }
  return resultArray
          .concat(left.slice(leftIndex))
          .concat(right.slice(rightIndex));
}

const main = (input) => {
    const inputValidation = /^"?(\d+,\s*){2,}\d+(,"?|"?)$/gm;
    if (inputValidation.test(input) == true) {
        let arr;
        arr = input.replace(/(\s|"|'|`)/g, '');
        arr = arr.split(',');
        arr = arr.map(function (n) {
            return parseInt(n, 10);
        });
        arr = arr.filter(n => n);
        arr=mergeSort(arr);
        console.log(arr);
    }
    else {
        console.log(usage);
    }
}

const usage = `Usage: please provide a list of at least two integers to sort in the format "1, 2, 3, 4, 5"`;

if (process.argv.length > 2) {
    const input = process.argv[2];
    main(input);
}
else {
    console.log(usage);
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [Workshopping a Tier List Generator](https://therenegadecoder.com/code/workshopping-a-tier-list-generator/)
- :black_nib: [No, The GRE Should Not Be Reinstated](https://therenegadecoder.com/blog/no-the-gre-should-not-be-reinstated/)
- :black_nib: [Summarizing My Dissertation for the Layman](https://therenegadecoder.com/blog/summarizing-my-dissertation-for-the-layman/)
- :black_nib: [9 Things I Wish I Knew About Doctoral Programs](https://therenegadecoder.com/blog/things-i-wish-i-knew-about-doctoral-programs/)
- :black_nib: [I Successfully Completed My PhD in Engineering Education](https://therenegadecoder.com/blog/i-successfully-completed-my-phd-in-engineering-education/)
- :apple: [So You Want to Be a University Educator](https://therenegadecoder.com/teach/so-you-want-to-be-a-university-educator/)
- :black_nib: [Looking Forward to the Future](https://therenegadecoder.com/blog/looking-forward-to-the-future/)
- :computer: [Unpacking the Jargon Around Compilers, Interpreters, and More](https://therenegadecoder.com/code/unpacking-the-jargon-around-compilers-interpreters-and-more/)
- :computer: [What Are Type Hints in Python?](https://therenegadecoder.com/code/what-are-type-hints-in-python/)
- :computer: [The Problem Enums Are Intended to Solve](https://therenegadecoder.com/code/the-problem-enums-are-intended-to-solve/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-12-27 using [SnakeMD](https://www.snakemd.io).
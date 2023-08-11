# Welcome to My Profile!

This week's code snippet, Quick Sort in Bash, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Bash
#!/bin/bash

# based on https://stackoverflow.com/questions/7442417/how-to-sort-an-array-in-bash

# quicksorts positional arguments
# return is in array qsort_ret
# Note: iterative, NOT recursive! :)
# First argument is a function name that takes two arguments and compares them
qsort_iter() {
   (($#<=1)) && return 0
   local compare_fun=$1
   shift
   local stack=( 0 $(($#-1)) ) beg end i pivot smaller larger
   qsort_ret=("$@")
   while ((${#stack[@]})); do
      beg=${stack[0]}
      end=${stack[1]}
      stack=( "${stack[@]:2}" )
      smaller=() larger=()
      pivot=${qsort_ret[beg]}
      for ((i=beg+1;i<=end;++i)); do
         if "$compare_fun" "${qsort_ret[i]}" "$pivot"; then
            smaller+=( "${qsort_ret[i]}" )
         else
            larger+=( "${qsort_ret[i]}" )
         fi
      done
      qsort_ret=( "${qsort_ret[@]:0:beg}" "${smaller[@]}" "$pivot" "${larger[@]}" "${qsort_ret[@]:end+1}" )
      if ((${#smaller[@]}>=2)); then stack+=( "$beg" "$((beg+${#smaller[@]}-1))" ); fi
      if ((${#larger[@]}>=2)); then stack+=( "$((end-${#larger[@]}+1))" "$end" ); fi
   done
}

# compare function
compare_str() { [[ $1 < $2 ]]; }

ERROR="Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""

#Validation to fit criteria
if [ "$#" != "1" ]; then echo $ERROR; exit 1; fi; #wrong input
if [[ ! "$1" =~ "," ]]; then echo $ERROR; exit 1; fi; #wrong format

array=($(echo $@ | tr ", " " "))

if [ "${array[0]}" == "" ]; then echo $ERROR; exit 1; fi; #empty input
if [ "${#array[@]}" == "1" ]; then echo $ERROR; exit 1; fi; #not a list

qsort_iter compare_str "${array[@]}"
arrayString=${qsort_ret[@]}
echo "${arrayString// /, }"

exit 0
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [I Am Officially a Lecturer](https://therenegadecoder.com/blog/i-am-officially-a-lecturer/)
- :black_nib: [CampusParc Has Got to Go](https://therenegadecoder.com/blog/campusparc-has-got-to-go/)
- :black_nib: [Explain Like I’m Five: Computer Programming](https://therenegadecoder.com/blog/explain-like-im-five-computer-programming/)
- :computer: [Abusing Python’s Operator Overloading Feature](https://therenegadecoder.com/code/abusing-pythons-operator-overloading-feature/)
- :computer: [5 Absurd Ways to Add Two Numbers in Python](https://therenegadecoder.com/code/5-absurd-ways-to-add-two-numbers-in-python/)
- :black_nib: [What It Takes to Throw a Celebration of Life](https://therenegadecoder.com/blog/what-it-takes-to-throw-a-celebration-of-life/)
- :black_nib: [Using Ethnography to Advocate for Student Needs in Computer Science Education](https://therenegadecoder.com/blog/using-ethnography-to-advocate-for-student-needs-in-computer-science-education/)
- :computer: [3 Key Programming Best Practices for Beginners](https://therenegadecoder.com/code/programming-best-practices-for-beginners/)
- :black_nib: [What Restoring a 20-Year-Old Deck Looks Like](https://therenegadecoder.com/blog/what-refreshing-a-20-year-old-deck-looks-like/)
- :black_nib: [Java Has A Remainder Operator—Not a Mod Operator](https://therenegadecoder.com/blog/java-has-a-remainder-operator-not-a-mod-operator/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-08-11 using [SnakeMD](https://www.snakemd.io).
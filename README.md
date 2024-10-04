# Welcome to My Profile!

This week's code snippet, Prime Number in R, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```R
# Program to check if the input number is prime or not
args<-commandArgs(TRUE)
if(length(args) > 0){
  a1 = args[1]
  # Check Numeral only, ..
  numbers_only <- function(a) !grepl("\\D", a1)
  if(numbers_only(a1) == TRUE){
    if (a1 >= 0){
      a = as.integer(a1)
    if(a == 2){
      cat("Prime")
      # If 0, or 1 or Even Number
    }else if (a == 0 || a == 1 || a %% 2 == 0 ) {
      cat("Composite")
    }else{
      flag = 1
      r = a %/% 2
      for(i in 2:r) {
        if (a %% i == 0) {
           flag = 0
          break
          }
       }
       if(flag == 1) {
         cat("Prime")
        } else {
          cat("Composite")
        }
    }
  }else{# Empty Input
  cat("Usage: please input a non-negative integer")
}
}else{  # Negative Input
  cat("Usage: please input a non-negative integer")
}
}else{    # Empty Input
  cat("Usage: please input a non-negative integer")
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :computer: [What Is a Function in Python?](https://therenegadecoder.com/code/what-is-a-function-in-python/)
- :computer: [What Is Operator Overloading in Python?](https://therenegadecoder.com/code/what-is-operator-overloading-in-python/)
- :computer: [What Is the Assignment Operator in Python?](https://therenegadecoder.com/code/what-is-the-assignment-operator-in-python/)
- :apple: [As a Student, You Are a Lab Rat](https://therenegadecoder.com/teach/as-a-student-you-are-a-lab-rat/)
- :computer: [What Is an Expression in Python?](https://therenegadecoder.com/code/what-is-an-expression-in-python/)
- :computer: [What Is a Variable in Python?](https://therenegadecoder.com/code/what-is-a-variable-in-python/)
- :black_nib: [A Preview of My Last Semester As a PhD Student](https://therenegadecoder.com/blog/a-preview-of-my-last-semester-as-a-phd-student/)
- :computer: [What Is a Condition in Python?](https://therenegadecoder.com/code/what-is-a-condition-in-python/)
- :computer: [What Is a Loop in Python?](https://therenegadecoder.com/code/what-is-a-loop-in-python/)
- :computer: [What Is a Constructor in Python?](https://therenegadecoder.com/code/what-is-a-constructor-in-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2024-10-04 using [SnakeMD](https://www.snakemd.io).
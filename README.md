# Welcome to My Profile!

This week's code snippet, File Input Output in R, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```R
file_create_result = tryCatch({
#Open and write 2 lines to the file.
  fileConn<-file("output.txt")
  writeLines(c("Hello","World\n"), fileConn)
  writeLines(c("Writing this file using R"), fileConn)
  close(fileConn)
},
 warning = function( w )
  {
     cat("Warning while opening the file")
  },
   error = function( w )
  {
     cat("Error while opening the file")
  }
)
# Catch File Open Error
if(file.exists("output.txt")){
  f_open = readLines("output.txt")
  singleString <- paste(readLines("output.txt"), collapse=" ")
  cat(singleString)
} else{
  cat("File doesn't exist")
}
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :milky_way: [The Renegade Coder Is Taking a Little Break](https://therenegadecoder.com/meta/the-renegade-coder-is-taking-a-little-break/)
- :gem: [Why Is Adding Two Random Numbers Not the Same as Generating One in the Same Range?](https://therenegadecoder.com/code/why-is-adding-two-random-numbers-not-the-same-as-generating-one-in-the-same-range/)
- :door: [Design by Contract Hinges on Implication](https://therenegadecoder.com/code/design-by-contract-hinges-on-implication/)
- :seedling: [Maybe It’s Not Okay to Test Private Methods—at Least When Using Design by Contract](https://therenegadecoder.com/code/maybe-its-not-okay-to-test-private-methods-at-least-when-using-design-by-contract/)
- :notes: [29 Things I’d Only Say If I Were Kidnapped](https://therenegadecoder.com/blog/29-things-id-only-say-if-i-were-kidnapped/)
- :cat: [Why Does == Sometimes Work on Strings in Java?](https://therenegadecoder.com/code/why-does-double-equals-sometimes-work-on-strings-in-java/)
- :exclamation: [2022: Year in Review](https://therenegadecoder.com/meta/2022-year-in-review/)
- :dango: [Reflecting on My 8th Semester of Teaching: Autumn 2022](https://therenegadecoder.com/blog/reflecting-on-my-8th-semester-of-teaching-autumn-2022/)
- :milky_way: [There Has to Be a Better Way: Reflecting on My Automation Catchphrase](https://therenegadecoder.com/blog/there-has-to-be-a-better-way-reflecting-on-my-automation-catchphrase/)
- :seedling: [I Am a PhD Candidate!](https://therenegadecoder.com/blog/i-am-a-phd-candidate/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2023-04-07 using [SnakeMD](https://www.snakemd.io).
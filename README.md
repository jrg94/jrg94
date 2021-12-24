# Welcome to My Profile!

This week's code snippet, Even Odd in Fortran, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Fortran
! In program name, - is not allowed
program evenodd
character(len=10) :: argument
Character(26) :: low = 'abcdefghijklmnopqrstuvwxyz'
Character(26) :: cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
integer :: number, check_capital_letters, check_small_letters, remainder 
! Anything not equal to single argument, Print Error
IF(COMMAND_ARGUMENT_COUNT().NE.1)THEN
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
ENDIF

CALL GET_COMMAND_ARGUMENT(1,argument)
if (argument == "") then
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
endif
! Scan for letters
check_capital_letters = scan(argument, cap)
check_small_letters = scan(argument, low)
! If capital letters exist, print error
if (check_capital_letters > 0) then
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
endif
! If small letters exist, print error
if (check_small_letters > 0) then
  write(*,'(g0.8)')"Usage: please input a number"
  STOP
endif
! read the cmd line arg into number
read (argument, '(I10)') number
! get the remainder
remainder = modulo(number, 2)
if (remainder == 0) then
  write(*,'(g0.8)') "Even"
else
  write(*,'(g0.8)') "Odd"
end if
end program
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :dango: [Write a Python Script to Autogenerate Google Form Responses](https://therenegadecoder.com/code/write-a-python-script-to-autogenerate-google-form-responses/)
- :dango: [The Case Against Measuring Work in Hours](https://therenegadecoder.com/blog/the-case-against-measuring-work-in-hours/)
- :gem: [Documenting My Coding Course Upgrades](https://therenegadecoder.com/teach/documenting-my-coding-course-upgrades/)
- :notes: [Brainstorming a List of Classes That Ought to Be Taught in Computer Science Curriculum](https://therenegadecoder.com/teach/brainstorming-a-list-of-classes-that-ought-to-be-taught-in-computer-science-curriculum/)
- :door: [Comparing Java to Python: A Syntax Mapping](https://therenegadecoder.com/code/comparing-java-to-python-a-syntax-mapping/)
- :cat: [How to Use Python to Build a Simple Visualization Dashboard Using Plotly](https://therenegadecoder.com/code/how-to-use-python-to-build-a-simple-visualization-dashboard-using-plotly/)
- :lock: [Sharing the Fruits of My Fourth Hackathon](https://therenegadecoder.com/blog/sharing-the-fruits-of-my-fourth-hackathon/)
- :tea: [The Sample Programs READMEs Now Feature Missing Solutions](https://therenegadecoder.com/meta/the-sample-programs-readmes-now-feature-missing-solutions/)
- :exclamation: [Stuck in Your Coding Journey? Try Leveraging Bloom’s Taxonomy](https://therenegadecoder.com/teach/stuck-in-your-coding-journey-try-leveraging-blooms-taxonomy/)
- :lock: [Translations of The Renegade Coder Content](https://therenegadecoder.com/blog/translations-of-the-renegade-coder-content/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-12-24 using [SnakeMD](https://snakemd.therenegadecoder.com).
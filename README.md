# Welcome to My Profile!

This week's code snippet, Capitalize in Lisp, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Lisp
;;Taken from the Common Lisp Cookbook Project (strings page)
(defun split-string (string)
    (loop for i = 0 then (1+ j)
          as j = (position #\Space string :start i)
          collect (subseq string i j)
          while j))

(defun join-string (lst)
  (when lst
    (concatenate 'string (car lst) " " (join-string (cdr lst)))))

 (defun capitalize (str)
   (concatenate 'string
     (string-upcase (subseq str 0 1)) (subseq str 1)))

(defparameter input (split-string (cadr *posix-argv*)))
(cond
  ((= (length (car input)) 0) (write-line "Usage: please provide a string"))
  (t (write-line (join-string (cons (capitalize (car input)) (cdr input))))))
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :dango: [Translations of The Renegade Coder Content](https://therenegadecoder.com/blog/translations-of-the-renegade-coder-content/)
- :tea: [Recommended Reading: “Some Final Thoughts on the SAT and ACT” by Jon Boeckenstedt](https://therenegadecoder.com/blog/recommended-reading-some-final-thoughts-on-the-sat-and-act-by-jon-boeckenstedt/)
- :tea: [Support The Sample Programs Repo This Hacktoberfest](https://therenegadecoder.com/meta/support-the-sample-programs-repo-this-hacktoberfest/)
- :cat: [Programmatically Explore Code Snippets of Many Languages Using Python](https://therenegadecoder.com/code/programmatically-explore-code-snippets-of-many-languages-using-python/)
- :tea: [How to Generate Markdown in Python Using SnakeMD](https://therenegadecoder.com/code/how-to-generate-markdown-in-python-using-snakemd/)
- :gem: [I Passed My Qualifying Exam!](https://therenegadecoder.com/blog/i-passed-my-qualifying-exam/)
- :milky_way: [How to Automate Your GitHub Profile](https://therenegadecoder.com/code/how-to-automate-your-github-profile/)
- :cat: [Practice Your Coding Skills With the Sample Programs Template](https://therenegadecoder.com/meta/practice-your-coding-skills-with-the-sample-programs-template/)
- :fu: [Sample Programs Docs Generator 2.3.0 Features How To Python README Automation](https://therenegadecoder.com/meta/sample-programs-docs-generator-2-3-0-features-how-to-python-readme-automation/)
- :cat: [Making a Discord Bot Roll a Die in Python](https://therenegadecoder.com/code/making-a-discord-bot-roll-a-die-in-python/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-10-22 using [SnakeMD](https://snakemd.therenegadecoder.com).
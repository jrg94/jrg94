# Welcome to My Profile!

This week's code snippet, Quick Sort in Lisp, is brought to you by [Subete](https://subete.therenegadecoder.com/en/latest/) and the [Sample Programs repo](https://sample-programs.therenegadecoder.com/).

```Lisp
(defun qsort (L)
  (cond
    ((null L) nil)
    (t
      (append
        (qsort (list< (car L) (cdr L)))
        (cons (car L) nil) 
        (qsort (list>= (car L) (cdr L)))))))

(defun list< (a b)
  (cond
    ((or (null a) (null b)) nil)
    ((< a (car b)) (list< a (cdr b)))
    (t (cons (car b) (list< a (cdr b))))))

(defun list>= (a b)
  (cond
    ((or (null a) (null b)) nil)
    ((>= a (car b)) (list>= a (cdr b)))
    (t (cons (car b) (list>= a (cdr b))))))

;;Taken from the Common Lisp Cookbook Project (strings page)
(defun split-string (string)
    (loop for i = 0 then (1+ j)
          as j = (position #\, string :start i)
          collect (subseq string i j)
          while j))

(defun join-string (lst)
  (reduce
    (lambda (acc n)
      (concatenate 'string acc ", " (princ-to-string n))) (cdr lst)
        :initial-value (princ-to-string (car lst))))

(defun maybe-int (input)
  (cond
    ((null input) nil)
    ((string= input "") nil)
    ((every #'digit-char-p (string-left-trim "-" input)) (parse-integer input))
    (t nil)))

(defun maybe-int-list (input-list &optional (acc))
  (cond
    ((<= (length input-list) 0) acc)
    (t
      (let ((i (maybe-int (string-trim " " (car input-list)))))
        (cond
          ((null i) nil)
          (t (maybe-int-list (cdr input-list) (cons i acc))))))))


(defparameter input (maybe-int-list (split-string (cadr *posix-argv*))))
(cond
  ((or (null input) (= (length input) 1)) (write-line "Usage: please provide a list of at least two integers to sort in the format \"1, 2, 3, 4, 5\""))
  (t (write-line (join-string (qsort input)))))
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com).

- :exclamation: [Breaking Down a Hello World Discord Bot in Python](https://therenegadecoder.com/code/breaking-down-a-hello-world-discord-bot-in-python/)
- :gem: [Chiropractors Have Broken My YouTube Recommendations](https://therenegadecoder.com/blog/chiropractors-have-broken-my-youtube-recommendations/)
- :lock: [Introduction to Python Coding With Discord Bots](https://therenegadecoder.com/code/introduction-to-python-coding-with-discord-bots/)
- :gem: [Write-Only Discord Bots Are Surprisingly Easy to Code in Python](https://therenegadecoder.com/code/write-only-discord-bots-are-surprisingly-easy-to-code-in-python/)
- :seedling: [Sample Programs Docs Generator 2.0.3 Features README Automation](https://therenegadecoder.com/meta/sample-programs-docs-generator-2-0-3-features-readme-automation/)
- :door: [Visualizing My 2020 Hum Driving History Using Python](https://therenegadecoder.com/code/visualizing-my-2020-hum-driving-history-using-python/)
- :notes: [Python Basics: Everything You Need to Know to Get Started](https://therenegadecoder.com/code/python-basics-everything-you-need-to-know-to-get-started/)
- :door: [Revising The Renegade Coder 2021 Roadmap](https://therenegadecoder.com/meta/revising-the-renegade-coder-2021-roadmap/)
- :fu: [How to Make a Choice in Your Python Program](https://therenegadecoder.com/code/how-to-make-a-choice-in-your-python-program/)
- :seedling: [Teaching Computers to Open Jars: How to Get a Jar](https://therenegadecoder.com/blog/teaching-computers-to-open-jars-how-to-get-a-jar/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://newsletter.therenegadecoder.com/)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2021-08-09 using [SnakeMD](https://snakemd.therenegadecoder.com).
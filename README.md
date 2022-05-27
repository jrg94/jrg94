# Welcome to My Profile!

This week's code snippet, Quick Sort in Lisp, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

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

- :notes: [The Sample Programs Website Is Fully Automated](https://therenegadecoder.com/meta/the-sample-programs-website-is-fully-automated/)
- :door: [3 Things Software Developers Don’t Need to Know](https://therenegadecoder.com/teach/3-things-software-developers-dont-need-to-know/)
- :fu: [The Complete Guide to SnakeMD: A Python Library for Generating Markdown](https://therenegadecoder.com/code/the-complete-guide-to-snakemd-a-python-library-for-generating-markdown/)
- :door: [The Complete Guide to Subete: A Python Library for Browsing Code Snippets](https://therenegadecoder.com/code/the-complete-guide-to-subete-a-python-library-for-browsing-code-snippets/)
- :door: [Stop Using Flags to Control Your Loops](https://therenegadecoder.com/code/stop-using-flags-to-control-your-loops/)
- :milky_way: [Celebrating 500 Articles on The Renegade Coder](https://therenegadecoder.com/meta/celebrating-500-articles-on-the-renegade-coder/)
- :fu: [The Great Subdomain Purge: Sample Programs Has a New Home](https://therenegadecoder.com/meta/the-great-subdomain-purge-sample-programs-has-a-new-home/)
- :notes: [Meet Pymon: A Discord Bot That Can Answer Any Question You Want](https://therenegadecoder.com/teach/meet-pymon-a-discord-bot-that-can-answer-any-question-you-want/)
- :exclamation: [How to Generate Any Random Number From a Zero to One Range](https://therenegadecoder.com/code/how-to-generate-any-random-number-from-a-zero-to-one-range/)
- :lock: [ULPT: How to Cheat on Programming Assignments and Get Away With It](https://therenegadecoder.com/teach/ulpt-how-to-cheat-on-programming-assignments-and-get-away-with-it/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

---

This document was automatically rendered on 2022-05-27 using [SnakeMD](https://snakemd.therenegadecoder.com).
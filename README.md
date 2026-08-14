# Welcome to My Profile!

This week's code snippet, Fraction Math in Ocaml, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Ocaml
let ( let* ) = Option.bind

module Rational : sig
  type rat

  val make : int -> int -> rat
  val rat_of_string_opt : string -> rat option
  val string_of_rat : rat -> string
  val recip : rat -> rat
  val mult : rat -> rat -> rat
  val div : rat -> rat -> rat
  val add : rat -> rat -> rat
  val sub : rat -> rat -> rat
  val eq : rat -> rat -> bool
  val neq : rat -> rat -> bool
  val gt : rat -> rat -> bool
  val lt : rat -> rat -> bool
  val gte : rat -> rat -> bool
  val lte : rat -> rat -> bool
end = struct
  type rat = { num : int; denom : int }

  let gcd a b =
    let a = abs a in
    let b = abs b in
    if b = 0 then a
    else
      let rec aux a b =
        let r = a mod b in
        if r = 0 then b else aux b r
      in
      aux a b

  let make num denom =
    if denom = 0 then raise Division_by_zero
    else
      let divisor = gcd num denom in
      let sign_flip = if denom < 0 then -1 else 1 in
      { num = num / divisor * sign_flip; denom = denom / divisor * sign_flip }

  let rat_of_string_opt s =
    match String.split_on_char '/' s with
    | [ num; denom ] ->
        let* num_int = int_of_string_opt num in
        let* denom_int = int_of_string_opt denom in
        if denom_int <> 0 then Some (make num_int denom_int) else None
    | _ -> None

  let string_of_rat { num; denom } =
    string_of_int num ^ "/" ^ string_of_int denom

  let recip { num; denom } = make denom num
  let mult a b = make (a.num * b.num) (a.denom * b.denom)
  let div a b = mult a (recip b)
  let add a b = make ((a.num * b.denom) + (b.num * a.denom)) (a.denom * b.denom)
  let sub a b = add a (make (-b.num) b.denom)
  let eq a b = a = b
  let neq a b = not (eq a b)
  let gt a b = a.num * b.denom > b.num * a.denom
  let gte a b = gt a b || eq a b
  let lt a b = not (gte a b)
  let lte a b = lt a b || eq a b
end

module StringMap = Map.Make (String)

type frac_op =
  | Arith of (Rational.rat -> Rational.rat -> Rational.rat)
  | Bool of (Rational.rat -> Rational.rat -> bool)

let ops =
  let open Rational in
  StringMap.of_list
    [
      ("*", Arith mult);
      ("/", Arith div);
      ("+", Arith add);
      ("-", Arith sub);
      ("==", Bool eq);
      ("!=", Bool neq);
      (">", Bool gt);
      ("<", Bool lt);
      (">=", Bool gte);
      ("<=", Bool lte);
    ]

let exec_exp a op b =
  match op with
  | Arith f -> f a b |> Rational.string_of_rat
  | Bool f -> if f a b then "1" else "0"

let parse_args = function
  | [| _; a; op_s; b |] ->
      let* op_f = StringMap.find_opt op_s ops in
      let* a_rat = Rational.rat_of_string_opt a in
      let* b_rat = Rational.rat_of_string_opt b in
      Some (a_rat, op_f, b_rat)
  | _ -> None

let () =
  print_endline
  @@
  match parse_args Sys.argv with
  | Some (a, op, b) -> exec_exp a op b
  | _ -> "Usage: ./fraction-math operand1 operator operand2"
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :apple: [Writing Code on Paper Is Good Actually](https://therenegadecoder.com/teach/writing-code-on-paper-is-good-actually/)
- :black_nib: [People Don’t Like to Be Deceived (by AI)](https://therenegadecoder.com/blog/people-dont-like-to-be-deceived-by-ai/)
- :apple: [Generative AI in Education is Pay-to-Lose](https://therenegadecoder.com/teach/generative-ai-in-education-is-pay-to-lose/)
- :black_nib: [My First “I Have a Toddler” Moment](https://therenegadecoder.com/blog/my-first-i-have-a-toddler-moment/)
- :black_nib: [LLMs Got Everyone Sounding the Same Now](https://therenegadecoder.com/blog/llms-got-everyone-sounding-the-same-now/)
- :black_nib: [6v6 Overwatch Is a Joke](https://therenegadecoder.com/blog/6v6-overwatch-is-a-joke/)
- :black_nib: [I Genuinely Don’t Understand Why People Tolerate Hallucinations in AI](https://therenegadecoder.com/blog/i-genuinely-dont-understand-why-people-tolerate-hallucinations-in-ai/)
- :black_nib: [Human Review of AI Output Is Not the Path Forward](https://therenegadecoder.com/blog/human-review-of-ai-output-is-not-the-path-forward/)
- :black_nib: [I Made the Mistake of Visiting the Vibe Coding Subreddit](https://therenegadecoder.com/blog/i-made-the-mistake-of-visiting-the-vibe-coding-subreddit/)
- :black_nib: [You’ve Fallen for the Red/Blue Button Trap](https://therenegadecoder.com/blog/youve-fallen-for-the-red-blue-button-trap/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-08-14 using [SnakeMD](https://www.snakemd.io).
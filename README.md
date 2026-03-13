# Welcome to My Profile!

This week's code snippet, Base64 Encode Decode in Pascal, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```Pascal
program Base64EncodeDecode;

{$mode objfpc}{$H+}

uses
   base64,
   Classes,
   SysUtils;

procedure Usage;
begin
   Writeln('Usage: please provide a mode and a string to encode/decode');
   Halt(1);
end;

function IsBase64Char(c: char): boolean;
begin
   Result := (c in ['A'..'Z', 'a'..'z', '0'..'9', '+', '/', '=']);
end;

function IsValidBase64(const s: string): boolean;
var
   i, L, padCount, firstPadPos: integer;
begin
   L := Length(s);

   if (L = 0) or (L mod 4 <> 0) then
      Exit(False);

   for i := 1 to L do
      if not IsBase64Char(s[i]) then
         Exit(False);

   padCount := 0;
   for i := L downto 1 do
      if s[i] = '=' then
         Inc(padCount)
      else
         Break;

   if padCount > 2 then
      Exit(False);

   firstPadPos := Pos('=', s);
   if (firstPadPos > 0) and (firstPadPos <= L - padCount) then
      Exit(False);

   Result := True;
end;

var
   mode, textarg, outstr: string;
begin
   if ParamCount <> 2 then
      Usage;

   mode := LowerCase(ParamStr(1));
   textarg := ParamStr(2);

   if textarg = '' then
      Usage;

   if mode = 'encode' then
   begin
      outstr := EncodeStringBase64(textarg);
      Writeln(outstr);
   end
   else if (mode = 'decode') then
   begin
      if not IsValidBase64(textarg) then
         Usage;

      outstr := DecodeStringBase64(textarg);
      if outstr = '' then
         Usage;

      Writeln(outstr);
   end
   else
      Usage;
end.
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [What It Feels Like to Be a Toddler Again: Learning a Language](https://therenegadecoder.com/blog/what-it-feels-like-to-be-a-toddler-again-learning-a-language/)
- :black_nib: [Things I Don’t Want AI To Help Me With](https://therenegadecoder.com/blog/things-i-dont-want-ai-to-help-me-with/)
- :black_nib: [Why I Rebel Against the Use of Generative AI](https://therenegadecoder.com/blog/why-i-rebel-against-the-use-of-generative-ai/)
- :black_nib: [Buying a House Sucks](https://therenegadecoder.com/blog/buying-a-house-sucks/)
- :black_nib: [Smug Yet Unserious](https://therenegadecoder.com/blog/smug-yet-unserious/)
- :black_nib: [32 College Stories That Always Make Friends Laugh](https://therenegadecoder.com/blog/32-college-stories-that-always-make-friends-laugh/)
- :computer: [Why Does == Sometimes Work on Integer Objects in Java?](https://therenegadecoder.com/code/why-does-sometimes-work-on-integer-objects-in-java/)
- :apple: [Online Exams Might Be Cooked](https://therenegadecoder.com/teach/online-exams-might-be-cooked/)
- :apple: [Encouraging Attendance With Peer Instruction](https://therenegadecoder.com/teach/encouraging-attendance-with-peer-instruction/)
- :black_nib: [Conspiracy Theory: All Pro Sports Are Rigged Now](https://therenegadecoder.com/blog/conspiracy-theory-all-pro-sports-are-rigged-now/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [YouTube](https://www.youtube.com/@TheRenegadeCoder)

[![An image of @jrg94's Holopin badges, which is a link to view their full Holopin profile](https://holopin.me/jrg94)](https://holopin.io/@jrg94)

***

This document was automatically rendered on 2026-03-13 using [SnakeMD](https://www.snakemd.io).
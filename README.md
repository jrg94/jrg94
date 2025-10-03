# Welcome to My Profile!

This week's code snippet, Reverse String in X86 64, is brought to you by [Subete](https://subete.jeremygrifski.com/en/latest/) and the [Sample Programs repo](https://sampleprograms.io/).

```X86 64
;I/0
%DEFINE SYS_WRITE 1
%DEFINE STDOUT 1

;Memory
%DEFINE SYS_MMAP 9
;PROTS (RDX)
%DEFINE PROT_READ 0x01
%DEFINE PROT_WRITE 0x02
;FLAGS (R10)
%DEFINE MAP_PRIVATE 0x02
%DEFINE MAP_ANONYMOUS 0x20

%DEFINE SYS_MUNMAP 11


;Process
%DEFINE SYS_EXIT 60

section .data
 
section .text


global strlen
strlen:
; ----------------------------------------------------------------------------
; Function: strlen
; Description:
;   Finds the length of the string. Will count until it hits a zero byte. Could be vectorized or optimized in another way but will be left this way for simplicity.
; Parameters:
;   RDI - (char*)         String pointer.
;   RSI - ()              Unused.
;   RDX - ()              Unused.
;   R10 - ()              Unused.
;   R8  - ()              Unused.
;   R9  - ()              Unused.
; Returns:
;   RAX - (int)           String length.
; ----------------------------------------------------------------------------
    
    MOV RCX, 0 ;RCX will be our counter.

    .loop:
        CMP BYTE [RDI+RCX], 0 ;Compare character to zero
        JE .done
        INC RCX ;Doesn't disturb any flags
        JNZ .loop ;Short jump back to the .loop label
    .done:
    MOV RAX, RCX
    RET
    
global reverseString
reverseString:
; ----------------------------------------------------------------------------
; Function: strlen
; Description:
;   Reverses a string and returns the pointer to it. Could be vectorized or optimized another way but will be left this way for simplicity.
; Parameters:
;   RDI - (char*)         String pointer.
;   RSI - (int)           String length.
;   RDX - ()              Unused.
;   R10 - ()              Unused.
;   R8  - ()              Unused.
;   R9  - ()              Unused.
; Returns:
;   RAX - (char*)         Pointer to reversed string.
; ----------------------------------------------------------------------------  
    %DEFINE reverseString.STACK_INIT 16
    PUSH RBP
    MOV RBP, RSP
    SUB RSP, reverseString.STACK_INIT
    
    MOV [RBP-8], RDI ;Move the string pointer to the stack.  
    MOV [RBP-16], RSI ;Move the string length to the stack.  
    
    MOV RAX, SYS_MMAP
    MOV RDI, 0 ;Let the OS decide which address to use.
    ;RSI will hold how many bytes to allocate, but that's already initialized so we won't add it.
    MOV RDX, PROT_WRITE | PROT_READ ;We'll allow the memory to be read and written to.
    MOV R10, MAP_PRIVATE | MAP_ANONYMOUS ;We won't allow other processes to touch this memory, and it will not be associated with a file.
    MOV R8, 0 ;No file descriptor.
    MOV R9, 0 ;No offset.
    SYSCALL
    MOV RBX, RAX ;RBX (base register) will hold the start of our new string for later.
    MOV RDI, RAX ;RDI (destination register) will hold our new string pointer.
    ;Add string length to RDI and then subrtract by one so we can start at end of address.
    ADD RDI, [RBP-16]
    DEC RDI
    MOV RSI, [RBP-8] ;RSI (source register) will hold the old string address.
    MOV RCX, 0 ;RCX (counter register) will hold the loop counter.
    .loop:
        MOV AL, [RSI+RCX] ;Move char from location RSI+RCX to AL.
        MOV [RDI], AL ;Move char from AL to location pointer to at RDI+RCX.
        DEC RDI ;Move pointer foward by one byte.
        INC RCX ;Move counter forward by one.
        CMP RCX, [RBP-16] ;Check if RCX hasn't hit the pointer at RSI yet.
        JL .loop
   
    MOV RAX, RBX ;Move our new string into RAX
    ADD RSP, reverseString.STACK_INIT
    MOV RSP, RBP
    POP RBP
    RET

global _start
_start:
    %DEFINE _start.STACK_INIT 16 ;Defining this so we aren't placing a literal every time we need to empty the stack at the end.
    ;Setting up stack frame. Prolog.
    PUSH RBP
    MOV RBP, RSP
    ;Allocating space on the stack for variables
    SUB RSP, _start.STACK_INIT ;16 bytes allocated
    MOV QWORD [RBP-8], 0 ;Length of text, 8 bytes.
    MOV QWORD [RBP-16], 0 ;New String PTR, 8 bytes.
    ;Jump to sections based on argc
    CMP QWORD [RBP+8], 1
    JE noInput
    CMP QWORD [RBP+8], 2
    JE input
    
    noInput:
        ;Epilog
        ADD RSP, _start.STACK_INIT
        MOV RSP, RBP
        POP RBP

        ;Exit
        MOV RAX, SYS_EXIT
        XOR RDI, RDI
        SYSCALL
        
    input:
        MOV RDI, [RBP+24] ;MOV arg1 to RDI.
        CALL strlen ;Call our string length function.
        MOV [RBP-8], RAX ;Move string length result into RSP-8.

        MOV RDI, [RBP+24]
        MOV RSI, RAX
        CALL reverseString
        MOV [RBP-16], RAX ;Moving return pointer into RBP-16.
        MOV RSI, RAX ;Moving new string pointer to RSI for SYS_WRITE.

        MOV RAX, SYS_WRITE
        MOV RDI, STDOUT
        ;RSI already handled earlier.
        MOV RDX, [RBP-8] ;Moving string length into RDX.
        SYSCALL
        ;Deallocating memory.
        MOV RAX, SYS_MUNMAP
        MOV RDI, [RBP-16] ;Move string pointer into RDI to be unmapped.
        MOV RSI, [RBP-8] ;Move amount of memory to be unmapped in bytes.
        SYSCALL

        ;Epilog
        ADD RSP, _start.STACK_INIT
        MOV RSP, RBP
        POP RBP

        ;Exit
        MOV RAX, SYS_EXIT
        XOR RDI, RDI
        SYSCALL
```

Below you'll find an up-to-date list of articles by me on [The Renegade Coder](https://therenegadecoder.com). For ease of browsing, emojis let you know the article category (i.e., blog: :black_nib:, code: :computer:, meta: :thought_balloon:, teach: :apple:)

- :black_nib: [I’m Learning a Language, and I’m Tired](https://therenegadecoder.com/blog/im-learning-a-language-and-im-tired/)
- :apple: [Yes, You Need General Education in College](https://therenegadecoder.com/teach/yes-you-need-general-education-in-college/)
- :apple: [Higher Education Should Not Be a Job Training Program](https://therenegadecoder.com/teach/higher-education-should-not-be-a-job-training-program/)
- :black_nib: [Why Generative AI Makes the Future of Software Development Worse](https://therenegadecoder.com/blog/why-generative-ai-makes-the-future-of-software-development-worse/)
- :black_nib: [Technology Will Not Liberate Us](https://therenegadecoder.com/blog/technology-will-not-liberate-us/)
- :black_nib: [The Future of AI Is Ubiquitous Surveillance](https://therenegadecoder.com/blog/the-future-of-ai-is-ubiquitous-surveillance/)
- :black_nib: [Y’all Need to Stop Using Generative AI for Summaries](https://therenegadecoder.com/blog/yall-need-to-stop-using-generative-ai-for-summaries/)
- :computer: [Loop Invariants Are Necessary for Writing Proper Loops](https://therenegadecoder.com/code/loop-invariants-are-necessary-for-writing-proper-loops/)
- :computer: [Dark Arts: Labeled Statements in Java](https://therenegadecoder.com/code/dark-arts-labeled-statements-in-java/)
- :apple: [Gamification Will Not Solve “America’s Education Crisis”](https://therenegadecoder.com/teach/gamification-will-not-solve-americas-education-crisis/)

Also, here are some fun links you can use to support my work.

- [Patreon](https://www.patreon.com/TheRenegadeCoder)
- [Discord](https://discord.gg/Jhmtj7Z)
- [Mailing List](https://therenegadecoder.com/about/newsletter)
- [Twitter](https://twitter.com/RenegadeCoder94)
- [YouTube](https://www.youtube.com/channel/UCpyoVwOqYRlSAEUPEn7P9hw)

***

This document was automatically rendered on 2025-10-03 using [SnakeMD](https://www.snakemd.io).
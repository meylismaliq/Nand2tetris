// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    // for initial cleaning of screen
    @status
    M = 1 
(MONITOR)
    @KBD
    D = M
    //if D is not equal to zero, go to DARK
    @DARK
    D; JNE
    // if status is not equal to 0, go to Bright
    @status
    D = M
    @BRIGHT
    D; JNE
    //go to monitor
    @MONITOR
    0; JMP

(DARK)
    @SCREEN
    D = A
    @addr
    M = D //addr=16384, screens base address
(LOOPDARK)
    @KBD
    D = A
    @addr
    D = D - M
    @ENDDARK
    D; JLE   // if KBD-addr <=o, goto enddark
    @addr
    A = M
    M = -1 // RAM[addr] = 1111111111111111
    @addr
    M = M + 1  //addr = addr +1
    @LOOPDARK
    0; JMP    //goto dark loop

(ENDDARK)
  //Set status as dirty screen
    @status
    M = 1
    //Jump to monitor
    @MONITOR
    0; JMP

(BRIGHT)
    @SCREEN
    D = A
    @addr
    M = D //addr=16384, screens base address
(LOOPBRIGHT)
    @KBD  
    D = A
    @addr
    D = D-M
    @ENDBRIGHT
    D; JLE   // if KBD-addr <=o, goto endbright
    @addr
    A = M
    M = 0 // RAM[addr] = 000000000000000000  
    @addr
    M = M + 1  //addr = addr +1
    @LOOPBRIGHT
    0; JMP    //goto bright loop
    
(ENDBRIGHT)
    //Set status as clean screen
    @status
    M = 0
    //Jump to monitor
    @MONITOR
    0; JMP
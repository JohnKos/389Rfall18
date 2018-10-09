section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame
	
	mov rcx, rdi
	add rcx, rdx
	mov rcx, [rcx]
	start:
	cmp rdx, 0
	je finish
	mov [rdi], rsi
	inc rdi
	dec rdx
	cmp rdx, 0
	jnz start
	mov [rdi], rcx
	finish: 	
	

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame

	mov rcx, rdi
	add rcx, rdx
	mov rcx, [rcx]
	staart:
	cmp rdx, 0
	je fiinish
	mov r11, [rsi]
	mov [rdi], r11
	inc rsi
	inc rdi
	dec rdx
	cmp rdx, 0
	jnz staart
	fiinish: 
	mov [rdi], rcx

        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!

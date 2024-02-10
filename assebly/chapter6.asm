; Project Name
; Project Description
; Author

.686
.model flat,stdcall
.stack 4096
;ExitProcess PROTO, dwExitCode:DWORD

INCLUDE Irvine32.inc

.data
; create variables here
;a1 word ?
;a2 word ?
;a3 word ?

array sword 0,0,0,3,4,2,5,7
nonmsg byte "all elements are non-zero"

.codeA
main PROC
	
	mov ebx,  OFFSET array
	mov ecx, LENGTHOF array

	L1:
		cmp word PTR [ebx], 0
		jnz found
		add ebx, 2
		loop L1
		jmp notFound

	found: 
		movsx eax, word PTR [ebx]
		mov edx, ebx
		;call WriteInt
		jmp quit

	notFound:
		mov edx, OFFSET nonmsg
		;call WriteString

	quit:
		call DumpRegs
		call Crlf
		exit
		
		

	
	;mov ax , a1	
	;cmp ax, a2
	;jbe l1
	;mov ax, a2
	;l1:
	;	cmp ax, a3
	;	jbe l2
	;	mov ax, a3
	;l2: 
	;	exit



	
	;exit
main ENDP

END main
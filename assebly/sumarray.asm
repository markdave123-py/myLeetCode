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
	nums word 2,1,1,1,1,1,1,1,1
	len word LENGTHOF nums


.code
main PROC
	
	mov esi, 0
	mov ax, 0
	mov cx, len

	l1: cmp si, len
		je l2
		add ax, nums[esi * 2]
		inc si
		loop l1

	l2: call DumpRegs
		exit


	
	
	
main ENDP

END main
# Approach to solve buffer overflow challenge : ApoorvCTF 2025



### Running the binary
![image](https://github.com/user-attachments/assets/f7a6dafd-6b41-4e7e-b2ff-a793ad41da3f)

Nothing interesting

### Reverse engineering using dogblot (Xrays)

<details>
  <summary>Click to expand the code</summary>
  
```c
/* This file was generated by the Hex-Rays decompiler version 8.4.0.240320.
   Copyright (c) 2007-2021 Hex-Rays <info@hex-rays.com>

   Detected compiler: GNU C++
*/

#include <defs.h>


//-------------------------------------------------------------------------
// Function declarations

void *init_proc();
int sub_80483D0();
// void setbuf(FILE *stream, char *buf);
// int printf(const char *format, ...);
// char *gets(char *s);
// char *fgets(char *s, int n, FILE *stream);
// int fclose(FILE *stream);
// int puts(const char *s);
// int __cdecl __libc_start_main(int (__cdecl *main)(int, char **, char **), int argc, char **ubp_av, void (*init)(void), void (*fini)(void), void (*rtld_fini)(void), void *stack_end);
// FILE *fopen(const char *filename, const char *modes);
// int _gmon_start__(void); weak
// void __usercall __noreturn start(int a1@<eax>, void (*a2)(void)@<edx>);
void _x86_get_pc_thunk_bx();
int deregister_tm_clones();
int register_tm_clones();
int _do_global_dtors_aux();
int frame_dummy();
int brew_coffee();
int order_coffee();
int __cdecl main(int argc, const char **argv, const char **envp);
void _libc_csu_init(void); // idb
void _libc_csu_fini(void); // idb
void term_proc();

//-------------------------------------------------------------------------
// Data declarations

const char aWelcomeToKogar[24] = "Welcome to Kogarashi Caf"; // idb
int (*_frame_dummy_init_array_entry[2])() = { &frame_dummy, &_do_global_dtors_aux }; // weak
int (*_do_global_dtors_aux_fini_array_entry)() = &_do_global_dtors_aux; // weak
Elf32_Dyn *GLOBAL_OFFSET_TABLE_ = &DYNAMIC; // weak
int (*dword_804A008)(void) = NULL; // weak
FILE *_bss_start; // idb
char completed_7209; // weak
// extern _UNKNOWN __gmon_start__; weak


//----- (080483A4) --------------------------------------------------------
void *init_proc()
{
  void *result; // eax

  result = &__gmon_start__;
  if ( &__gmon_start__ )
    return (void *)_gmon_start__();
  return result;
}
// 8048460: using guessed type int _gmon_start__(void);

//----- (080483D0) --------------------------------------------------------
int sub_80483D0()
{
  return dword_804A008();
}
// 804A008: using guessed type int (*dword_804A008)(void);

//----- (08048470) --------------------------------------------------------
// positive sp value has been detected, the output may be wrong!
void __usercall __noreturn start(int a1@<eax>, void (*a2)(void)@<edx>)
{
  int v2; // esi
  int v3; // [esp-4h] [ebp-4h] BYREF
  char *retaddr; // [esp+0h] [ebp+0h] BYREF

  v2 = v3;
  v3 = a1;
  __libc_start_main((int (__cdecl *)(int, char **, char **))main, v2, &retaddr, _libc_csu_init, _libc_csu_fini, a2, &v3);
  __halt();
}
// 8048473: positive sp value 4 has been found

//----- (080484A0) --------------------------------------------------------
void _x86_get_pc_thunk_bx()
{
  ;
}

//----- (080484B0) --------------------------------------------------------
int deregister_tm_clones()
{
  int result; // eax

  result = 134520887 - (_DWORD)&_bss_start;
  if ( (unsigned int)(134520887 - (_DWORD)&_bss_start) > 6 )
    return 0;
  return result;
}
// 80484B0: could not find valid save-restore pair for ebp

//----- (080484E0) --------------------------------------------------------
int register_tm_clones()
{
  return 0;
}
// 80484E0: could not find valid save-restore pair for ebp

//----- (08048520) --------------------------------------------------------
int _do_global_dtors_aux()
{
  int result; // eax

  if ( !completed_7209 )
  {
    result = deregister_tm_clones();
    completed_7209 = 1;
  }
  return result;
}
// 8048520: could not find valid save-restore pair for ebp
// 804A038: using guessed type char completed_7209;

//----- (08048540) --------------------------------------------------------
int frame_dummy()
{
  return register_tm_clones();
}
// 8048540: could not find valid save-restore pair for ebp

//----- (0804856B) --------------------------------------------------------
int brew_coffee()
{
  char s[128]; // [esp+Ch] [ebp-8Ch] BYREF
  FILE *stream; // [esp+8Ch] [ebp-Ch]

  stream = fopen("flag.txt", "r");
  if ( !stream )
    return puts("Barista: 'Strange... the recipe is missing.(Create flag.txt)'");
  fgets(s, 128, stream);
  printf("Barista: 'A rare choice... here is your secret blend.'\n%s\n", s);
  return fclose(stream);
}

//----- (080485E6) --------------------------------------------------------
int order_coffee()
{
  char s[40]; // [esp+0h] [ebp-28h] BYREF

  puts(aWelcomeToKogar);
  puts("Barista: 'What will you have?'");
  gets(s);
  printf("Barista: '%s... interesting choice.'\n", s);
  return puts("Brewing...");
}

//----- (08048642) --------------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setbuf(_bss_start, 0);
  order_coffee();
  return 0;
}

//----- (08048680) --------------------------------------------------------
void _libc_csu_init(void)
{
  int v0; // esi
  int i; // edi

  init_proc();
  v0 = ((char *)&_do_global_dtors_aux_fini_array_entry
      - ((char *)&_frame_dummy_init_array_entry[-33630208]
       + (_DWORD)&GLOBAL_OFFSET_TABLE_)) >> 2;
  if ( v0 )
  {
    for ( i = 0; i != v0; ++i )
      _frame_dummy_init_array_entry[i]();
  }
}
// 8049F08: using guessed type int (*_frame_dummy_init_array_entry[2])();
// 8049F0C: using guessed type int (*_do_global_dtors_aux_fini_array_entry)();
// 804A000: using guessed type Elf32_Dyn *GLOBAL_OFFSET_TABLE_;

//----- (080486E4) --------------------------------------------------------
void term_proc()
{
  ;
}

// nfuncs=32 queued=13 decompiled=13 lumina nreq=0 worse=0 better=0
// ALL OK, 13 function(s) have been successfully decompiled

```
</details>


### Three Interesting functions
```c
//----- (0804856B) --------------------------------------------------------
int brew_coffee()
{
  char s[128]; // [esp+Ch] [ebp-8Ch] BYREF
  FILE *stream; // [esp+8Ch] [ebp-Ch]

  stream = fopen("flag.txt", "r");
  if ( !stream )
    return puts("Barista: 'Strange... the recipe is missing.(Create flag.txt)'");
  fgets(s, 128, stream);
  printf("Barista: 'A rare choice... here is your secret blend.'\n%s\n", s);
  return fclose(stream);
}

//----- (080485E6) --------------------------------------------------------
int order_coffee()
{
  char s[40]; // [esp+0h] [ebp-28h] BYREF

  puts(aWelcomeToKogar);
  puts("Barista: 'What will you have?'");
  gets(s);
  printf("Barista: '%s... interesting choice.'\n", s);
  return puts("Brewing...");
}

//----- (08048642) --------------------------------------------------------
int __cdecl main(int argc, const char **argv, const char **envp)
{
  setbuf(_bss_start, 0);
  order_coffee();
  return 0;
}

```


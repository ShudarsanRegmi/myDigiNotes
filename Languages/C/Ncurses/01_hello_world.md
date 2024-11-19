# Hello, world

### Installation
```bash
sudo apt install build-essentials
sudo apt install libcurses5-dev libncursesw5-dev
```

```c
#include <curses.h>

int main() {

	int screen_height = 40;
	int screen_width = 20;

	// initialize screen 
	WINDOW *win = initscr();
	printw("Hello, world");

	refresh();
	getch();
	endwin();
	return 0;
}
```

### Compiling 
```bash
gcc -o out main.c -lncurses
```

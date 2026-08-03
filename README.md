# Karbox Engine
Continuation of a Python terminal game engine, Karton, written from scratch and now featuring colors!
<img width="1920" height="1080" alt="karbox-demo2" src="https://github.com/user-attachments/assets/34a4f83c-f250-4eb5-aa7c-0b714921b1c8" />
## Features
- Rich text with ANSI escape codes
- Layers
- Basic drawing functions:
  - One character insert
  - Lines
  - Rectangle (outline or solid)
  - Text
- Inputs at a specified position
- **Groups** with next functions:
  - loading texture from a text file
  - saving texture in color
  - loading texture in color
  - moving by x and/or y
  - moving to a position
  - touch detection
## Bad Apple Demo
This is how to run it:
```bash
python /demos/bad-apple/badapple.py
```
 ---
 For now this engine is pretty basic. To make the image above i used two rectangle and one text function, `sys.get_terminal_size()` to make it fill the whole terminal.

 I'm thinking about adding this to PyPI soon

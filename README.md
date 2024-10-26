# sound triggered search

## motivation

one day, my friend jokingly mentioned he'd like made: when he
clapped, a window filled with "sexy girls" would pop up on
screen.

lo and behold, this mini meme project.

## how this works

if you have Python, you can use Python to run `script.py`
directly. (and also use it to change the search query)

if not, you can run `script.exe` on WindowsOS.

i still have not figured out how to make the `.dmg` file
for MacOS.

## considerations when i made the script

1. `ctypes` vs `tkinter.messagebox`: i used `tkinter.messagebox`
at first, but there was an additional popup window (other than
the one i wanted to popup) that existed and i did not know how
to get rid of it. so, i used `ctypes` instead.

2. `struct` vs `numpy`: initially, `struct.unpack()` was used
to unpack the audio bytes into integers. in the end though,
`numpy` was used because it seems neater.

## reflections

i learnt:

1. how to use `PyAudio` to continuously read audio data from user
2. how to create a popup window using Python
3. how greatly convenient tools like gptengineer are to test out
ideas

## references

1. gptengineer (for my proof of concept)
2. [this nice youtube video which taught me how to use `PyAudio`](https://youtu.be/AShHJdSIxkY?si=xGkza8E3fjoo0Eio)

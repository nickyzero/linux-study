#!/usr/bin/python3

import os
os.posix_spawn("/bin/echo", ["echo", "echo", "Posix_spawn()으로 생성되었습니다."],{})
print("echo 명령어를 생성했습니다")


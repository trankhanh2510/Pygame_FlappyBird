# Pygame_FlappyBird
build file .exe
pyinstaller --onefile --noconsole --add-data "assets;assets" --add-data "sound;sound" --add-data "04B_19.ttf;." flappybird.py

--onefile: Đóng gói tất cả vào một file .exe.
--noconsole: Ẩn cửa sổ terminal nếu là game có giao diện.
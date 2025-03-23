# Pygame_FlappyBird
build file .exe
pyinstaller --onefile --noconsole --add-data "assets;assets" --add-data "sound;sound" --add-data "04B_19.ttf;." flappybird.py

--onefile: Đóng gói tất cả vào một file .exe.
--noconsole: Ẩn cửa sổ terminal nếu là game có giao diện.
📌 Lưu ý: Nếu bạn chọn lưu file high_score.txt trong AppData, bạn có thể thay đổi base_dir như sau:
base_dir = os.path.join(os.getenv('APPDATA'), 'MyGame')
os.makedirs(base_dir, exist_ok=True)  # Tạo thư mục nếu chưa có

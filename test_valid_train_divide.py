import os
import shutil
import random

# 設定路徑
source_dir = "C:/Users/rayso_sq9ff/Downloads/fruit/train/train"  # 您原始數據的目錄
train_dir = "C:/Users/rayso_sq9ff/Desktop/try/train"    # 訓練數據的目錄
test_dir = "C:/Users/rayso_sq9ff/Desktop/try/test"      # 測試數據的目錄
valid_dir = "C:/Users/rayso_sq9ff/Desktop/try/valid"    # 驗證數據的目錄

# 創建目標目錄
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)
os.makedirs(valid_dir, exist_ok=True)

# 獲取所有檔案
files = os.listdir(source_dir)

# 對每個檔案夾進行處理
for file in files:
    file_path = os.path.join(source_dir, file)

    # 如果是檔案夾
    if os.path.isdir(file_path):
        images = os.listdir(file_path)
        random.shuffle(images)

        # 計算分配給每個集的數量
        total_images = len(images)
        train_size = int(0.7 * total_images)
        test_size = int(0.2 * total_images)
        valid_size = total_images - train_size - test_size

        # 創建目標檔案夾
        train_file_path = os.path.join(train_dir, file)
        test_file_path = os.path.join(test_dir, file)
        valid_file_path = os.path.join(valid_dir, file)
        os.makedirs(train_file_path, exist_ok=True)
        os.makedirs(test_file_path, exist_ok=True)
        os.makedirs(valid_file_path, exist_ok=True)

        # 分配圖片到各個集
        for i in range(train_size):
            shutil.copy(os.path.join(file_path, images[i]), os.path.join(train_file_path, images[i]))
        for i in range(train_size, train_size + test_size):
            shutil.copy(os.path.join(file_path, images[i]), os.path.join(test_file_path, images[i]))
        for i in range(train_size + test_size, total_images):
            shutil.copy(os.path.join(file_path, images[i]), os.path.join(valid_file_path, images[i]))

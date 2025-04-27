import os
import uuid
from fastapi import UploadFile

UPLOAD_DIR = "./static/posters"

os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_image(file: UploadFile) -> str:
    # Валидация по размеру и типу
    content = file.file.read()
    if len(content) > 2 * 1024 * 1024:  # 2 МБ
        raise HTTPException(status_code=400, detail="Размер файла превышает 2MB")
    filename = file.filename
    ext = os.path.splitext(filename)[1]
    new_filename = f"{uuid.uuid4()}{ext}"
    save_path = os.path.join(UPLOAD_DIR, new_filename)

    # Записываем файл
    with open(save_path, "wb") as f:
        f.write(content)

    return f"/static/posters/{new_filename}"

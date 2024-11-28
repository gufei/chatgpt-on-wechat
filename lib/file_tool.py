import os


def get_file_extension(file_url):
    """从文件链接中提取文件扩展名"""
    return os.path.splitext(file_url)[1].lower()

def is_image_file(file_url):
    ext = os.path.splitext(file_url)[1].lower()
    """判断文件扩展名是否为图片类型"""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']
    return ext in image_extensions

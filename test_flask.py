import requests

# Test için bir görsel dosya yolu
image_path = "C:/Users/i_naz/Pictures/test_image.jpg"  # Kendi görsel dosyanın yolunu buraya yaz

# Flask servisine istek gönder
with open(image_path, 'rb') as f:
    files = {'image': f}
    response = requests.post('http://localhost:5001/analyze', files=files)

# Yanıtı yazdır
print(response.json())

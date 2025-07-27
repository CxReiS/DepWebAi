"""Google Analytics entegrasyonu örneği."""


def send_event(category: str, action: str):
    """Sadece ekrana yazar"""
    print(f"GA {category}:{action}")

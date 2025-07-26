"""S3 depolaması işlemleri."""


def save(path: str, bucket: str) -> str:
    """Kaydedilen nesnenin adını döner"""
    obj = f"{bucket}/{path}"
    print(f"S3 save {obj}")
    return obj

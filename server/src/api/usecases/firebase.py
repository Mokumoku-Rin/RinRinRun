from firebase_admin import storage

def fetch_landmark_image(filename: str) -> bytes:
  bucket = storage.bucket()
  blob = bucket.blob(filename)
  b = blob.download_as_string(raw_download=True)
  return b

def upload_landmark_image(filename: str, data: bytes) -> bool:
  blob = storage.bucket().blob()
  blob.upload_from_string(data, content_type="image/jpeg")
  return True
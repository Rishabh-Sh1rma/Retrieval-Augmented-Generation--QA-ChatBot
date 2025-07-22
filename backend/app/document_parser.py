import cv2
from typing import List

def parse_document(filepath: str) -> str:
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = "Extracted text from document image"
    return text

def chunk_text(text: str, max_tokens: int = 500) -> List[str]:
    words = text.split()
    return [" ".join(words[i:i+max_tokens]) for i in range(0, len(words), max_tokens)]

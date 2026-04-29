import os
import cv2
import numpy as np
import insightface
from typing import Optional, List, Dict

# ===============================
# ADVANCED FACE ENGINE
# ===============================

class FaceRecognitionEngine:
    def __init__(self):
        self.model = insightface.app.FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.model.prepare(
            ctx_id=0,
            det_size=(640, 640)
        )

        print("✅ InsightFace model loaded")

    # ===============================
    # IMAGE LOADER
    # ===============================
    def load_image(self, img_path: str):
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"Image not found: {img_path}")

        img = cv2.imread(img_path)

        if img is None:
            raise ValueError("Cannot read image")

        return img

    # ===============================
    # PREPROCESS IMAGE
    # ===============================
    def preprocess(self, img):
        img = cv2.resize(img, (900, 700))
        return img

    # ===============================
    # DETECT ALL FACES
    # ===============================
    def detect_faces(self, img) -> List:
        return self.model.get(img)

    # ===============================
    # GET BEST FACE
    # ===============================
    def get_best_face(self, faces):
        if len(faces) == 0:
            return None

        # choose largest face
        best = max(
            faces,
            key=lambda x: (x.bbox[2] - x.bbox[0]) * (x.bbox[3] - x.bbox[1])
        )

        return best

    # ===============================
    # NORMALIZE EMBEDDING
    # ===============================
    def normalize(self, emb):
        return emb / np.linalg.norm(emb)

    # ===============================
    # MAIN EMBEDDING FUNCTION
    # ===============================
    def get_embedding(self, img_path: str) -> Optional[np.ndarray]:

        try:
            img = self.load_image(img_path)

            img = self.preprocess(img)

            faces = self.detect_faces(img)

            if len(faces) == 0:
                print("❌ No face found")
                return None

            face = self.get_best_face(faces)

            emb = face.embedding

            emb = self.normalize(emb)

            return emb

        except Exception as e:
            print("ERROR:", e)
            return None

    # ===============================
    # MULTIPLE EMBEDDINGS
    # ===============================
    def get_all_embeddings(self, img_path: str):

        try:
            img = self.load_image(img_path)

            faces = self.detect_faces(img)

            result = []

            for face in faces:
                emb = self.normalize(face.embedding)

                result.append({
                    "bbox": face.bbox.tolist(),
                    "embedding": emb
                })

            return result

        except:
            return []

    # ===============================
    # COSINE SIMILARITY
    # ===============================
    def compare(self, emb1, emb2):

        if emb1 is None or emb2 is None:
            return 0.0

        score = np.dot(emb1, emb2)

        return float(score)

    # ===============================
    # MATCH RESULT
    # ===============================
    def verify(self, emb1, emb2, threshold=0.55):

        score = self.compare(emb1, emb2)

        return {
            "match": score >= threshold,
            "score": round(score, 4),
            "threshold": threshold
        }


# ===============================
# GLOBAL INSTANCE
# ===============================

engine = FaceRecognitionEngine()


# ===============================
# USER FUNCTION
# ===============================
def get_embedding(img_path):
    return engine.get_embedding(img_path)
# Emotion Detector

IBM Watson NLP Emotion Detector (oaqjp-final-project-emb-ai).

## Run

```bash
pip install -r requirements.txt
python server.py
```

Open http://127.0.0.1:5000.

## Checks

```bash
python -m unittest test_emotion_detection -v
pylint server.py
```

The detector returns anger, disgust, fear, joy, sadness, and dominant_emotion. Blank input and Watson status 400 return None for all fields.

Unit tests use mocked Watson HTTP responses. They verify the required five emotions, output format, blank input, and status 400; they do not verify the live model. The live Skills Network Watson endpoint timed out from this computer during preparation. No live Watson success is claimed.

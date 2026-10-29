# Emotion Detector

IBM Watson NLP Emotion Detector (oaqjp-final-project-emb-ai).

## Run

```bash
pip install -r requirements.txt
python server.py
```

Open http://127.0.0.1:5000 locally, or use the course lab's application launcher on port 5000.

## Checks

```bash
python -m unittest test_emotion_detection -v
pylint server.py
```

The detector returns anger, disgust, fear, joy, sadness, and dominant_emotion. Blank input and Watson status 400 return None for all fields.

`test_emotion_detection.py` tests the five required phrases against the real Watson service. Run it where the endpoint is reachable. `test_emotion_logic.py` separately tests formatting and error handling using mocked HTTP responses.

The live Skills Network Watson endpoint timed out from this computer during preparation. No live Watson success is claimed. Live test output must be captured in an environment where the service responds.

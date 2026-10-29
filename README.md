# Final Project

IBM Watson NLP Emotion Detector (oaqjp-final-project-emb-ai).

## Run

```bash
pip install -r requirements.txt
python server.py
```

Open http://127.0.0.1:5000 in your browser.

## Checks

```bash
python -m unittest test_emotion_detection -v
pylint server.py
```

The detector returns anger, disgust, fear, joy, sadness, and dominant_emotion. Blank input and Watson status 400 return None for all fields.

`test_emotion_detection.py` tests the five required phrases, output formatting, blank input, and status 400 using explicitly mocked Watson HTTP responses. `test_emotion_service.py` preserves the five live-service tests; run it when the Watson endpoint is reachable.

The live Skills Network Watson endpoint timed out from this computer during preparation. No live Watson success is claimed. Live test output must be captured in an environment where the service responds.

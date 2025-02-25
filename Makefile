init: ; rm -r ./.venv && python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
dev: ; source .venv/bin/activate && flask run --host=0.0.0.0 --port 5001 --debug

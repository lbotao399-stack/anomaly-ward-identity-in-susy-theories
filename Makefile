PYTHON ?= python3

.PHONY: verify hashes notion-payload

verify:
	$(PYTHON) -m unittest discover -s tests -v

hashes:
	$(PYTHON) scripts/update_contract_hashes.py

notion-payload:
	$(PYTHON) scripts/build_notion_payload.py --source contracts/foundations/step-01-supersymmetry-commutator.md --commit "$$(git rev-parse HEAD)"

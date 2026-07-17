#!/bin/bash
# post-processing pipeline once kite_raw.pkl exists
set -e
cd "$(dirname "$0")"
python3 finalize.py > finalize.log 2>&1
python3 summarize.py > summarize.log 2>&1
# prepend calibration record to the summary
cat ../calib_section.md ../engine_A_summary.md > /tmp/eng_a_sum.$$ && mv /tmp/eng_a_sum.$$ ../engine_A_summary.md
echo DONE

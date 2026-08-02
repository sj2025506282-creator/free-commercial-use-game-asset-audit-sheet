import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "summarize_answer_log.py"
SPEC = importlib.util.spec_from_file_location("summarize_answer_log", SCRIPT)
SUMMARY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SUMMARY)


SAMPLE = """\
| 2026-08-01 | Reddit | r/godot | Direct fit | https://example.com/1 | Skip | Low | None | No | Score 2/2/2/2/1 = 9. Existing answer. |
| 2026-08-02 | Reddit | r/Unity3D | Posted | https://example.com/2 | Answer only | Low | None | Yes | Score 1/2/2/2/2 = 9. 48-72h readback: score 1. |
| not-a-date | Reddit | r/godot | Invalid | URL | Skip | Low | None | No | Invalid. |
"""


class AnswerLogSummaryTests(unittest.TestCase):
    def test_parse_and_summarize(self):
        result = SUMMARY.summarize(SUMMARY.parse_rows(SAMPLE))
        self.assertEqual(result["candidate_count"], 2)
        self.assertEqual(result["decisions"], {"Answer only": 1, "Skip": 1})
        self.assertEqual(result["reply_posted_count"], 1)
        self.assertEqual(result["linked_candidate_count"], 0)
        self.assertEqual(result["direct_fit_count"], 1)
        self.assertEqual(result["mature_outcome_readback_count"], 1)


if __name__ == "__main__":
    unittest.main()

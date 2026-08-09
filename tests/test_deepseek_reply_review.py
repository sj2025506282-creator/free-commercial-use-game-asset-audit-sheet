import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "deepseek_reply_review.py"
SPEC = importlib.util.spec_from_file_location("deepseek_reply_review", SCRIPT)
REVIEW = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REVIEW)


class DeepSeekReplyReviewTests(unittest.TestCase):
    def test_prompt_includes_normalized_existing_reply_ids(self):
        prompt = REVIEW.build_user_prompt(
            {
                "thread": "Question summary",
                "existing_replies": "One existing answer",
                "existing_reply_ids": [" second ", "first", "first"],
                "draft": "Draft answer",
            }
        )

        self.assertIn('Existing reply IDs:\n["first", "second"]', prompt)
        self.assertIn("ordinary user a concrete first action", prompt)
        self.assertIn("what success looks like", prompt)


if __name__ == "__main__":
    unittest.main()

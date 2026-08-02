import hashlib
import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "reddit_prepublish_gate.py"
SPEC = importlib.util.spec_from_file_location("reddit_prepublish_gate", SCRIPT)
GATE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(GATE)


def valid_payload():
    draft = "Use the local-space hit normal. Convert it first, then compare axes."
    return {
        "community": "Unity3D",
        "community_status_verified": True,
        "rules_allow_ordinary_help": True,
        "moderator_sensitive": False,
        "thread_open": True,
        "existing_replies_reviewed": True,
        "legal_or_commercial_dispute": False,
        "useful_without_link_verified": True,
        "opening_answer_verified": True,
        "live_reply_ids": ["existing1"],
        "concrete_gap": "Adds the local-space conversion missing from current replies.",
        "today_public_comment_count": 0,
        "scores": {
            "thread_fit": 1,
            "helpfulness": 2,
            "risk": 2,
            "link_fit": 2,
            "originality": 2,
        },
        "draft": draft,
        "deepseek": {
            "usefulness_score": 9,
            "subreddit_tone_score": 8,
            "promotion_risk_score": 0,
            "brevity_score": 8,
            "redundancy_risk_score": 2,
            "recommendation": "Yes",
            "link_dependency": "None",
            "link_decision": "no_link_present",
            "draft_sha256": hashlib.sha256(draft.encode("utf-8")).hexdigest(),
            "reviewed_reply_ids": ["existing1"],
        },
    }


class PublishGateTests(unittest.TestCase):
    def test_valid_no_link_candidate_passes(self):
        result = GATE.evaluate(valid_payload())
        self.assertTrue(result["passed"])
        self.assertEqual(result["candidate_total"], 9)

    def test_changed_draft_fails_hash_binding(self):
        payload = valid_payload()
        payload["draft"] += " Extra unreviewed sentence."
        result = GATE.evaluate(payload)
        self.assertFalse(result["passed"])
        self.assertIn(
            "draft body does not match the DeepSeek-reviewed hash",
            result["failures"],
        )

    def test_new_live_reply_requires_re_review(self):
        payload = valid_payload()
        payload["live_reply_ids"].append("new_reply")
        result = GATE.evaluate(payload)
        self.assertFalse(result["passed"])
        self.assertIn(
            "live reply ids changed after DeepSeek review; re-read and re-review",
            result["failures"],
        )

    def test_banned_language_and_daily_cap_fail(self):
        payload = valid_payload()
        payload["today_public_comment_count"] = 1
        payload["draft"] = "Use this paid upgrade."
        payload["deepseek"]["draft_sha256"] = hashlib.sha256(
            payload["draft"].encode("utf-8")
        ).hexdigest()
        result = GATE.evaluate(payload)
        self.assertFalse(result["passed"])
        self.assertIn("a public comment was already posted today", result["failures"])
        self.assertTrue(
            any(reason.startswith("banned public language") for reason in result["failures"])
        )

    def test_gamedev_is_blocked(self):
        payload = valid_payload()
        payload["community"] = "r/gamedev"
        result = GATE.evaluate(payload)
        self.assertFalse(result["passed"])
        self.assertIn("r/gamedev is read-only", result["failures"])

    def test_link_requires_github_and_keep(self):
        payload = valid_payload()
        payload["draft"] += " https://example.com/tool"
        payload["deepseek"]["draft_sha256"] = hashlib.sha256(
            payload["draft"].encode("utf-8")
        ).hexdigest()
        result = GATE.evaluate(payload)
        self.assertFalse(result["passed"])
        self.assertIn("public link is not on github.com", result["failures"])
        self.assertIn("DeepSeek did not explicitly keep the link", result["failures"])


if __name__ == "__main__":
    unittest.main()

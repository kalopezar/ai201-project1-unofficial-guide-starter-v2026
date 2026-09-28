import unittest
from types import SimpleNamespace

from scorer import judge


class JudgeTests(unittest.TestCase):
    def test_matches_expected_phrase_in_retrieved_chunk(self):
        results = [SimpleNamespace(text="A W doesn't affect GPA.")]

        self.assertTrue(
            judge(
                "What happens to my GPA if I withdraw?",
                "doesn't affect GPA",
                "A W doesn't affect your GPA.",
                results,
            )
        )

    def test_answer_phrase_does_not_replace_missing_retrieval_evidence(self):
        results = [SimpleNamespace(text="A W appears on the transcript.")]

        self.assertFalse(
            judge(
                "What happens to my GPA if I withdraw?",
                "doesn't affect GPA",
                "A W doesn't affect GPA.",
                results,
            )
        )

    def test_empty_expectation_fails(self):
        results = [SimpleNamespace(text="Any retrieved text")]

        self.assertFalse(judge("Question", "", "Answer", results))


if __name__ == "__main__":
    unittest.main()
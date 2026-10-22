"""Regression cases based on the tracker disappearing during a redesign."""
import unittest
from scripts.check_analytics import validate

TAG = '<script src="https://cdn.usefathom.com/script.js" data-site="HIYUJOPT" defer></script>'


class AnalyticsChecks(unittest.TestCase):
    def test_original_tracker_passes(self):
        validate(f"<!doctype html><html><head>{TAG}</head><body></body></html>")

    def test_removed_or_disabled_tracker_fails(self):
        cases = {
            "removed": "<head></head>",
            "commented out": f"<head><!-- {TAG} --></head>",
            "duplicate": f"<head>{TAG}{TAG}</head>",
            "wrong account": f"<head>{TAG.replace('HIYUJOPT', 'WRONGSITE')}</head>",
            "wrong source": f"<head>{TAG.replace('https://cdn.usefathom.com/script.js', 'https://example.com/script.js')}</head>",
            "missing defer": f"<head>{TAG.replace(' defer', '')}</head>",
            "disabled auto tracking": f"<head>{TAG.replace(' defer', ' data-auto="false" defer')}</head>",
            "non-executable": f"<head>{TAG.replace(' defer', ' type="text/plain" defer')}</head>",
            "in template": f"<head><template>{TAG}</template></head>",
            "in noscript": f"<head><noscript>{TAG}</noscript></head>",
            "outside head": f"<head></head><body>{TAG}</body>",
        }
        for name, html in cases.items():
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate(html)


if __name__ == "__main__":
    unittest.main()

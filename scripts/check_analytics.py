"""Fail publication when the existing Fathom pageview tracker is not intact."""
from html.parser import HTMLParser
from pathlib import Path
import sys

SCRIPT_URL = "https://cdn.usefathom.com/script.js"
SITE_ID = "HIYUJOPT"
EXPECTED = {"src": SCRIPT_URL, "data-site": SITE_ID, "defer": None}


class TrackerParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.inert_depth = 0
        self.trackers = []

    def handle_starttag(self, tag, attrs):
        if tag == "head":
            self.in_head = True
        if tag in {"template", "noscript"}:
            self.inert_depth += 1
        values = dict(attrs)
        if tag == "script" and (
            "usefathom.com" in values.get("src", "")
            or "data-site" in values
        ):
            self.trackers.append((attrs, self.in_head, self.inert_depth))

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False
        if tag in {"template", "noscript"}:
            self.inert_depth = max(0, self.inert_depth - 1)


def validate(html):
    parser = TrackerParser()
    parser.feed(html)
    if len(parser.trackers) != 1:
        raise ValueError("Expected exactly one Fathom tracker; missing or duplicate tracking blocks publication.")
    attrs, in_head, inert_depth = parser.trackers[0]
    if not in_head or inert_depth:
        raise ValueError("The Fathom script must be active in <head>, outside templates and noscript blocks.")
    if len(attrs) != len(EXPECTED) or dict(attrs) != EXPECTED:
        raise ValueError("Restore the original Fathom script: correct HTTPS source, site HIYUJOPT, defer, and no disabling attributes.")


def main():
    paths = [Path(p) for p in sys.argv[1:]] or [Path("index.html")]
    for path in paths:
        try:
            validate(path.read_text())
        except (OSError, ValueError) as error:
            print(f"FAIL {path}: {error}", file=sys.stderr)
            return 1
        print(f"PASS {path}: one active Fathom tracker for {SITE_ID}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

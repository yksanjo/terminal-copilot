#!/usr/bin/env python3
import argparse
import json


def suggest(last_cmd: str) -> list[str]:
    if "git status" in last_cmd:
        return ["git add -p", "git commit -m \"chore: checkpoint\"", "git push origin HEAD"]
    if "pytest" in last_cmd or "unittest" in last_cmd:
        return ["pytest -q", "pytest -k failing_test", "git diff"]
    if "npm run" in last_cmd:
        return ["npm test", "npm run lint", "npm run build"]
    return ["ls -la", "rg --files", "git status"]


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest next shell commands")
    parser.add_argument("--last-cmd", required=True)
    ns = parser.parse_args()

    print(json.dumps({"last_cmd": ns.last_cmd, "suggestions": suggest(ns.last_cmd)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

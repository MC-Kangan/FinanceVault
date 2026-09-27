#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from vault_core import build_alias_registry, validate_vault


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the CFA Obsidian vault")
    parser.add_argument("vault", nargs="?", type=Path, default=Path.cwd())
    parser.add_argument(
        "--write-alias-registry",
        action="store_true",
        help="write 99 System/Alias Registry.md after a clean validation",
    )
    args = parser.parse_args()
    vault = args.vault.resolve()
    issues = validate_vault(vault)
    if issues:
        for issue in issues:
            print(issue)
        print(f"Validation failed with {len(issues)} issue(s).")
        return 1
    if args.write_alias_registry:
        registry = vault / "99 System" / "Alias Registry.md"
        registry.parent.mkdir(parents=True, exist_ok=True)
        registry.write_text(build_alias_registry(vault), encoding="utf-8")
        print(f"Wrote {registry.relative_to(vault)}")
        issues = validate_vault(vault)
        if issues:
            for issue in issues:
                print(issue)
            print(f"Validation failed with {len(issues)} issue(s) after registry generation.")
            return 1
    print("Validation passed: 0 issues.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

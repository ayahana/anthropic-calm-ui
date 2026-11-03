#!/usr/bin/env python3
"""Check only the solid-color pairings defined for the bundled example tokens."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / 'references/tokens.css'


def luminance(color):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', color):
        raise ValueError(f'Expected a six-digit sRGB color, got {color!r}')
    values = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in values]
    return sum(a * b for a, b in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    bright, dark = sorted((luminance(a), luminance(b)), reverse=True)
    return (bright + 0.05) / (dark + 0.05)


def parse_themes(css):
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)
    themes = {}
    for name, selector in [('light', ':root'), ('dark', '.calm-ui[data-theme="dark"]')]:
        matches = re.findall(re.escape(selector) + r'\s*\{([^{}]*)\}', css)
        if len(matches) != 1:
            raise ValueError(f'Expected exactly one {selector} block')
        required = {'canvas', 'surface', 'surface-soft', 'text', 'text-muted', 'accent', 'success', 'warning', 'danger', 'border-control', 'focus', 'on-action', 'action', 'action-hover'}
        # Inspect every declaration, including unsupported values. Filtering for
        # hex first would silently retain an earlier color when CSS overrides it.
        declarations = re.findall(r'--calm-([\w-]+)\s*:\s*([^;]*)(?:;|$)', matches[0])
        values = {}
        for token, raw_value in declarations:
            if token not in required:
                continue
            if token in values:
                raise ValueError(f'Duplicate tested token in {name}: --calm-{token}')
            value = raw_value.strip()
            if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
                raise ValueError(f'Unsupported color for {name} --calm-{token}: {value!r}')
            values[token] = value
        if required - values.keys():
            raise ValueError(f'Missing literal colors in {name}: {sorted(required - values.keys())}')
        themes[name] = values
    return themes


def evaluate(css):
    rows = []
    for theme, colors in parse_themes(css).items():
        pairs = [(fg, bg, 3.0 if fg in ('border-control', 'focus') else 4.5)
                 for fg in ('text', 'text-muted', 'accent', 'success', 'warning', 'danger', 'border-control', 'focus')
                 for bg in ('canvas', 'surface', 'surface-soft')]
        pairs += [('on-action', bg, 4.5) for bg in ('action', 'action-hover')]
        for fg, bg, threshold in pairs:
            ratio = contrast(colors[fg], colors[bg])
            rows.append(dict(theme=theme, foreground=fg, background=bg, ratio=ratio,
                             threshold=threshold, passed=ratio >= threshold))
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tokens', type=Path, default=DEFAULT)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        rows = evaluate(args.tokens.read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        parser.exit(2, f'Input error: {exc}\n')
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=2))
    else:
        for row in rows:
            print(f"{'PASS' if row['passed'] else 'FAIL'} {row['theme']:5} {row['foreground']}/{row['background']}: {row['ratio']:.2f}:1 >= {row['threshold']}:1")
        print(f"{sum(row['passed'] for row in rows)}/{len(rows)} passed. Solid colors only; not a full accessibility audit.")
    return 0 if all(row['passed'] for row in rows) else 1


if __name__ == '__main__':
    raise SystemExit(main())

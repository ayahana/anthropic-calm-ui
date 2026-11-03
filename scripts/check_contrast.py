#!/usr/bin/env python3
"""Repository convenience entry point; implementation ships with the skill."""
from pathlib import Path
import runpy

if __name__ == '__main__':
    runpy.run_path(str(Path(__file__).resolve().parents[1] /
                      'skills/anthropic-calm-ui/scripts/check_contrast.py'),
                  run_name='__main__')

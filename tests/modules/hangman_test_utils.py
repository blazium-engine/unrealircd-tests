#!/usr/bin/python3
"""
Helper utilities for hangman module tests
"""

def extract_invite_code(invite_line):
    """Extract invite code from a 2505 numeric response line"""
    if not invite_line:
        return None
    parts = invite_line.split()
    # Format: :server 2505 client invite_code
    # We want the last token (invite_code)
    if len(parts) >= 4:
        return parts[-1]
    return None


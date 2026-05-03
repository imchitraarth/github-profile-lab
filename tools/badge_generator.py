#!/usr/bin/env python3
"""badge_generator.py - Generate shields.io badge markdown from CLI.

Usage:
    python tools/badge_generator.py --label build --message passing --color brightgreen
"""
import argparse, urllib.parse

COLORS = ['brightgreen','green','yellow','orange','red','blue','lightgrey','blueviolet']

def make_badge(label, message, color, style='flat'):
    l = urllib.parse.quote(label.replace('-','--').replace('_','__'))
    m = urllib.parse.quote(message.replace('-','--').replace('_','__'))
    url = f'https://img.shields.io/badge/{l}-{m}-{color}?style={style}'
    return f'![{label}: {message}]({url})'

def main():
    p = argparse.ArgumentParser(description='Generate GitHub README badge markdown.')
    p.add_argument('--label', help='Left side text')
    p.add_argument('--message', help='Right side text')
    p.add_argument('--color', default='blue')
    p.add_argument('--style', default='flat', choices=['flat','flat-square','plastic','for-the-badge','social'])
    p.add_argument('--list-colors', action='store_true')
    a = p.parse_args()
    if a.list_colors:
        print('\n'.join(COLORS)); return
    if not a.label or not a.message:
        p.error('--label and --message required')
    print(make_badge(a.label, a.message, a.color, a.style))

if __name__ == '__main__': main()

#!/usr/bin/env python3
"""Verify documented scope commands in a disposable Git repository."""
from pathlib import Path
import os
import subprocess
import tempfile
import unittest


class GitScopes(unittest.TestCase):
    def test_scope_snapshots(self):
        with tempfile.TemporaryDirectory(prefix='jim-review-git-') as directory:
            root = Path(directory)
            env = {**os.environ, 'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': os.devnull,
                   'GIT_AUTHOR_NAME': 'Fixture', 'GIT_COMMITTER_NAME': 'Fixture',
                   'GIT_AUTHOR_EMAIL': 'fixture@example.invalid', 'GIT_COMMITTER_EMAIL': 'fixture@example.invalid'}
            def git(*args):
                return subprocess.check_output(['git', '-C', directory, *args], env=env, text=True)
            def diff(*args):
                return git('--no-pager', 'diff', '--no-ext-diff', '--no-textconv', *args)
            git('init', '-q')
            (root / 'notes.txt').write_text('original\n')
            git('add', '--', 'notes.txt')
            self.assertIn('+original', diff('--cached', '--'))
            git('commit', '-qm', 'initial')
            initial = git('rev-parse', 'HEAD').strip()
            self.assertIn('+original', git('show', '--root', '--format=', '--no-ext-diff', '--no-textconv', initial, '--'))
            (root / 'notes.txt').write_text('staged\n')
            git('add', '--', 'notes.txt')
            (root / 'notes.txt').write_text('working\n')
            (root / 'new note.txt').write_text('untracked\n')
            before = git('status', '--porcelain=v1')
            index_before = (root / '.git/index').read_bytes()
            self.assertIn('+staged', diff('--cached', '--'))
            self.assertNotIn('+working', diff('--cached', '--'))
            self.assertEqual(git('show', ':notes.txt'), 'staged\n')
            self.assertIn('+working', diff('HEAD', '--'))
            self.assertNotIn('new note.txt', diff('HEAD', '--'))
            self.assertIn('new note.txt', git('ls-files', '--others', '--exclude-standard'))
            self.assertEqual(before, git('status', '--porcelain=v1'))
            self.assertEqual(index_before, (root / '.git/index').read_bytes())
            self.assertEqual(initial, git('rev-parse', 'HEAD').strip())
            git('add', '--', 'notes.txt')
            git('commit', '-qm', 'base-side change')
            base = git('rev-parse', 'HEAD').strip()
            git('checkout', '-qb', 'fixture-feature', initial)
            (root / 'feature.txt').write_text('feature\n')
            git('add', '--', 'feature.txt')
            git('commit', '-qm', 'feature-side change')
            feature = git('rev-parse', 'HEAD').strip()
            self.assertIn('notes.txt', diff(base, feature, '--'))
            self.assertNotIn('notes.txt', diff(base + '...' + feature, '--'))
            self.assertIn('+feature', diff(base + '...' + feature, '--'))
            self.assertEqual(git('show', initial + ':notes.txt'), 'original\n')


if __name__ == '__main__':
    unittest.main(verbosity=2)

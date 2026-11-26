import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from isil_validation_claim_audit.audit import audit, claims, evidence, main
from isil_validation_claim_audit.phrases import ISILVALIDATION, NOISILVALIDATION, GENERIC_NAMES


class AuditTests(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((len(ISILVALIDATION), len(NOISILVALIDATION), len(GENERIC_NAMES)), (50, 24, 24))
        for phrase in ISILVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (True, False))
        for phrase in NOISILVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (False, True))
        for text, expected in [('documented isil validation claim false', (True, False)), ('isil validation claim audit', (True, False)), ('documented no isil validation claim false', (False, True)), ('```\nvalidate isil\n```', (False, False)), ("doesn't validate isil", (False, True))]:
            with self.subTest(text=text):
                self.assertEqual(claims(text), expected)

    def test_routes(self):
        routes = ['import stdnum.isil\nstdnum.isil.validate(x)', 'import stdnum.isil as fg\nfg.is_valid(x)', 'from stdnum import isil\nisil.validate(x)', 'import stdnum\nstdnum.isil.is_valid(x)', 'from stdnum.isil import validate as v\nv(x)', 'from stdnum.isil import is_valid\nis_valid(x)']
        for name in GENERIC_NAMES:
            routes.extend(['client.' + name + '(x)', 'from other import ' + name + ' as v\nv(x)', 'result = object()\nresult.' + name + '(x)'])
        for source in routes:
            with self.subTest(source=source):
                self.assertTrue(evidence(source))

    def test_not_evidence(self):
        cases = ['import stdnum.isil', 'isil(x)', 'validate(x)', 'is_valid(x)', 'compact(x)', 'format(x)', 'validate_isil(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'obj.isil(x)', 'obj.compact(x)', 'obj.format(x)', 'from stdnum import isil\nisil.compact(x)', 'from stdnum import isil\nisil.format(x)', 'import validators\nvalidators.isil(x)', 'import re\nre.match(".*", x)', 'import re\nre.search(".*", x)', 'import re\nre.fullmatch(".*", x)', 'len(x) <= 15', 'x.split("-")[0] in agencies', '"validate isil"', '# isil validation', 'from stdnum.isil import validate\nvalidate', 'import subprocess\nsubprocess.run(["checker", x])', 'def broken(:', 'from stdnum import isil\nisil = None\nisil.validate(x)', 'from stdnum.isil import validate\nwith ctx() as validate:\n validate(x)', 'from other import validate_isil\ndef validate_isil(x): pass\nvalidate_isil(x)', 'def validate_isil(x): pass\nclient.validate_isil(x)']
        for module in ['ean', 'luhn']:
            for name in ['validate', 'calc_check_digit']:
                cases.append('from stdnum import ' + module + '\n' + module + '.' + name + '(x)')
        for module in ['isbn', 'issn', 'ismn', 'isan', 'isin']:
            cases.append('from stdnum import ' + module + '\n' + module + '.validate(x)')
        for source in cases:
            with self.subTest(source=source):
                self.assertFalse(evidence(source))

    def test_findings_and_paths(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'README.md').write_text('validate isil')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'tests').mkdir()
            (root / 'tests/test_sample.py').write_text('from stdnum import isil\nisil.validate(x)')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')
            (root / 'app.py').write_text('from stdnum import isil\nisil.validate(x)')
            self.assertEqual(audit(root), [])
            (root / 'README.md').write_text('no isil validation')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            self.assertEqual(audit(root, ['app.py']), [])
            (root / 'app.py').unlink()
            self.assertEqual(audit(root), [])
            (root / 'docs').mkdir()
            (root / 'docs/a.md').write_text('validate isil')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')

    def test_cli(self):
        with tempfile.TemporaryDirectory() as d, contextlib.redirect_stdout(io.StringIO()):
            (Path(d) / 'README.md').write_text('validate isil')
            self.assertEqual(main(['audit', d, '--json']), 2)
            self.assertEqual(main(['audit', d, '--ignore', 'README.md', '--verbose']), 0)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(main(['audit', d + '/missing']), 1)
                with self.assertRaises(SystemExit) as cm:
                    main(['audit', d, '--fail-on', 'HIGH'])
                self.assertEqual(cm.exception.code, 1)

    def test_self_audit(self):
        root = Path(__file__).resolve().parents[1]
        readme = (root / 'README.md').read_text()
        self.assertEqual(audit(root), [])
        self.assertEqual(claims(readme), (False, False))
        prose = []
        fenced = False
        for line in readme.splitlines():
            if line.startswith('```'):
                fenced = not fenced
            elif not fenced:
                prose.append(line)
        normalized = ' '.join(prose).lower().replace('-', ' ')
        for phrase in ISILVALIDATION + NOISILVALIDATION:
            with self.subTest(phrase=phrase):
                self.assertNotIn(phrase, normalized)
        self.assertNotIn('the phrase', readme)
        self.assertNotIn('a tool that', readme)


if __name__ == '__main__':
    unittest.main()

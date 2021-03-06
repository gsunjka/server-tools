# -*- coding: utf-8 -*-
# License AGPL-3: Antiun Ingenieria S.L. - Javier Iniesta
# See README.rst file on addon root folder for more details

from openerp.tests.common import TransactionCase
from openerp.exceptions import ValidationError


class TestIrExportsLineCase(TransactionCase):

    def setUp(self):
        super(TestIrExportsLineCase, self).setUp()
        m_ir_exports = self.env['ir.exports']
        self.export = m_ir_exports.create({'name': 'Partner Test',
                                           'resource': 'res.partner'})

    def test_check_name(self):
        m_ir_exports_line = self.env['ir.exports.line']
        m_ir_exports_line.create({'name': 'name',
                                  'export_id': self.export.id})
        with self.assertRaises(ValidationError):
            m_ir_exports_line.create({'name': 'name',
                                      'export_id': self.export.id})
        with self.assertRaises(ValidationError):
            m_ir_exports_line.create({'name': 'bad_error_name',
                                      'export_id': self.export.id})

    def test_get_label_string(self):
        m_ir_exports_line = self.env['ir.exports.line']
        export_line = m_ir_exports_line.create({'name': 'parent_id/name',
                                                'export_id': self.export.id})
        self.assertEqual(export_line.label,
                         "Related Company/Name (parent_id/name)")
        with self.assertRaises(ValidationError):
            m_ir_exports_line.create({'name': '',
                                      'export_id': self.export.id})

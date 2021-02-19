from odoo import api, fields, models


class TutorialXlsx(models.AbstractModel):
    _name = 'report.tutorial_module.tutorial_apps_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, docs):
        report_name = docs.name
        # One sheet by partner
        sheet = workbook.add_worksheet(report_name)
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, report_name, bold)

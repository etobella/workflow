# Copyright 2017 Creu Blanca
# Copyright 2017 Eficent Business and IT Consulting Services, S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import fields, models
from datetime import timedelta


class ActivityDefinition(models.Model):
    _inherit = 'workflow.activity.definition'

    workflow_activity_type_id = fields.Many2one(
        'mail.activity.type', domain=[]
    )
    activity_note = fields.Text()
    activity_delay = fields.Integer(default=0)

    def _get_activity_values(self, vals, parent=False, plan=False, action=False
                             ):
        values = super()._get_activity_values(vals, parent, plan, action)
        if self.model_id.model == 'mail.activity':
            values.update({
                'activity_type_id': self.workflow_activity_type_id.id,
                'name': self.name,
                'date_deadline': fields.Date.to_string(
                    fields.Date.from_string(fields.Date.today()) +
                    timedelta(days=self.activity_delay)
                ),
                'note': self.activity_note
            })
        return values

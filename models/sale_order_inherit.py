from odoo import models, fields, api


class SaleOrderIbherit(models.Model):
    _inherit = 'sale.order'


    @api.multi
    def send_mail(self):
        self.ensure.one()
        template_id = self.env.ref('send_order.email_template').id
        ctx = {
            'default_model':'sale.order',
            'default_res_id':self.id,
            'default_use_template':bool(template_id),
            'default_template_id':template_id,
            'default_composition_mode':'comment',
            'email_to':self.email,
        }
        return {
            'type':'ir.actions.act_window',
            'view_type':'form',
            'view_mode':'form',
            'res_model':'mail.compose.message',
            'target':'new',
            'conext':ctx,
        }
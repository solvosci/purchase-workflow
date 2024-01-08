# Copyright 2024 Christian Santamaria <christian.santamaria@solvos.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def message_subscribe(self, partner_ids=None, subtype_ids=None):
        partner_ids = partner_ids or []
        if (
            self._partner_disable_autofollow()
            and self.partner_id.id in partner_ids
        ):
            partner_ids.remove(self.partner_id.id)
        return super(PurchaseOrder, self).message_subscribe(partner_ids, subtype_ids)

    def _partner_disable_autofollow(self):
        return (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param(
                "purchase_order_partner_no_autofollow.partner_disable_autofollow", False
            )
        )

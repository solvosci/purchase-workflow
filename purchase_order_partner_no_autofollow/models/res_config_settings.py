# Copyright 2024 Christian Santamaria <christian.santamaria@solvos.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    purchase_partner_disable_autofollow = fields.Boolean(
        config_parameter="purchase_order_partner_no_autofollow.partner_disable_autofollow",
        string="Customer disable autofollow",
    )

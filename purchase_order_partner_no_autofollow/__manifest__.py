# Copyright 2024 Christian Santamaria <christian.santamaria@solvos.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Order Customer No Autofollow",
    "summary": "Do not add customer as follower in Purchase Orders",
    "version": "15.0.1.0.0",
    "category": "Purchases",
    "website": "https://github.com/OCA/purchase-workflow",
    "author": "Solvos, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["purchase"],
    "data": ["views/res_config_settings.xml"],
}
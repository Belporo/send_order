# -*- coding: utf-8 -*-
from odoo import http

# class ItsWebsiteHelpdeskTicket(http.Controller):
#     @http.route('/its_website_helpdesk_ticket/its_website_helpdesk_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/its_website_helpdesk_ticket/its_website_helpdesk_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('its_website_helpdesk_ticket.listing', {
#             'root': '/its_website_helpdesk_ticket/its_website_helpdesk_ticket',
#             'objects': http.request.env['its_website_helpdesk_ticket.its_website_helpdesk_ticket'].search([]),
#         })

#     @http.route('/its_website_helpdesk_ticket/its_website_helpdesk_ticket/objects/<model("its_website_helpdesk_ticket.its_website_helpdesk_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('its_website_helpdesk_ticket.object', {
#             'object': obj
#         })
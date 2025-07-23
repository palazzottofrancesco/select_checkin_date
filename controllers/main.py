# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response

class SelectCheckInController(http.Controller):

    @http.route('/hotel/booking/submit', auth='public', website=True, methods=['POST'], csrf=False)
    def hotel_booking_submit(self, **kwargs):
        # 1) Prendo i valori dal form
        ci      = kwargs.get('check_in')          # es. "2025-07-28"
        co      = kwargs.get('check_out')         # es. "2025-07-30"
        pax     = kwargs.get('guests')   or "1"    # default 1
        ch      = kwargs.get('children') or "0"    # default 0
        ch_ages = kwargs.get('children_ages', "-1")# default -1

        # 2) Endpoint
        base_url = "https://book.octorate.com/octobook/site/reservation/result.xhtml"

        # 3) Parametri richiesti dall’endpoint result.xhtml
        params = {
            "checkin":      ci,
            "children":     ch,
            "pax":          pax,
            "codice":       "302487",
            "checkout":     co,
            "childrenAges": ch_ages,
        }
        query_string = "&".join(f"{k}={v}" for k, v in params.items())

        # 4) Redirect
        redirect_url = f"{base_url}?{query_string}"
        return Response("", status=302, headers={"Location": redirect_url})
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
from urllib.parse import quote
from datetime import datetime

class SelectCheckInController(http.Controller):

    @http.route('/hotel/booking/submit', auth='public', website=True, methods=['POST'], csrf=False)
    def hotel_booking_submit(self, **kwargs):
        check_in = kwargs.get('check_in')
        check_out = kwargs.get('check_out')
        guests = kwargs.get('guests')
        children = kwargs.get('children')


        # Convertiamo le date dal formato YYYY-MM-DD al formato DD/MM/YYYY
        try:
            dt_checkin = datetime.strptime(check_in, "%Y-%m-%d")
            dt_checkout = datetime.strptime(check_out, "%Y-%m-%d")
            formatted_checkin = dt_checkin.strftime("%d/%m/%Y")
            formatted_checkout = dt_checkout.strftime("%d/%m/%Y")
        except Exception:
            formatted_checkin = check_in
            formatted_checkout = check_out

        # Impostiamo l'URL di base desiderato
        base_url = "https://book.octorate.com/octobook/site/reservation/result.xhtml"

        # Costruiamo i parametri dell'URL, assicurandoci di codificare correttamente le date e gli altri valori
        params = {
            "siteKey": "c14e7071d2f4b862e3f7d35b827dce74",
            "lang": "it",
            "ota": "false",
            "checkin": quote(formatted_checkin),
            "checkout": quote(formatted_checkout),
            "pax": quote(guests) if guests else ""
        }
        query_string = "&".join(f"{k}={v}" for k, v in params.items())
        redirect_url = f"{base_url}?{query_string}"

        # Forziamo la redirezione esterna usando Response per evitare riscritture interne
        return Response("", status=302, headers={"Location": redirect_url})

# TODO

## Medicines: cart + checkout + reliability
- [ ] Fix legacy `medicines/views.py::order()` race condition (`Order.objects.latest('id')`).
- [ ] Verify `medicines/templates/medicines/cart.html` uses `|mul` filter; ensure a `mul` template filter exists and is registered.
- [ ] (Optional) Verify cart-related context processor usage; wire if required.

## Appointments: email robustness
- [ ] Harden `appointments/views.py` email sending: broaden exception handling and optionally add debug logging.

## After code edits
- [ ] Run `python manage.py migrate`.
- [ ] Run `python manage.py runserver` and manually validate:
  - add to cart → cart total → checkout → order placed
  - appointment booking → emails don’t crash even with missing env vars


# TODO

## Medicines: cart + checkout + reliability
- [ ] Fix production crash: `relation "medicines_cart" does not exist` (ensure migrations are applied).

## Appointments: email robustness
- [ ] Harden `appointments/views.py` legacy `order()` flow.
- [ ] Harden `appointments/views.py` email sending.

## After code edits
- [ ] Run `python manage.py check`.
- [ ] Run `python manage.py migrate`.
- [ ] Run `python manage.py runserver` and manually validate:
  - add to cart → cart total → checkout → order placed
  - appointment booking → emails don’t crash even with missing env vars


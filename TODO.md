# TODO

## Medicines: cart + checkout + reliability
- [x] Identify root cause of production crash: `relation "medicines_cart" does not exist` indicates Cart table missing in deployed DB.
- [x] Add `vercel.json` to run `python manage.py migrate` during Vercel build.

- [ ] Confirm Vercel environment variable `DATABASE_URL` points to the same Neon DB where you expect tables.

- [ ] Re-test: `/medicines/add-to-cart/<id>/` then `/medicines/cart/` then checkout.

## Appointments: email robustness
- [ ] Harden `appointments/views.py` legacy `order()` flow.
- [ ] Harden `appointments/views.py` email sending.

## After code edits
- [ ] Run `python manage.py check`.
- [ ] Run `python manage.py migrate`.
- [ ] Run `python manage.py runserver` and manually validate.


# TODO

## 1) Doctors page theme fix (red → green)
- Update `chatbot/templates/chatbot/index.html` styles/variables:
  - Add missing `--black`, `--red`, `--red-dark` mappings so buttons/text show correctly.
  - Replace hardcoded red colors in UI elements with green equivalents. ✅


## 2) Home page theme fix (blue → green)
- Update `chatbot/templates/chatbot/home.html` CSS variables and gradients:
  - Switch `--secondary`/blue gradients to green palette. ✅ (partial: primary/secondary now green)



## 3) Speed slow (DB queries)
- Update `appointments/views.py`:
  - Reduce redundant DB hits:
    - compute filtered count once
  - Optimize queryset fields (use `.only(...)` for list page).

## 4) Verification
- Run server and manually check:
  - `/` home colors
  - `/appointments/` doctor page button visibility
  - Pagination/search works


- harsh gradients
- lucide icons
- pure white background
- rainbow coloring
- drop shadows
- 3 feature cards in a row
- emojis
- liquid glass
- em dashes
- inter/geist/space grotesk
- colored left stripe
- bento grids
- terminal window
- "it's not x, it's y"
- checkmark bullets
- 3 pricing tiers
- no real product demos
- soft corner radius
- purple and black palette
- no skeleton loaders
- radial orbs
- dot grids
- sparkle icons
- animated arrows
- no TOS
- no privacy policy
- hover animations
- neon colors
- basic pastel colors 

- n+1 queries  --> use a join
- missing indexes  --> add an index
- SELECT *  --> where + limit
- no pagination  --> page it
- blocking main threads. --> async + workers

## do this instead:
- Skeleton Loaders: Replace generic loading spinners with animated gray placeholder boxes that mimic your UI layout to drastically reduce perceived load times.  
* Aggressive Caching: Cache fetched data locally so returning to pages or reloading doesn't trigger redundant network requests and slow down your app.  
* Optimistic Rendering: Instantly update the UI on user actions (like toggling a button or submitting a form) before the server response confirms it, making the app feel instantaneous.  
* Helpful Tooltips: Attach clean hover tooltips to all icon-only buttons so users aren't left guessing what cryptic symbols actually do.  
* Seamless State Sync: Combine these patterns to eliminate layout shifts, flashing loaders, and sluggish responsiveness, giving your app a truly legitimate finish.

- "strong logo location" (top-left instead of top-center)
- "provide hierarchy"
- "don't use placeholder as label"
- "primary CTA should always standout"
- "don't use letter spacing unnecessarily"
- "error messages attached to the specific place it belongs" (rather than consensing them at the bottom)
- "card prices instead of radio buttons"

---
%% Sezione aggiunta da AI il 2026-10-16. Tutto il testo sopra è il tuo originale, non modificato. %%
## Collegamenti
- Indice: [[MOC Web]]
- [[some designs]]: catalogo degli stili visivi
- [[palettes]]: palette alternative al viola/nero
- [[design with AI]]: strumenti per un design meno generico
- [[on backend]]: N+1, indici, SELECT *, paginazione
- [[speed-up the website]]: stesse tecniche di performance
- [[privacy policy]]: "no privacy policy"
- [[terms and conditions]]: "no TOS"
- [[selling]]: prezzi a card e piani tariffari

> [!warning] Da verificare (nota aggiunta da AI)
> La nota mescola tre cose diverse: estetica tipica dei siti fatti con AI, errori di database e regole UX. Alcune voci sono gusti personali dell'autore del reel (hover animations, drop shadows, soft corner radius) e contraddicono strumenti salvati in [[design with AI]] (Lottie, gsap, transitions.dev).

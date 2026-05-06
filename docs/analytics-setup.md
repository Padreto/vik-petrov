# Analytics Setup Guide — ВиК Петров

## Recommended Tools

- **Google Analytics 4 (GA4)** — primary analytics
- **Google Tag Manager (GTM)** — tag management
- **Google Search Console** — SEO monitoring

---

## Step 1: Install Google Tag Manager

1. Create a GTM account at tagmanager.google.com
2. Create a new container for `vikpetrov.bg`
3. Add the GTM snippet to the site:
   - In `src/layouts/BaseLayout.astro`, add the GTM `<script>` in `<head>` and `<noscript>` after `<body>`

---

## Step 2: Connect GA4 via GTM

1. Create a GA4 property at analytics.google.com
2. Copy the Measurement ID (G-XXXXXXXXXX)
3. In GTM, create a GA4 Configuration tag with the Measurement ID
4. Fire on All Pages trigger

---

## Step 3: Event Tracking (already wired up in HTML)

All conversion-critical elements already have `data-event` attributes. Wire them in GTM:

### Calls (most important)

**Trigger:** Click — all elements — CSS selector `[data-event="call_click"]`
**Tag:** GA4 Event
- Event name: `phone_call`
- Parameters:
  - `source`: {{Click Element}} → `getAttribute('data-source')`

### Viber/Chat

**Trigger:** Click — CSS selector `[data-event="chat_click"]`
**Tag:** GA4 Event — `viber_chat`
- Parameters: `source`

### Form Submissions

**Trigger:** Click — CSS selector `[data-event="form_submit"]`  
OR better: **Thank You Page** trigger (`/uspeshno/` URL)
**Tag:** GA4 Event — `form_submission`

### CTA Button Clicks

**Trigger:** Click — CSS selector `[data-event="cta_click"]`
**Tag:** GA4 Event — `cta_click`
- Parameters: `cta_name`, `source`

---

## Step 4: Key GA4 Conversions to Mark

In GA4 → Admin → Events → Mark as conversions:
- `phone_call` ← most valuable
- `form_submission`
- `viber_chat`

---

## Step 5: Google Search Console

1. Add property: `vikpetrov.bg`
2. Verify via DNS record or HTML file
3. Submit sitemap: `https://vikpetrov.bg/sitemap-index.xml`
4. Monitor: Coverage, Core Web Vitals, Search Performance

---

## Step 6: Recommended GA4 Reports

- **Acquisition** → Which channels drive calls
- **Engagement** → Which pages have highest CTA conversion
- **Conversions** → Track phone_call and form_submission trends

---

## Event Data Layer (advanced)

The site already fires events to `window.dataLayer` when GTM is present. The code in `BaseLayout.astro` pushes:

```js
window.dataLayer.push({
  event: 'call_click',
  source: 'hero',
  cta_name: 'hero_call',
});
```

GTM can read these directly — no additional code needed.

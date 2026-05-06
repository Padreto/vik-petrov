# ВиК Петров — Website

Production-ready, SEO-optimized website for ВиК Петров — plumbing services in Sofia, Bulgaria.

Built with **Astro 6**, **Tailwind CSS**, **TypeScript**. Deploys to Netlify / Vercel / Cloudflare Pages.

## Setup

**Prerequisites:** Node.js 22+

```bash
npm install        # Install dependencies
npm run dev        # Start dev server at localhost:4321
npm run build      # Build for production to ./dist/
npm run preview    # Preview production build
```

## Configuration Before Launch

All business data is in one file — **`src/data/business.ts`**.
Search for `// TODO:` to find values needing update:

- GPS coordinates (verify exact lat/lng)
- Facebook, Instagram, Google Business URLs
- Email address confirmation

## Deploy

**Netlify:** Connect repo, build command `npm run build`, publish dir `dist`. Forms work automatically.

**Vercel:** Import repo, framework preset: Astro. For forms, use Formspree or similar.

**Cloudflare Pages:** Build command `npm run build`, output dir `dist`.

## Site Structure

- `src/data/business.ts` — single source of truth for all business data
- `src/layouts/BaseLayout.astro` — base HTML with SEO, schema, navigation
- `src/layouts/ServiceLayout.astro` — template for all 11 service pages
- `src/pages/` — all pages (homepage, services, neighborhoods, blog, etc.)
- `src/components/` — reusable components (Header, Footer, CTABlock, etc.)
- `public/` — static assets, robots.txt, llms.txt, favicon
- `docs/` — setup guides (analytics, SEO, GBP, content calendar)

## Post-Launch

See `docs/seo-checklist.md` — critical steps after going live.

Key tasks:
1. Replace photo placeholders with real photos
2. Update all TODOs in `src/data/business.ts`
3. Set up GA4 + GTM (see `docs/analytics-setup.md`)
4. Claim Google Business Profile (see `docs/local-seo-setup.md`)
5. Submit sitemap to Google Search Console

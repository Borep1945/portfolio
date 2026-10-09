# Engineering portfolio

Original responsive static portfolio for CoreVail, with six engineering project cards, category filters, keyboard access, dark/light preference, reduced-motion support, local graphics and public GitHub contact links.

## Run

```sh
python -m http.server 8765
```

Open http://127.0.0.1:8765. No external UI library, analytics, fonts or runtime dependency. The graphics are explicitly labeled architecture illustrations. Inspect the source and repositories for actual capabilities and verification limits.

## Architecture and verification

HTML defines content and semantic sections, CSS defines responsive tokens/layouts, JavaScript handles filters and theme state. CI checks local links and JS syntax, then publishes GitHub Pages. Browser checks cover desktop/mobile overflow, filter counts, theme persistence and screenshots.

## Deploy

The workflow deploys this repository to GitHub Pages through GitHub Actions. Enable Pages with build type `workflow`; see the root task publication report for the actual verified URL. Do not infer availability only from this README.

## License

MIT; original design and generated original avatar. No copied template or fabricated application screenshot. Open Source fixes are forks with their original licensing, attribution and changes.

# Abyssinia Air — Flight Results

A fictional Ethiopian airline flight-results interface created for the CodeOps Module 2 Day 14 mini-project.

The project recreates the structure of a modern airline booking/results interface using CSS Grid and Flexbox.

## Interface

Abyssinia Air — Flight Results

Route:
Addis Ababa (ADD) → Nairobi (NBO)

## How to Open

1. Clone or download the repository.
2. Open the Day14 folder.
3. Open `index.html` in a web browser.

The project can also be opened using VS Code and a local development server.

## CSS Grid

CSS Grid is used for:

- The main application page skeleton.
- Header area.
- Sidebar area.
- Main content area.
- Footer area.
- Responsive flight-card grid.

The page skeleton uses named grid areas:

- `header`
- `sidebar`
- `main`
- `footer`

The flight cards use:

`repeat(auto-fit, minmax(280px, 1fr))`

## Flexbox

Flexbox is used for:

- Main navigation.
- Page heading.
- Toolbar.
- Airline information row.
- Flight departure/arrival information.
- Flight card footer.

## Other CSS Techniques

- `position: sticky`
- `position: relative`
- `position: absolute`
- Responsive media query
- CSS custom properties
- Box sizing
- Borders
- Border radius
- Spacing
- Hover states

## Responsive Design

A single media query at `max-width: 700px` changes the application from the desktop two-column layout to a single-column mobile layout.

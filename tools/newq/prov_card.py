"""canada-quiz.com — put a province's card into the grid on driving-test.html.

Never insert a card with a plain string replace. The Saskatchewan build did that:
it added the real card and left the "Coming soon" placeholder sitting right
underneath, so the page advertised Saskatchewan twice, once as ready to practise
and once as not built yet. The owner found it on his phone.

place_card() deletes the placeholder itself and refuses to finish if the
province ends up appearing anything other than exactly once in the grid.
"""

import re

GRID_OPEN = '<div class="prov-grid">'


def _grid(html):
    i = html.index(GRID_OPEN)
    j = html.index("\n  </div>", i)
    return i, j


def count(html, name):
    """How many cards in the grid carry this <h3>?"""
    i, j = _grid(html)
    return len(re.findall(r"<h3>%s[^<]*</h3>" % re.escape(name), html[i:j]))


def drop_soon(html, name):
    """Remove the prov-soon placeholder whose <h3> matches this province."""
    pat = re.compile(
        r'\n?    <div class="card [^"]*prov-soon">\s*'
        r'(?:<div class="emoji">[^<]*</div>\s*)?'
        r'<h3>%s</h3>.*?</div>' % re.escape(name), re.S)
    out, n = pat.subn("", html)
    return out, n


def place_card(html, name, card, after_href):
    """Return html with `card` inserted after the card linking to `after_href`.

    name        the exact <h3> text of the placeholder to remove
    card        the full <div class="card …">…</div> block, already indented 4 spaces
    after_href  the previous province's practice page, so the grid stays in build order
    """
    html, dropped = drop_soon(html, name)

    anchor = 'href="%s"' % after_href
    k = html.index(anchor)
    end = html.index("</div>", html.index("</a>", k)) + len("</div>")
    html = html[:end] + "\n" + card.rstrip("\n") + html[end:]

    n = count(html, name)
    if n != 1:
        raise AssertionError(
            "%s appears %d times in the province grid (placeholder dropped: %d). "
            "It must appear exactly once." % (name, n, dropped))
    return html


def audit(html, expected_total=None):
    """Sanity-check the whole grid: no province twice, no live card without a link."""
    i, j = _grid(html)
    grid = html[i:j]
    cards = re.findall(r'<div class="card [^"]*">.*?</div>\s*</div>', grid, re.S)
    cards = re.split(r'\n    (?=<div class="card )', grid)[1:]
    problems = []
    titles = []
    for c in cards:
        m = re.search(r"<h3>(.*?)</h3>", c)
        if not m:
            problems.append("card with no <h3>")
            continue
        titles.append(m.group(1))
        soon = "prov-soon" in c.split(">", 1)[0]
        if not soon and "<a class=\"btn" not in c:
            problems.append("live card with no link: " + m.group(1))
        if soon and "<a class=\"btn" in c:
            problems.append("coming-soon card that links somewhere: " + m.group(1))
    dupes = {t for t in titles if titles.count(t) > 1}
    if dupes:
        problems.append("province listed more than once: " + ", ".join(sorted(dupes)))
    if expected_total is not None and len(titles) != expected_total:
        problems.append("expected %d cards, found %d" % (expected_total, len(titles)))
    return titles, problems

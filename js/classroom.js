/* canada-quiz.com — "Share to Google Classroom", on school pages only.

   Added 20 October 2026. Teachers already post our pages in Google Classroom
   for their classes. A teacher who wants to set one of our
   pages as class work had to copy the address by hand. This puts one button
   under the page title that opens Classroom's own "share" screen with the page
   already filled in; the teacher picks the class and the assignment there.

   Only the school pages load this script (grade quizzes, the teachers' page,
   printables, the kids' true stories, the learning quizzes). Driving tests,
   citizenship and the games do not load it.

   It is a plain link to Google's documented share address
   (classroom.google.com/share?url=...). No Google script is loaded, nothing is
   sent anywhere until the teacher clicks, and then only the page address and
   its title. The words are picked by the same URL test the rest of the site
   uses, so the French pages need no dictionary entry. */
(function () {
  "use strict";

  var FR = /(^|\/)fr\//.test(location.pathname);
  var LABEL = FR ? "Partager dans Google Classroom" : "Share to Google Classroom";
  var HINT = FR ? "Pour les enseignants : donnez cette page à votre classe."
                : "For teachers: give this page to your class.";

  function pageUrl() {
    var c = document.querySelector('link[rel="canonical"]');
    var u = (c && c.href) || (location.origin + location.pathname);
    return u.split("#")[0];
  }

  function pageTitle() {
    return (document.title || "Canada Quiz")
      .replace(/\s*[|—-]\s*Canada Quiz.*$/, "").trim() || "Canada Quiz";
  }

  var css = ""
    + ".cq-classroom{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px 12px;margin:10px 0 4px}"
    + ".cq-classroom a{display:inline-flex;align-items:center;gap:9px;background:#1e7e34;color:#fff;"
    + "border-radius:999px;padding:10px 18px;font-weight:700;font-size:15px;line-height:1.2;text-decoration:none;"
    + "box-shadow:0 2px 8px rgba(0,0,0,.18)}"
    + ".cq-classroom a:hover,.cq-classroom a:focus{background:#176328;color:#fff;text-decoration:none}"
    + ".cq-classroom a:focus-visible{outline:3px solid #ffbf47;outline-offset:2px}"
    + ".cq-classroom svg{flex:none}"
    + ".cq-classroom small{color:inherit;opacity:.75;font-size:13px}"
    + "@media print{.cq-classroom{display:none}}";

  function icon() {
    /* a small chalkboard with a person in front of it: our own drawing */
    return '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
      + '<rect x="2" y="3" width="20" height="13" rx="2" fill="#fff"/>'
      + '<rect x="4" y="5" width="16" height="9" rx="1" fill="#1e7e34"/>'
      + '<circle cx="12" cy="17.5" r="2.2" fill="#fff"/>'
      + '<path d="M7.5 23c.6-2.6 2.3-3.8 4.5-3.8s3.9 1.2 4.5 3.8z" fill="#fff"/></svg>';
  }

  function track() {
    try {
      if (typeof window.gtag === "function") {
        window.gtag("event", "classroom_share", { page_location: location.href });
      }
    } catch (e) { /* analytics must never break a link */ }
  }

  function add() {
    var h1 = document.querySelector("main h1");
    if (!h1 || document.querySelector(".cq-classroom")) return;
    var box = h1.closest("section") || h1.parentNode;

    var st = document.createElement("style");
    st.textContent = css;
    document.head.appendChild(st);

    var row = document.createElement("div");
    row.className = "cq-classroom";
    var a = document.createElement("a");
    a.href = "https://classroom.google.com/share?url=" + encodeURIComponent(pageUrl())
      + "&title=" + encodeURIComponent(pageTitle());
    a.target = "_blank";
    a.rel = "noopener";
    a.innerHTML = icon() + "<span></span>";
    a.lastChild.textContent = LABEL;
    a.addEventListener("click", track);
    var s = document.createElement("small");
    s.textContent = HINT;
    row.appendChild(a);
    row.appendChild(s);
    box.appendChild(row);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", add);
  } else {
    add();
  }
})();

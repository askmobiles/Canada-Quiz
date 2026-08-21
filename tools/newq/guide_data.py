"""canada-quiz.com — what each government actually publishes about its written test.

This is the single place where the verified facts live. It exists because the
worst thing this site can do is print a pass mark that is wrong: these pages are
read by people deciding whether to book a real government exam.

Two rules govern every entry:

  1. Only what an official source states. The provincial or territorial
     registry, insurer or transport department, and nothing else. Practice
     sites, tire retailers and forums are not sources.
  2. Where a government publishes nothing, the value is None and the page says
     so in plain words. Six of the thirteen publish no question count at all —
     including Ontario. Saying so is a feature, not a gap.

`checked` is the date a human or an agent last read the official page. Anything
older than a few months should be re-read before it is quoted, and fees should
never be published as if they were permanent.

Fields
------
name        English and French
body        the registry / insurer / department that runs the test
licence     the learner licence, in that jurisdiction's own words
questions   number of questions on the real test, or None if not published
pass        pass mark as published, or None
minutes     time limit as published, or None
split       how the test is divided, as published
age         youngest age for the learner licence
stage1      how long the learner stage lasts
novice_pts  demerit points that suspend a new driver
handbook    the free official handbook, EN/FR
urls        where those facts were read
notes       the one thing that catches people out
"""

CHECKED = "2026-08-20"

JURISDICTIONS = {
    "on": dict(
        name=("Ontario", "Ontario"), body="Ministry of Transportation / DriveTest",
        licence="G1", questions=None, pass_mark="80% overall", minutes=None,
        split="two or three sections; you rewrite only the sections you failed",
        age=16, stage1="12 months, or 8 with an approved driving course", novice_pts=9,
        handbook=("Official MTO Driver's Handbook", "Guide officiel de l'automobiliste"),
        page="ontario-g1-practice-test.html",
        notes="Neither ontario.ca nor DriveTest publishes a question count, though almost every practice site prints one.",
    ),
    "bc": dict(
        name=("British Columbia", "Colombie-Britannique"), body="ICBC",
        licence="Class 7L", questions=50, pass_mark="40 of 50", minutes=45,
        split="one test", age=16, stage1="12 months, or 9 with a recognised course", novice_pts=4,
        handbook=("Learn to Drive Smart", "Tuning Up for Drivers"),
        page="bc-class-7l-practice-test.html",
        notes="Supervisor age changes from 25 to 22 on 19 October 2026 — update the bc-* pages then.",
    ),
    "ab": dict(
        name=("Alberta", "Alberta"), body="Government of Alberta",
        licence="Class 7", questions=30, pass_mark="25 of 30", minutes=None,
        split="one test, scored overall", age=14, stage1="12 months", novice_pts=8,
        handbook=("Alberta Basic Licence Driver's Guide", "Alberta Basic Licence Driver's Guide"),
        page="alberta-class-7-practice-test.html",
        notes="Scored across the whole test rather than half by half.",
    ),
    "qc": dict(
        name=("Quebec", "Québec"), body="SAAQ",
        licence="Class 5 learner's licence", questions=None, pass_mark="75% in EACH section",
        minutes=None, split="three sections; you retake only the sections you failed",
        age=16, stage1="10 months before the knowledge test, 12 before the road test", novice_pts=4,
        handbook=("Driver's Handbook", "Guide de la route"),
        page="quebec-class-5-practice-test.html",
        notes="SAAQ publishes the 75 percent but not the number of questions. A driving course is mandatory.",
    ),
    "mb": dict(
        name=("Manitoba", "Manitoba"), body="Manitoba Public Insurance",
        licence="Class 5 Learner", questions=None, pass_mark=None, minutes=30,
        split="one test", age=16, stage1="9 months", novice_pts=None,
        handbook=("Manitoba Driver's Handbook", "Manitoba Driver's Handbook"),
        page="manitoba-class-5-practice-test.html",
        notes="MPI publishes the 30-minute limit but neither a question count nor a pass mark.",
    ),
    "sk": dict(
        name=("Saskatchewan", "Saskatchewan"), body="SGI",
        licence="Class 7", questions=None, pass_mark=None, minutes=None,
        split="two tests, Basic and Sign; you rewrite only the one you failed",
        age=16, stage1="9 months, or 6 with driver education", novice_pts=4,
        handbook=("Saskatchewan Driver's Handbook", "Saskatchewan Driver's Handbook"),
        page="saskatchewan-class-7-practice-test.html",
        notes="SGI publishes neither a question count nor a pass mark nor a time limit.",
    ),
    "ns": dict(
        name=("Nova Scotia", "Nouvelle-Écosse"), body="Access Nova Scotia / Registry of Motor Vehicles",
        licence="Class 7", questions=40, pass_mark="16 of 20 in EACH test", minutes=30,
        split="two tests of 20: Rules of the Road, and Road Sign Recognition",
        age=16, stage1="12 months, or 9 with an approved course", novice_pts=4,
        handbook=("Nova Scotia Driver's Handbook", "Nova Scotia Driver's Handbook"),
        page="nova-scotia-class-7-practice-test.html",
        notes="Publishes the whole format. The school-bus rule has no median exception, and zero alcohol applies through all three stages.",
    ),
    "nb": dict(
        name=("New Brunswick", "Nouveau-Brunswick"), body="Service New Brunswick",
        licence="Class 7 Level 1", questions=None, pass_mark=None, minutes=30,
        split="two written exams", age=16, stage1="12 months, or 8 with a recognised driving school",
        novice_pts=None,
        handbook=("New Brunswick Driver's Handbook", "Manuel du conducteur pour le Nouveau-Brunswick"),
        page="new-brunswick-class-7-practice-test.html",
        notes="First province in Canada to put the written test online (2020). Publishes no question count and no pass mark.",
    ),
    "nl": dict(
        name=("Newfoundland and Labrador", "Terre-Neuve-et-Labrador"),
        body="Motor Registration Division",
        licence="Class 5 Level I", questions=None, pass_mark="85%", minutes=None,
        split="one exam covering rules, safe driving and sign recognition",
        age=16, stage1="12 months, or 8 with an approved Driver Education Program", novice_pts=6,
        handbook=("Driver's Handbook", "Manuel du conducteur"),
        page="newfoundland-class-5-practice-test.html",
        urls=["https://www.gov.nl.ca/motorregistration/new-drivers/written-tests/",
              "https://www.gov.nl.ca/motorregistration/new-drivers/graduated-driver-licencing-program/",
              "https://www.gov.nl.ca/motorregistration/new-drivers/road-user-guide/",
              "https://www.gov.nl.ca/ti/roads/department/moose/"],
        notes=("85 percent is published in three places; the question count and time limit are not published "
               "anywhere. Default limits: 100 paved Trans-Canada, 80 other paved, 60 gravel, 50 through a "
               "community and in an unmarked school zone. Written test offered in French and Ukrainian in person."),
    ),
    "pe": dict(
        name=("Prince Edward Island", "Île-du-Prince-Édouard"), body="Access PEI / Highway Safety Division",
        licence="Class 7 Instruction Permit", questions=None, pass_mark=None, minutes=None,
        split="not published", age=16,
        stage1="365 days, or 275 with certified driver education", novice_pts=0,
        handbook=("Driver's Handbook", "Guide du conducteur"),
        page="pei-class-7-practice-test.html",
        urls=["https://www.princeedwardisland.ca/en/information/transportation-and-infrastructure/getting-an-instruction-drivers-permit-in-pei",
              "https://www.princeedwardisland.ca/en/information/transportation-and-infrastructure/graduated-driver-licensing-program-gdl",
              "https://www.princeedwardisland.ca/en/information/transportation-and-infrastructure/rules-of-the-road",
              "https://www.princeedwardisland.ca/en/publication/drivers-handbook"],
        notes=("ANY demerit points at all suspend a Stage 1 permit for at least 30 days. The learner must be at "
               "zero alcohol while the accompanying driver must be under 0.05 — two different published limits. "
               "Open highway 80, maximum posted 90: the Island has no 100 km/h highway. Seven days before "
               "rewriting the written exam, fourteen before a second road test."),
    ),
    "yt": dict(
        name=("Yukon", "Yukon"), body="Yukon Motor Vehicles (Highways and Public Works)",
        licence="Class 7 Learner", questions=None, pass_mark="80%, every licence class", minutes=None,
        split="ONE combined written and sign recognition test", age=15,
        stage1="6 months and 50 logged driving hours", novice_pts=7,
        handbook=("Yukon Driver's Basic Handbook", "Guide de la route du Yukon"),
        page="yukon-class-7-practice-test.html",
        urls=["https://yukon.ca/en/driving-and-transportation/driver-licensing/get-drivers-licence",
              "https://laws.yukon.ca/cms/images/LEGISLATION/regs/co1978_120.pdf",
              "https://yukon.ca/en/licence-suspensions",
              "https://yukon.ca/en/driving-permafrost-affected-roads"],
        notes=("The 80 percent is in the Motor Vehicles Regulations and applies to every class. Hands-free is "
               "banned for learners and novices, not only hand-held. Daytime low beams are the law if the "
               "vehicle has no daytime running lights. A GDL violation restarts the clock."),
    ),
    "nt": dict(
        name=("Northwest Territories", "Territoires du Nord-Ouest"),
        body="Driver and Vehicle Services (Department of Infrastructure)",
        licence="Class 7 Learner", questions=40, pass_mark="16 of 20 in EACH test", minutes=30,
        split="two separate tests of 20: rules of the road, and road signage",
        age=15, stage1="12 months", novice_pts=6,
        handbook=("NWT Basic Driver's Manual", "Manuel du conducteur"),
        page="nwt-class-7-practice-test.html",
        urls=["https://www.idmv.inf.gov.nt.ca/Drivers/Drivers/Book-cancel-or-rebook-a-written-or-practical-examination",
              "https://www.idmv.inf.gov.nt.ca/Drivers/Drivers/Get-a-drivers-licence-for-the-first-time",
              "https://www.inf.gov.nt.ca/en/BisonSafety",
              "https://www.inf.gov.nt.ca/en/services/highways-ferries-and-winter-roads/winter-driving"],
        notes=("Publishes the whole format: 'You may not miss more than four questions in each test.' The wording "
               "'the test lasts 30 minutes' is singular and does not say whether that is per test or for both, so "
               "we claim neither. Headlights on at all times is the law. Both driver and supervisor at zero alcohol. "
               "The official examination fee page currently shows two contradicting tables — quote neither."),
    ),
    "nu": dict(
        name=("Nunavut", "Nunavut"),
        body="Motor Vehicles Division (Economic Development and Transportation)",
        licence="Class 7", questions=None, pass_mark=None, minutes=None,
        split="two parts at one sitting; you rewrite only the part you failed",
        age=15, stage1=None, novice_pts=None,
        handbook=("Nunavut Driver's Manual", "Nunavut Driver's Manual"),
        page="nunavut-class-7-practice-test.html",
        urls=["https://www.gov.nu.ca/en/service-nunavut/drivers-manuals",
              "https://www.gov.nu.ca/sites/default/files/documents/2022-12/driversmanual_eng.pdf"],
        notes=("Publishes less than any other jurisdiction: no question count, no pass mark, no time limit, no fee, "
               "and NO graduated licensing programme at all. There are no road markings anywhere in Nunavut. "
               "50 km/h inside communities, 90 outside. Three Motor Vehicles Offices, plus Government Liaison "
               "Officers in all 25 communities. The manuals are published in English only."),
    ),
}


def not_published(field):
    """Which jurisdictions publish nothing for this field — the honest answer."""
    return [k for k, v in JURISDICTIONS.items() if v.get(field) in (None, "not published")]


if __name__ == "__main__":
    print("checked", CHECKED, "-", len(JURISDICTIONS), "jurisdictions")
    for f in ("questions", "pass_mark", "minutes"):
        miss = not_published(f)
        print("  %-10s not published by %d: %s" % (f, len(miss), ", ".join(miss)))

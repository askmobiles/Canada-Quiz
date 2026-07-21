/* Canada Citizenship Practice — starter question bank
   Based on the official "Discover Canada" study guide themes.
   UNOFFICIAL practice questions. Review for accuracy before launch.
   Format: { q, options:[...], answer:index, explain, chapter }
*/
const CITIZENSHIP_QUESTIONS = [
  {
    q: "How many correct answers do you need to pass the real Canadian citizenship test?",
    options: ["10 out of 20", "15 out of 20", "18 out of 20", "20 out of 20"],
    answer: 1,
    explain: "The real test has 20 questions and you must get at least 15 correct (75%) to pass.",
    chapter: "About the Test"
  },
  {
    q: "What is the capital city of Canada?",
    options: ["Toronto", "Vancouver", "Ottawa", "Montreal"],
    answer: 2,
    explain: "Ottawa, in Ontario, is the capital of Canada.",
    chapter: "Canada's Regions"
  },
  {
    q: "Who was the first Prime Minister of Canada?",
    options: ["Sir John A. Macdonald", "Sir Wilfrid Laurier", "Sir George-Étienne Cartier", "William Lyon Mackenzie King"],
    answer: 0,
    explain: "Sir John A. Macdonald was Canada's first Prime Minister. His image is on the $10 bill.",
    chapter: "Canada's History"
  },
  {
    q: "What are the two official languages of Canada?",
    options: ["English and Spanish", "English and French", "French and German", "English and Italian"],
    answer: 1,
    explain: "Canada has two official languages: English and French.",
    chapter: "Modern Canada"
  },
  {
    q: "On what date did Canada become a country (Confederation)?",
    options: ["July 1, 1867", "July 4, 1776", "January 1, 1900", "November 11, 1918"],
    answer: 0,
    explain: "Canada became a country on July 1, 1867. We celebrate this every year as Canada Day.",
    chapter: "Canada's History"
  },
  {
    q: "How many provinces and territories does Canada have?",
    options: ["10 provinces and 3 territories", "12 provinces and 2 territories", "8 provinces and 3 territories", "10 provinces and 5 territories"],
    answer: 0,
    explain: "Canada has 10 provinces and 3 territories.",
    chapter: "Canada's Regions"
  },
  {
    q: "Who is Canada's Head of State?",
    options: ["The Prime Minister", "The Governor General", "The Sovereign (currently King Charles III)", "The President"],
    answer: 2,
    explain: "Canada's Head of State is the Sovereign — currently King Charles III. The Governor General represents the King in Canada.",
    chapter: "How Canadians Govern Themselves"
  },
  {
    q: "Who is Canada's Head of Government?",
    options: ["The King", "The Prime Minister", "The Governor General", "The Chief Justice"],
    answer: 1,
    explain: "The Prime Minister is the Head of Government and runs the day-to-day government of Canada.",
    chapter: "How Canadians Govern Themselves"
  },
  {
    q: "What are the three parts of Parliament?",
    options: ["The King, the Senate, and the House of Commons", "The Prime Minister, the courts, and the police", "The provinces, the cities, and the towns", "The Army, the Navy, and the Air Force"],
    answer: 0,
    explain: "Parliament has three parts: the Sovereign (King or Queen), the Senate, and the House of Commons.",
    chapter: "How Canadians Govern Themselves"
  },
  {
    q: "What is Canada's national winter sport?",
    options: ["Curling", "Ice hockey", "Skiing", "Snowboarding"],
    answer: 1,
    explain: "Ice hockey is Canada's national winter sport. Lacrosse is the national summer sport.",
    chapter: "Canadian Symbols"
  },
  {
    q: "What is the name of Canada's national police force?",
    options: ["The FBI", "The Royal Canadian Mounted Police (RCMP)", "The Canadian Guard", "The National Police Service"],
    answer: 1,
    explain: "The Royal Canadian Mounted Police (RCMP), also called 'the Mounties', is Canada's national police force.",
    chapter: "Canadian Symbols"
  },
  {
    q: "What is the title of Canada's national anthem?",
    options: ["God Save the King", "The Maple Leaf Forever", "O Canada", "True North"],
    answer: 2,
    explain: "'O Canada' is Canada's national anthem. It was proclaimed the official anthem in 1980.",
    chapter: "Canadian Symbols"
  },
  {
    q: "Which document sets out the rights and freedoms of people in Canada?",
    options: ["The Magna Carta", "The Canadian Charter of Rights and Freedoms", "The Declaration of Independence", "The Bill of Sale"],
    answer: 1,
    explain: "The Canadian Charter of Rights and Freedoms (1982) sets out the basic rights and freedoms of everyone in Canada.",
    chapter: "Rights and Responsibilities"
  },
  {
    q: "What do we celebrate on July 1st?",
    options: ["Remembrance Day", "Canada Day", "Victoria Day", "Labour Day"],
    answer: 1,
    explain: "July 1st is Canada Day, celebrating the day Canada became a country in 1867.",
    chapter: "Canadian Symbols"
  },
  {
    q: "What do we remember on November 11th (Remembrance Day)?",
    options: ["The men and women who served and died for Canada", "The first Prime Minister", "The founding of Ottawa", "The end of winter"],
    answer: 0,
    explain: "On Remembrance Day we honour the sacrifice of Canadians who served and died in wars. Many people wear a red poppy.",
    chapter: "Canada's History"
  },
  {
    q: "How old must you be to vote in a Canadian federal election?",
    options: ["16 years old", "18 years old", "19 years old", "21 years old"],
    answer: 1,
    explain: "You must be a Canadian citizen and at least 18 years old on voting day to vote in a federal election.",
    chapter: "Federal Elections"
  },
  {
    q: "Which three groups are the Aboriginal (Indigenous) peoples of Canada?",
    options: ["First Nations, Métis, and Inuit", "English, French, and Irish", "North, South, and Central", "Farmers, fishers, and miners"],
    answer: 0,
    explain: "The Aboriginal peoples of Canada are the First Nations, the Métis, and the Inuit.",
    chapter: "Canada's History"
  },
  {
    q: "What animal is an official symbol (emblem) of Canada?",
    options: ["The lion", "The eagle", "The beaver", "The kangaroo"],
    answer: 2,
    explain: "The beaver is an official emblem of Canada and appears on the five-cent coin (nickel).",
    chapter: "Canadian Symbols"
  },
  {
    q: "Which ocean is on the WEST coast of Canada?",
    options: ["The Atlantic Ocean", "The Pacific Ocean", "The Arctic Ocean", "The Indian Ocean"],
    answer: 1,
    explain: "The Pacific Ocean is on Canada's west coast (British Columbia). The Atlantic is on the east and the Arctic is to the north.",
    chapter: "Canada's Regions"
  },
  {
    q: "Which three provinces are known as the Prairie provinces?",
    options: ["Ontario, Quebec, and Nova Scotia", "Manitoba, Saskatchewan, and Alberta", "B.C., Yukon, and Alberta", "New Brunswick, P.E.I., and Nova Scotia"],
    answer: 1,
    explain: "The Prairie provinces are Manitoba, Saskatchewan, and Alberta.",
    chapter: "Canada's Regions"
  },
  {
    q: "What is the population of Canada, approximately?",
    options: ["About 3 million", "About 40 million", "About 100 million", "About 300 million"],
    answer: 1,
    explain: "Canada's population is roughly 40 million people, making it one of the least crowded countries by land area.",
    chapter: "Modern Canada"
  },
  {
    q: "Canada is the ____ largest country in the world by total area.",
    options: ["First", "Second", "Fifth", "Tenth"],
    answer: 1,
    explain: "Canada is the second largest country in the world by total area, after Russia.",
    chapter: "Canada's Regions"
  },
  {
    q: "Which province is mostly French-speaking?",
    options: ["Ontario", "Quebec", "Alberta", "Manitoba"],
    answer: 1,
    explain: "Quebec is the only province where most people speak French as their first language.",
    chapter: "Canada's Regions"
  },
  {
    q: "What was the last province to join Canada?",
    options: ["British Columbia", "Alberta", "Newfoundland and Labrador", "Manitoba"],
    answer: 2,
    explain: "Newfoundland and Labrador was the last province to join Canada, in 1949.",
    chapter: "Canada's History"
  },
  {
    q: "How often must a federal election be held (at the latest)?",
    options: ["Every year", "At least every four years", "Every ten years", "Only when the King decides"],
    answer: 1,
    explain: "By law, a federal election must be held at least every four years.",
    chapter: "Federal Elections"
  },
  {
    q: "Who represents the King (the Sovereign) in Canada at the federal level?",
    options: ["The Prime Minister", "The Governor General", "The Mayor", "The Chief Justice"],
    answer: 1,
    explain: "The Governor General represents the Sovereign at the federal level in Canada.",
    chapter: "How Canadians Govern Themselves"
  },
  {
    q: "What are the four Atlantic provinces?",
    options: ["Nova Scotia, New Brunswick, P.E.I., Newfoundland and Labrador", "Ontario, Quebec, Manitoba, Alberta", "B.C., Alberta, Saskatchewan, Manitoba", "Yukon, Nunavut, N.W.T., B.C."],
    answer: 0,
    explain: "The Atlantic provinces are Nova Scotia, New Brunswick, Prince Edward Island, and Newfoundland and Labrador.",
    chapter: "Canada's Regions"
  },
  {
    q: "What is the national summer sport of Canada?",
    options: ["Baseball", "Soccer", "Lacrosse", "Cricket"],
    answer: 2,
    explain: "Lacrosse is Canada's national summer sport, and ice hockey is the national winter sport.",
    chapter: "Canadian Symbols"
  },
  {
    q: "In Canada, who has the right to vote and run for office?",
    options: ["Only people born in Canada", "Canadian citizens", "Only property owners", "Only people over 30"],
    answer: 1,
    explain: "Canadian citizens aged 18 or older have the right to vote and to run for office in elections.",
    chapter: "Rights and Responsibilities"
  },
  {
    q: "What is a responsibility of Canadian citizenship?",
    options: ["Obeying the law", "Never leaving Canada", "Paying no taxes", "Joining a political party"],
    answer: 0,
    explain: "Obeying the law is a key responsibility. Others include serving on a jury, voting, and helping others in the community.",
    chapter: "Rights and Responsibilities"
  },
  {
    q: "Which war took place partly in Canada in the years 1812–1814?",
    options: ["World War I", "The War of 1812", "The Seven Years' War", "The Cold War"],
    answer: 1,
    explain: "In the War of 1812, the United States invaded Canada, but the invasion was defeated. This helped shape the border we have today.",
    chapter: "Canada's History"
  },
  {
    q: "The 1917 Battle of Vimy Ridge is remembered as an important moment for Canada during which war?",
    options: ["The War of 1812", "The First World War", "The Second World War", "The Korean War"],
    answer: 1,
    explain: "Canadian troops captured Vimy Ridge in 1917 during the First World War. It is seen as a proud national moment.",
    chapter: "Canada's History"
  },
  {
    q: "What colour(s) is the Canadian flag?",
    options: ["Red and white", "Blue and white", "Red, white, and blue", "Green and gold"],
    answer: 0,
    explain: "The Canadian flag is red and white with a single red maple leaf in the centre. It was first raised in 1965.",
    chapter: "Canadian Symbols"
  },
  {
    q: "Which level of government is responsible for national defence and citizenship?",
    options: ["The city (municipal) government", "The provincial government", "The federal government", "The school board"],
    answer: 2,
    explain: "The federal government is responsible for things like national defence, citizenship, and foreign policy.",
    chapter: "How Canadians Govern Themselves"
  },
  {
    q: "Who do Canadians elect to represent them in the House of Commons?",
    options: ["Senators", "Members of Parliament (MPs)", "Judges", "Governors"],
    answer: 1,
    explain: "Canadians vote to elect Members of Parliament (MPs) to represent them in the House of Commons.",
    chapter: "Federal Elections"
  },
  {
    q: "What is the名 name given to the first European and Aboriginal peoples who worked together in the early fur trade?",
    options: ["The Loyalists", "The Voyageurs and their partners", "The Vikings", "The Pilgrims"],
    answer: 1,
    explain: "French fur traders (voyageurs) and First Nations partners built the early fur trade, one of Canada's first industries.",
    chapter: "Canada's History"
  },
  {
    q: "What is the meaning of the poppy that many Canadians wear in November?",
    options: ["It celebrates spring", "It remembers those who died in war", "It is a symbol of hockey", "It marks Canada Day"],
    answer: 1,
    explain: "The red poppy is worn to remember Canadians who died serving in wars, inspired by the poem 'In Flanders Fields'.",
    chapter: "Canada's History"
  },
  {
    q: "Which famous Canadian ran the 'Marathon of Hope' to raise money for cancer research?",
    options: ["Wayne Gretzky", "Terry Fox", "Sir John A. Macdonald", "Alexander Graham Bell"],
    answer: 1,
    explain: "Terry Fox, who lost a leg to cancer, ran the Marathon of Hope in 1980 and became a national hero.",
    chapter: "Modern Canada"
  },
  {
    q: "What are the three territories of Canada?",
    options: ["Yukon, Northwest Territories, and Nunavut", "Ontario, Quebec, and Alberta", "Yukon, Alberta, and Manitoba", "Nunavut, Labrador, and Yukon"],
    answer: 0,
    explain: "Canada's three territories are Yukon, the Northwest Territories, and Nunavut, all in the North.",
    chapter: "Canada's Regions"
  },
  {
    q: "Where does the Prime Minister and Cabinet get the authority to govern?",
    options: ["From winning the support of the elected House of Commons", "From the King alone", "From the courts", "From the newspapers"],
    answer: 0,
    explain: "In Canada's system of responsible government, the government must have the confidence (support) of the elected House of Commons.",
    chapter: "How Canadians Govern Themselves"
  },
  {
    q: "What is one thing Canada is known for producing and exporting?",
    options: ["Oil, gas, grain, and minerals", "Only bananas", "Only cars", "Nothing at all"],
    answer: 0,
    explain: "Canada has a strong economy based on natural resources such as oil, gas, grain, lumber, and minerals, plus services and manufacturing.",
    chapter: "Canada's Economy"
  },
  {
    q: "The maple leaf is a symbol of Canada. Where can you see it?",
    options: ["Only on the flag", "On the flag, coins, and the coat of arms", "Nowhere official", "Only in Quebec"],
    answer: 1,
    explain: "The maple leaf appears on the national flag, on coins (like the penny of the past), and on the Canadian coat of arms.",
    chapter: "Canadian Symbols"
  },
  {
    q: "Which country shares the longest border with Canada?",
    options: ["Russia", "The United States", "Mexico", "Greenland"],
    answer: 1,
    explain: "Canada shares the longest border in the world with the United States to the south.",
    chapter: "Canada's Regions"
  }
];

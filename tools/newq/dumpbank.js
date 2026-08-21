/* canada-quiz.com — dump one province question bank as JSON.
   Usage:  node tools/newq/dumpbank.js nl
   Prints {questions:[...], province:{...}, signs:{key:svg}, meta:{key:{cat,en,fr}}}
   so the Python build tools never have to parse JavaScript by hand. */
const path = require('path');
const root = path.resolve(__dirname, '..', '..');
const code = process.argv[2];
if (!code) { console.error('usage: dumpbank.js <code>'); process.exit(2); }

global.window = {};
require(path.join(root, 'js', 'driving', 'signs.js'));
require(path.join(root, 'js', 'driving', code + '.js'));

if (!global.window.CQ_PROVINCE) {
  console.error('js/driving/' + code + '.js sets no window.CQ_PROVINCE — the pages would render nothing.');
  process.exit(1);
}

process.stdout.write(JSON.stringify({
  questions: global.window.CQ_DRIVE_Q,
  province: global.window.CQ_PROVINCE,
  signs: global.window.CQ_SIGNS,
  meta: global.window.CQ_SIGN_META
}));

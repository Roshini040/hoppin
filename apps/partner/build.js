const fs = require('fs');
const path = require('path');

const candidates = [
  path.resolve(__dirname, '../web/index.html'),
  path.resolve(__dirname, '../../apps/web/index.html'),
  path.resolve(__dirname, 'index.html'),
];

let src = candidates.find(c => fs.existsSync(c));
const distDir = path.resolve(__dirname, 'dist');
fs.mkdirSync(distDir, { recursive: true });

if (src) {
  fs.copyFileSync(src, path.join(distDir, 'index.html'));
  console.log('Successfully generated dist/index.html in apps/admin from', src);
} else {
  fs.writeFileSync(path.join(distDir, 'index.html'), '<!doctype html><html><body><h1>Hoppin Ready</h1></body></html>');
}

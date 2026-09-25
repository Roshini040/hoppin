const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

console.log('[build] Building apps/web production bundle...');
execSync('npm --prefix apps/web run build', { stdio: 'inherit' });

const srcDist = path.resolve(__dirname, 'apps/web/dist');
const rootDist = path.resolve(__dirname, 'dist');

if (fs.existsSync(srcDist)) {
  fs.mkdirSync(rootDist, { recursive: true });
  const files = fs.readdirSync(srcDist);
  for (const f of files) {
    const s = path.join(srcDist, f);
    const d = path.join(rootDist, f);
    if (fs.statSync(s).isDirectory()) {
      fs.cpSync(s, d, { recursive: true });
    } else {
      fs.copyFileSync(s, d);
    }
  }
  console.log('[build] Successfully synced build to root ./dist and ./apps/web/dist');
}

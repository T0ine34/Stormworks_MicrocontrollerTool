const glob = require('glob');
const fs = require('fs');
const path = require('path');

// copy all html and js files from src to dist
glob.sync('src/**/*.+(html|js)').forEach(file => {
    const dist = file.replace('src', 'dist');       // replace src with dist
    fs.mkdirSync(path.dirname(dist), { recursive: true });  // create parent directories
    fs.copyFileSync(file, dist);                            // copy file
    console.log(`Copied ${file} to ${dist}`);
});

console.log('Build complete!');
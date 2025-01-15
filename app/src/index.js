document.getElementById('openFileButton').addEventListener('click', async () => {
    const filePaths = await window.file.open();
});

document.getElementById('newFileButton').addEventListener('click', async () => {
    // ask if the user wants to save the file
    if (confirm('Do you want to save the file?')) {
        const filePath = await window.file.save();
    }

    // clear the editor
});

document.getElementById('saveFileButton').addEventListener('click', async () => {
    // const filePath = await window.file.save(); // get a file path only if we don't have one (new file)
});

document.getElementById('saveAsFileButton').addEventListener('click', async () => {
    const filePath = await window.file.save();
});



async function onClose (){
    // ask if the user wants to save the file
    if (confirm('Do you want to save the file?')) {
        const filePath = await window.file.save();
    }

    // clear the editor
}

document.getElementById('closeFileButton').addEventListener('click', onClose);


const canvas = document.querySelector('#canvas');
const ctx = canvas.getContext('2d');

// draw a grid
ctx.beginPath();
for (let i = 1; i < canvas.width; i += 50) {
    ctx.moveTo(i, 0);
    ctx.lineTo(i, canvas.height);
}
for (let i = 1; i < canvas.height; i += 50) {
    ctx.moveTo(0, i);
    ctx.lineTo(canvas.width, i);
}
ctx.strokeStyle = '#ddd';
ctx.stroke();

// handle zoom using the mouse wheel
let scale = 1;
const MAX_SCALE = 2;
const MIN_SCALE = 0.1;

let isPanning = false;
let clickedX = 0;
let clickedY = 0;
let currentX = -1280;
let currentY = -1280;

const MAX_X = 0;
const MAX_Y = 0;
const MIN_X = -2560;
const MIN_Y = -2560;



canvas.style.transform = `scale(${scale}) translate(${currentX}px, ${currentY}px)`;

document.addEventListener('wheel', (e) => {
    e.preventDefault();
    console.log(e.deltaY);
    scale += e.deltaY * -0.001;
    scale = Math.min(Math.max(MIN_SCALE, scale), MAX_SCALE);
    canvas.style.transform = `scale(${scale}) translate(${currentX}px, ${currentY}px)`;
}, { passive: false });

// handle panning using mouse middle button and dragging

canvas.addEventListener('mousedown', (e) => {
    e.preventDefault();
    if (e.button === 1) { // middle button
        isPanning = true;
        clickedX = e.clientX - currentX;
        clickedY = e.clientY - currentY;
    }
}, { passive: false });

canvas.addEventListener('mouseup', () => {
    isPanning = false;
}, { passive: false });

canvas.addEventListener('mousemove', (e) => {
    if (isPanning) {
        currentX = Math.min(Math.max(MIN_X, e.clientX - clickedX), MAX_X);
        currentY = Math.min(Math.max(MIN_Y, e.clientY - clickedY), MAX_Y);
        canvas.style.transform = `scale(${scale}) translate(${currentX}px, ${currentY}px)`;
    }
}, { passive: false });
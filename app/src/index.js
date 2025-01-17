
document.addEventListener('DOMContentLoaded', () => {
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

    const canvasContainer = document.querySelector('.canvas-container'); // a div containing only the canvas
    const canvas = document.querySelector('#canvas'); // the canvas element
    const ctx = canvas.getContext('2d');
    
});
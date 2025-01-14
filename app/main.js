const { app, BrowserWindow, dialog, ipcMain } = require('electron/main');
const path = require('node:path');

const createWindow = () => {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            preload: path.join(__dirname, 'preload.js')
        },
        titleBarStyle: 'hidden',
        ...(process.platform !== 'darwin' ? { titleBarOverlay: true } : {}),
    });

    win.loadFile('dist/index.html');
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createWindow();
        }
    });
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
});

ipcMain.handle('dialog:openFile', async () => {
    const result = await dialog.showOpenDialog({
        properties: ['openFile']
    });
    return result.filePaths;
});

ipcMain.handle('dialog:saveFile', async () => {
    const result = await dialog.showSaveDialog();
    return result.filePath;
});

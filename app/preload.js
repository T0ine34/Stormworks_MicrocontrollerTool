const { contextBridge, ipcRenderer } = require('electron');


contextBridge.exposeInMainWorld('versions', {
	node: () => process.versions.node,
	chrome: () => process.versions.chrome,
	electron: () => process.versions.electron
});

contextBridge.exposeInMainWorld('file', {
	open: () => ipcRenderer.invoke('dialog:openFile'),
	save: () => ipcRenderer.invoke('dialog:saveFile')
});
const { app, BrowserWindow } = require('electron')

const createWindow = () => {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    resizable: false,
  })

  const textData = encodeURIComponent('from_ftp_electron_gui');
  win.loadURL(`http://127.0.0.1:541/?data=${textData}`);

  win.setMenu(null);
}

app.whenReady().then(() => {
  // 检查是否传入了 "--flask-start" 参数
  if (process.argv.includes('--flask-start')) {
    createWindow();
  } else {
    console.log('No have "--flask-start.');
    // 如果不需要做其他事情，可以简单地返回或让应用退出
    app.quit(); // 如果希望应用在没有参数时不显示窗口就退出，可以取消注释这行
  }
})
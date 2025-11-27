// json定义
interface flask_send {
    id: String;
    data: object;
}

//绑定按钮
const taskbar_status = document.getElementById('taskbar_status') as HTMLButtonElement
const taskbar_ftpset = document.getElementById('taskbar_ftpset') as HTMLButtonElement
const taskbar_system = document.getElementById('taskbar_system') as HTMLButtonElement
const taskbar_about = document.getElementById('taskbar_about') as HTMLButtonElement
// 按钮事件
taskbar_status.addEventListener('click', (event: MouseEvent) => {
    const data: flask_send = { id: 'taskbar_status', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
});
taskbar_ftpset.addEventListener('click', (event: MouseEvent) => {
    const data: flask_send = { id: 'taskbar_ftpset', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
});
taskbar_system.addEventListener('click', (event: MouseEvent) => {
    const data: flask_send = { id: 'taskbar_system', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
});
taskbar_about.addEventListener('click', (event: MouseEvent) => {
    const data: flask_send = { id: 'taskbar_about', data: {} };
    const response = fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });
});